from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

llm = ChatOpenAI(model="gpt-4o-mini")

@app.get("/ask")
def ask(question: str):
    response = llm.invoke(question)
    return {
        "answer": response.content
    }