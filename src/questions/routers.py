from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import desc
from sqlalchemy.orm import Session

from src.utils import get_db

from .crud import add_question, get_question_from_database
from .models import Question
from .schemas import LastQuestion
from .utils import get_response


ques_router = APIRouter(prefix='/question', tags=['questions'])


@ques_router.post('/',
                  summary='Запрос вопросов',
                  response_model=LastQuestion)
def request_question(
    questions_num: int,
    db: Annotated[Session, Depends(get_db)]
) -> LastQuestion:
    """
    Получение вопросов с API https://jservice.io/api/random?count=1,
    где questions_num: количество запрашиваемых вопросов
    """
    response = get_response(questions_num)
    last_question = db.query(Question).order_by(desc('id')).first()

    exists_question = get_question_from_database(response, db)
    while exists_question:
        response = get_response(questions_num)

    add_question(response, db)

    if last_question is None:
        return LastQuestion()
    return LastQuestion(question=last_question.question)
