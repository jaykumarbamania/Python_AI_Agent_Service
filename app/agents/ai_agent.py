from langchain.agents import create_agent

from app.tools.company_tool import get_company_name
from app.tools.order_tool import get_order_status

from app.config.llm_config import llm

from app.prompts.system_prompt import SYSTEM_PROMPT

tools = [get_company_name, get_order_status]

# agent=initialize_agent(
#     tools=tools,
#     llm=llm,
#     agent=AgentType.OPENAI_FUNCTIONS,
#     verbose=True
# )

agent=create_agent(
    tools=tools,
    model=llm,
    debug=True,
    system_prompt=SYSTEM_PROMPT
)
