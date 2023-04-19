"""APITable Toolkit."""
from typing import List

from langchain.agents.agent_toolkits.base import BaseToolkit
from langchain.tools import BaseTool
from tool.tool import APITableAction
from utilities.apitable import APITableAPIWrapper


class APITableToolkit(BaseToolkit):
    """APITable Toolkit."""

    tools: List[BaseTool] = []

    @classmethod
    def from_apitable_api_wrapper(
        cls, apitable_api_wrapper: APITableAPIWrapper
    ) -> "APITableToolkit":
        actions = apitable_api_wrapper.list()
        tools = [
            APITableAction(
                name=action["name"],
                description=action["description"],
                mode=action["mode"],
                api_wrapper=apitable_api_wrapper,
            )
            for action in actions
        ]
        return cls(tools=tools)

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return self.tools
