from langchain.agents import create_agent

from app.tools.company_tool import get_company_name
from app.config.llm_config import llm

tools = [get_company_name]

# agent=initialize_agent(
#     tools=tools,
#     llm=llm,
#     agent=AgentType.OPENAI_FUNCTIONS,
#     verbose=True
# )

agent=create_agent(
    tools=tools,
    model=llm
)
