"""Util that calls APITable."""
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Extra, root_validator

from langchain.utils import get_from_dict_or_env

from apitable_toolkit.tool.prompt import (
    APITABLE_CATCH_ALL_PROMPT,
    APITABLE_GET_NODES_PROMPT,
    APITABLE_GET_RECORDS_PROMPT,
    APITABLE_GET_SPACES_PROMPT,
)


# TODO: think about error handling, more specific api specs
class APITableAPIWrapper(BaseModel):
    """Wrapper for APITable API."""

    apitable: Any  #: :meta private:
    apitable_api_token: str
    apitable_api_base: Optional[str] = "https://apitable.com"

    operations: List[Dict] = [
        {
            "mode": "get_spaces",
            "name": "Get Spaces",
            "description": APITABLE_GET_SPACES_PROMPT,
        },
        {
            "mode": "get_nodes",
            "name": "Get Nodes",
            "description": APITABLE_GET_NODES_PROMPT,
        },
        {
            "mode": "get_records",
            "name": "Get Records",
            "description": APITABLE_GET_RECORDS_PROMPT,
        },
        {
            "mode": "other",
            "name": "Catch all APITable API call",
            "description": APITABLE_CATCH_ALL_PROMPT,
        },
    ]

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    def list(self) -> List[Dict]:
        return self.operations

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key and python package exists in environment."""

        apitable_api_token = get_from_dict_or_env(
            values, "apitable_api_token", "APITABLE_API_TOKEN"
        )
        values["apitable_api_token"] = apitable_api_token

        apitable_api_base = get_from_dict_or_env(
            values, "apitable_api_base", "APITABLE_API_BASE"
        )
        values["apitable_api_base"] = apitable_api_base

        try:
            from apitable import Apitable
        except ImportError:
            raise ImportError(
                "apitable is not installed. "
                "Please install it with `pip install apitable`"
            )

        apitable = Apitable(token=apitable_api_token, api_base=apitable_api_base)
        values["apitable"] = apitable

        return values

    def trans_key(self, field_key_map, key: str):
        """
        When there is a field mapping, convert the mapped key to the actual key
        """
        if key in ["_id", "recordId"]:
            return key
        if field_key_map:
            _key = field_key_map.get(key, key)
            return _key
        return key

    def query_parse(self, field_key_map, **kwargs) -> str:
        query_list = []
        for k, v in kwargs.items():
            # Handling null
            if v is None:
                v = "BLANK()"
            # Handling string
            elif isinstance(v, str):
                v = f'"{v}"'
            elif isinstance(v, bool):
                v = "TRUE()" if v else "FALSE()"
            # Handling array type values, multiple select, members?
            elif isinstance(v, list):
                v = f'"{", ".join(v)}"'
            query_list.append(f"{{{self.trans_key(field_key_map, k)}}}={v}")
        if len(query_list) == 1:
            return query_list[0]
        else:
            qs = ",".join(query_list)
            return f"AND({qs})"

    def get_spaces(self) -> str:
        try:
            import json
        except ImportError:
            raise ImportError(
                "json is not installed. " "Please install it with `pip install json`"
            )
        spaces = self.apitable.spaces.all()
        parsed_spaces = [json.loads(space.json()) for space in spaces]
        parsed_spaces_str = (
            "Found " + str(len(parsed_spaces)) + " spaces:\n" + str(parsed_spaces)
        )
        return parsed_spaces_str

    def get_nodes(self, query: str) -> str:
        try:
            import json
        except ImportError:
            raise ImportError(
                "json is not installed. " "Please install it with `pip install json`"
            )
        params = json.loads(query)
        nodes = self.apitable.space(space_id=params["space_id"]).nodes.all()
        parsed_nodes = [json.loads(node.json()) for node in nodes]
        parsed_nodes_str = (
            "Found " + str(len(parsed_nodes)) + " nodes:\n" + str(parsed_nodes)
        )
        return parsed_nodes_str

    def get_records(self, query: str) -> str:
        try:
            import json
        except ImportError:
            raise ImportError(
                "json is not installed. " "Please install it with `pip install json`"
            )
        params = json.loads(query)
        datasheet_id = params["datasheet_id"]
        dst = self.apitable.datasheet(datasheet_id)
        if "filter_condition" in params:
            query_formula = self.query_parse(params["filter_condition"])
            records = dst.records.all(filterByFormula=query_formula)
        elif "sort_condition" in params:
            sort_condition = params["sort_condition"]
            records = dst.records.all(sort=sort_condition)
        elif "maxRecords_condition" in params:
            maxRecords_condition = params["maxRecords_condition"]
            records = dst.records.all(maxRecords=maxRecords_condition)
        else:
            records = dst.records.all()
        parsed_records = [record.json() for record in records]
        parsed_records_str = (
            "Found " + str(len(parsed_records)) + " records:\n" + str(parsed_records)
        )
        return parsed_records_str

    def other(self, query: str) -> str:
        context = {"self": self}
        exec(f"result = {query}", context)
        result = context["result"]
        return str(result)

    def run(self, mode: str, query: str) -> str:
        if mode == "get_spaces":
            return self.get_spaces()
        elif mode == "get_nodes":
            return self.get_nodes(query)
        elif mode == "get_records":
            return self.get_records(query)
        elif mode == "other":
            return self.other(query)
        else:
            raise ValueError(f"Got unexpected mode {mode}")
