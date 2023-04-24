from pydantic import Field

from langchain.tools.base import BaseTool
from apitable_toolkit.utilities.apitable import (
    APITableAPIWrapper,
)


class APITableAction(BaseTool):
    api_wrapper: APITableAPIWrapper = Field(default_factory=APITableAPIWrapper)
    name = ""
    description = ""

    def _run(self, instructions: str) -> str:
        """Use the APITable API to run an operation."""
        return self.api_wrapper.run(self.name, instructions)

    async def _arun(self, _: str) -> str:
        """Use theAPITable to run an operation."""
        raise NotImplementedError("APITableAction does not support async")
