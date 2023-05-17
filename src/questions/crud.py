import json

from fastapi import HTTPException
from sqlalchemy.orm import Session

from .models import Question


def get_question_from_database(response: json, db: Session) -> bool:
    for ques in response:
        question = db.query(Question).filter(
            Question.question_id == ques.get('id')
        ).first()
        if question is not None:
            return True
        return False


def add_question(response: json, db: Session) -> dict | None:
    if response is None:
        raise HTTPException(
            status_code=404,
            detail='Question is not found'
        )
    for ques in response:
        question = Question(
            question_id=ques.get('id'),
            question=ques.get('question'),
            answer=ques.get('answer'),
            created_at=ques.get('created_at')
        )
        db.add(question)
        db.commit()
        db.refresh(question)
