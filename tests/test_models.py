import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from testcontainers.mysql import MySqlContainer

from carpi_data_model.models import *


@pytest.fixture(scope="session")
def engine():
    """
    Spin up a temporary MySQL Docker container for the whole test session. This
    requires Docker to be running on your machine.
    """
    with MySqlContainer("mysql:8.0", dialect="mysqlconnector") as mysql:
        yield create_engine(mysql.get_connection_url(), echo=False)


@pytest.fixture(autouse=True)
def setup_database(engine):
    """
    Creates all tables before each test and drops them after to ensure a clean
    state for every test.
    """
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_create_tables(engine):
    """
    Test that the SQLAlchemy schema can be translated into DDL and executed
    in a Native MySQL database without throwing any mapping or constraint
    errors.
    """
    assert Subject.__tablename__ in Base.metadata.tables
    assert Attribute.__tablename__ in Base.metadata.tables
    assert Restriction.__tablename__ in Base.metadata.tables
    assert Faculty.__tablename__ in Base.metadata.tables
    assert Course.__tablename__ in Base.metadata.tables
    assert Course_Attribute.__tablename__ in Base.metadata.tables
    assert Course_Relationship.__tablename__ in Base.metadata.tables
    assert Course_Restriction.__tablename__ in Base.metadata.tables
    assert Course_Offering.__tablename__ in Base.metadata.tables
    assert Course_Faculty.__tablename__ in Base.metadata.tables


def test_insert_and_query(engine):
    """
    Test basic database operations (insert and query) on a table
    to ensure the ORM definitions functionally work.
    """
    with Session(engine) as session:
        subj = Subject(subj_code="CSCI", title="Computer Science")
        session.add(subj)
        session.commit()

        fetched = session.query(Subject).filter_by(subj_code="CSCI").first()
        assert fetched is not None
        assert fetched.subj_code == "CSCI"
        assert fetched.title == "Computer Science"
