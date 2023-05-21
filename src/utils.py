from typing import Generator
from fastapi import HTTPException
from sqlalchemy.exc import OperationalError

from src.database import SessionLocal


def get_db() -> Generator:
    with SessionLocal() as session:
        try:
            yield session
        except OperationalError as e:
            raise HTTPException(
                status_code=503,
                detail=f'Server closed the connection unexpectedly: {e}'
            )
