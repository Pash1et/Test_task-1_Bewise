import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app
from src.utils import get_db
from fastapi.testclient import TestClient
from src.database import Base

SQLALCHEMY_DATABASE_URL = ('postgresql://postgres_test:postgres_test@'
                           '127.0.0.1:5434/postgres_test')

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False,
                                   autoflush=False,
                                   bind=engine)


def override_get_db():
    Base.metadata.create_all(bind=engine)
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True, scope='session')
def create_db():
    Base.metadata.create_all(bind=engine)


@pytest.fixture(autouse=True, scope='session')
def drop_db():
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    return TestClient(app)
