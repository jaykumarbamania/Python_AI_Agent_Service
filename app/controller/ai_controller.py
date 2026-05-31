from fastapi import APIRouter

from app.agents.ai_agent import agent

router = APIRouter()

@router.get("/ask")
def ask(question: str):
    response = agent.invoke({
        "messages": [
            {
                "role" : "user",
                "content" : question
            }
        ]
    })

    print(response)
    
    return {
        "answer" : response["messages"][-1].content
    }


@router.get("/test")
def test(question: str):

    return {
        "status" : "Service is up and running",
        "your_question" : question
    }