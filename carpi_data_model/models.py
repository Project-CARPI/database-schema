from sqlalchemy.dialects.mysql import ENUM, SMALLINT, TEXT, TINYINT, VARCHAR
from sqlmodel import Field, SQLModel

_ATTR_ENUM = [
    "Communication Intensive",
    "Culminating Exp/Capstone",
    "Data Intensive I",
    "Data Intensive II",
    "Writing Intensive",
    "HASS Inquiry",
    "Introductory Level Course",
    "PDII Option for Engr Majors",
]

_RELATIONSHIP_ENUM = ["Coreq", "Cross"]
_CATEGORY_ENUM = ["Major", "Level", "Classification"]
_RESTRICTION_ENUM = ["Must be", "May not be"]
_SEMESTER_ENUM = ["Fall", "Spring", "Summer"]


class Course_Attribute(SQLModel, table=True):
    dept: str = Field(primary_key=True, sa_type=VARCHAR(4))
    code_num: str = Field(primary_key=True, sa_type=VARCHAR(4))
    attr: str = Field(primary_key=True, sa_type=ENUM(*_ATTR_ENUM))


class Course_Relationship(SQLModel, table=True):
    dept: str = Field(primary_key=True, sa_type=VARCHAR(4))
    code_num: str = Field(primary_key=True, sa_type=VARCHAR(4))
    relationship: str = Field(primary_key=True, sa_type=ENUM(*_RELATIONSHIP_ENUM))
    rel_dept: str = Field(primary_key=True, sa_type=VARCHAR(4))
    rel_code_num: str = Field(primary_key=True, sa_type=VARCHAR(4))


class Course_Restriction(SQLModel, table=True):
    dept: str = Field(primary_key=True, sa_type=VARCHAR(4))
    code_num: str = Field(primary_key=True, sa_type=VARCHAR(4))
    category: str = Field(primary_key=True, sa_type=ENUM(*_CATEGORY_ENUM))
    restr_rule: str = Field(primary_key=True, sa_type=ENUM(*_RESTRICTION_ENUM))
    restriction: str = Field(primary_key=True, sa_type=VARCHAR(255))


class Course_Seats(SQLModel, table=True):
    sem_year: int = Field(primary_key=True, sa_type=SMALLINT)
    semester: str = Field(primary_key=True, sa_type=ENUM(*_SEMESTER_ENUM))
    dept: str = Field(primary_key=True, sa_type=VARCHAR(4))
    code_num: str = Field(primary_key=True, sa_type=VARCHAR(4))
    seats_filled: int = Field(sa_type=TINYINT)
    seats_total: int = Field(sa_type=TINYINT)


class Course(SQLModel, table=True):
    dept: str = Field(primary_key=True, sa_type=VARCHAR(4))
    code_num: str = Field(primary_key=True, sa_type=VARCHAR(4))
    title: str = Field(sa_type=VARCHAR(255))
    desc_text: str = Field(sa_type=TEXT)
    credit_min: int = Field(sa_type=TINYINT)
    credit_max: int = Field(sa_type=TINYINT)


class Professor(SQLModel, table=True):
    sem_year: int = Field(primary_key=True, sa_type=SMALLINT)
    semester: str = Field(primary_key=True, sa_type=ENUM(*_SEMESTER_ENUM))
    dept: str = Field(primary_key=True, sa_type=VARCHAR(4))
    code_num: str = Field(primary_key=True, sa_type=VARCHAR(4))
    prof_name: str = Field(primary_key=True, sa_type=VARCHAR(255))
