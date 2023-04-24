from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
import os
from apitable_toolkit.tool.prompt import PREFIX, FORMAT_INSTRUCTIONS, SUFFIX
from langchain.chat_models import ChatOpenAI
from apitable_toolkit.toolkit import APITableToolkit
from apitable_toolkit.utilities.apitable import APITableAPIWrapper
from langchain.callbacks import get_openai_callback

llm = ChatOpenAI(temperature=0)

apitable = APITableAPIWrapper()
toolkit = APITableToolkit.from_apitable_api_wrapper(apitable)
agent = initialize_agent(
    toolkit.get_tools(),
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    agent_kwargs={
        "prefix": PREFIX,
        "format_instructions": FORMAT_INSTRUCTIONS,
        "suffix": SUFFIX,
    },
)

with get_openai_callback() as cb:
    agent.run("What spaces do I have")
    # agent.run("What datasheets do I have")

    # TODO: need to make AI understand what is node.
    # TODO: need to make AI do not make up tools.
    # agent.run(
    #     "The space_id is spctqtTZpssYw. Tell me the datasheet ID whose name has 'MAU' in this space"
    # )

    # agent.run("Tell me the latest value of APITable MAU in xukecheng's space")
    # agent.run("Create all field type fields in AITEST of xukecheng's space")
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Successful Requests: {cb.successful_requests}")
    print(f"Total Cost (USD): ${cb.total_cost}")
