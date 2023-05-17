from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class QuestionOut(BaseModel):
    id: Optional[int]
    question_id: Optional[int]
    question: Optional[str]
    answer: Optional[str]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
