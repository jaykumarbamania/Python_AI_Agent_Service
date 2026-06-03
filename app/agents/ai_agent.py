from langchain.agents import create_agent

from app.tools.company_tool import get_company_name
from app.tools.order_tool import get_order_status
from app.tools.customer_tool import get_customer_details
from app.tools.product_tool import get_product_details

from app.config.llm_config import llm

from app.prompts.system_prompt import SYSTEM_PROMPT

tools = [get_company_name, get_order_status, get_customer_details, get_product_details]

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
