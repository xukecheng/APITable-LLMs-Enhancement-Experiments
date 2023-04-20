from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
import os

from langchain.chat_models import ChatOpenAI

from apitable_toolkit.toolkit import APITableToolkit
from apitable_toolkit.utilities.apitable import APITableAPIWrapper

os.environ["OPENAI_API_KEY"] = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

llm = ChatOpenAI(temperature=0)
apitable = APITableAPIWrapper(
    apitable_api_token="uskxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
)
toolkit = APITableToolkit.from_apitable_api_wrapper(apitable)
agent = initialize_agent(
    toolkit.get_tools(),
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)
# agent.run("What spaces do I have")
# agent.run("What datasheets do I have")

# TODO: need to make AI understand what is node.
# TODO: need to make AI do not make up tools.

# agent.run(
#     "The space_id is spctqtTZpssYw. Tell me the datasheet ID whose name has 'MAU' in this space"
# )

agent.run("Tell me the latest value of APITable MAU in xukecheng's space")
