from typing import Optional

from pydantic import BaseModel


class LastQuestion(BaseModel):
    question: Optional[str]

    class Config:
        orm_mode = True
