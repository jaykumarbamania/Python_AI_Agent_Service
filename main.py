from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

llm = ChatOpenAI(model="gpt-4o-mini")


#Create tool
from langchain.tools import tool

@tool
def get_company_name():
    """Returns company name"""

    return "Jay OMS Pvt Ltd"

#Register tool
from langchain.agents import initialize_agent
from langchain.agents import AgentType
tools = [get_company_name]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)


@app.get("/ask")
def ask(question: str):
    # response = llm.invoke(question)
    response = agent.run(question)
    return {
        "answer": response.content
    }