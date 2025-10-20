from sqlalchemy.dialects.mysql import ENUM, SMALLINT, TEXT, TINYINT, VARCHAR
from sqlmodel import Field, SQLModel

_RELATIONSHIP_ENUM = ["Coreq", "Cross"]
_RESTRICTION_RULE_ENUM = ["Must be", "Cannot be"]
_SEMESTER_ENUM = ["Fall", "Spring", "Summer"]


class Course_Attribute(SQLModel, table=True):
    subj: str = Field(primary_key=True, foreign_key="course.subj", sa_type=VARCHAR(4))
    code_num: str = Field(
        primary_key=True, foreign_key="course.code_num", sa_type=VARCHAR(4)
    )
    attr: str = Field(
        primary_key=True, foreign_key="attribute_description.attr", sa_type=VARCHAR(4)
    )


class Attribute_Description(SQLModel, table=True):
    attr: str = Field(primary_key=True, sa_type=VARCHAR(4))
    description: str = Field(sa_type=VARCHAR(255))


class Course_Relationship(SQLModel, table=True):
    subj: str = Field(primary_key=True, foreign_key="course.subj", sa_type=VARCHAR(4))
    code_num: str = Field(
        primary_key=True, foreign_key="course.code_num", sa_type=VARCHAR(4)
    )
    relationship: str = Field(primary_key=True, sa_type=ENUM(*_RELATIONSHIP_ENUM))
    rel_subj: str = Field(
        primary_key=True, foreign_key="course.subj", sa_type=VARCHAR(4)
    )
    rel_code_num: str = Field(
        primary_key=True, foreign_key="course.code_num", sa_type=VARCHAR(4)
    )


class Course_Restriction(SQLModel, table=True):
    subj: str = Field(primary_key=True, foreign_key="course.subj", sa_type=VARCHAR(4))
    code_num: str = Field(
        primary_key=True, foreign_key="course.code_num", sa_type=VARCHAR(4)
    )
    category: str = Field(
        primary_key=True,
        foreign_key="restriction_description.category",
        sa_type=VARCHAR(50),
    )
    restr_rule: str = Field(
        primary_key=True,
        sa_type=ENUM(*_RESTRICTION_RULE_ENUM),
    )
    restriction: str = Field(
        primary_key=True,
        foreign_key="restriction_description.restriction",
        sa_type=VARCHAR(50),
    )


class Restriction_Description(SQLModel, table=True):
    category: str = Field(primary_key=True, sa_type=VARCHAR(50))
    restriction: str = Field(primary_key=True, sa_type=VARCHAR(20))
    description: str = Field(sa_type=VARCHAR(255))


class Course_Seats(SQLModel, table=True):
    sem_year: int = Field(primary_key=True, sa_type=SMALLINT)
    semester: str = Field(primary_key=True, sa_type=ENUM(*_SEMESTER_ENUM))
    subj: str = Field(primary_key=True, foreign_key="course.subj", sa_type=VARCHAR(4))
    code_num: str = Field(
        primary_key=True, foreign_key="course.code_num", sa_type=VARCHAR(4)
    )
    seats_filled: int = Field(sa_type=TINYINT)
    seats_total: int = Field(sa_type=TINYINT)


class Course(SQLModel, table=True):
    subj: str = Field(
        primary_key=True, foreign_key="subject_description.subj", sa_type=VARCHAR(4)
    )
    code_num: str = Field(primary_key=True, sa_type=VARCHAR(4))
    title: str = Field(sa_type=VARCHAR(255))
    desc_text: str = Field(sa_type=TEXT)
    credit_min: int = Field(sa_type=TINYINT)
    credit_max: int = Field(sa_type=TINYINT)


class Subject_Description(SQLModel, table=True):
    subj: str = Field(primary_key=True, sa_type=VARCHAR(4))
    description: str = Field(sa_type=VARCHAR(255))


class Professor(SQLModel, table=True):
    sem_year: int = Field(primary_key=True, sa_type=SMALLINT)
    semester: str = Field(primary_key=True, sa_type=ENUM(*_SEMESTER_ENUM))
    subj: str = Field(primary_key=True, foreign_key="course.subj", sa_type=VARCHAR(4))
    code_num: str = Field(
        primary_key=True, foreign_key="course.code_num", sa_type=VARCHAR(4)
    )
    prof_name: str = Field(primary_key=True, sa_type=VARCHAR(255))
