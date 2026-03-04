import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dotenv import load_dotenv
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app
import services


from fastapi.testclient import TestClient
import database

load_dotenv()
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")


test_engine = create_engine(TEST_DATABASE_URL, pool_pre_ping=True)
TestingSessionLocal = sessionmaker(bind=test_engine, autoflush=False, autocommit=False)

@pytest.fixture(scope="session", autouse=True)
def create_test_schema():
   #crea tablas en la db de test
   database.Base.metadata.create_all(bind=test_engine)
   yield
   database.Base.metadata.drop_all(bind=test_engine)

@pytest.fixture()
def db_session():
    #aislar cada test con transaccion y rollback
    connection = test_engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    try:
      yield session
    finally:
      session.close()
      transaction.rollback()
      connection.close()

@pytest.fixture()
def client(db_session):
    def override_get_db():
      yield db_session

    app.dependency_overrides[services.get_db] = override_get_db
    with TestClient(app) as c:
       yield c
    app.dependency_overrides.clear()


