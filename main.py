from fastapi import FastAPI

from app.controller.ai_controller import router

app = FastAPI()

app.include_router(router)