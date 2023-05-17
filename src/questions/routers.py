from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import desc
from sqlalchemy.orm import Session

from src.utils import get_db

from .crud import add_question, get_question_from_database
from .models import Question
from .schemas import QuestionOut
from .utils import get_response


ques_router = APIRouter(prefix='/question', tags=['questions'])


@ques_router.post('/',
                  summary='Запрос вопросов',
                  response_model=QuestionOut)
def request_question(
    questions_num: int,
    db: Annotated[Session, Depends(get_db)]
) -> QuestionOut:
    """
    Получение вопросов с API https://jservice.io/api/random?count=1,
    где questions_num: количество запрашиваемых вопросов
    """
    response = get_response(questions_num)
    last_question = db.query(Question).order_by(desc('id')).first()

    exists_question = get_question_from_database(response, db)
    if exists_question:
        response = get_response(questions_num)

    add_question(response, db)

    if last_question is None:
        return QuestionOut()
    return QuestionOut(
        id=last_question.id,
        question_id=last_question.question_id,
        question=last_question.question,
        answer=last_question.answer,
        created_at=last_question.created_at
    )
