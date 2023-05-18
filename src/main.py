from fastapi import FastAPI

from src.questions.routers import ques_router


app = FastAPI(title='Test_task_Bewise.ai')
app.include_router(ques_router)
