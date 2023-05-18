from fastapi import HTTPException
from sqlalchemy.exc import OperationalError

from src.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    except OperationalError as e:
        raise HTTPException(
            status_code=503,
            detail=f'Server closed the connection unexpectedly: {e}'
        )
    finally:
        db.close()
