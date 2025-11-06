from sqlalchemy import Column, Enum, ForeignKey, ForeignKeyConstraint
from sqlalchemy.dialects.mysql import SMALLINT, TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, declarative_base

Base: DeclarativeBase = declarative_base()

_RELATIONSHIP_ENUM = ["COREQ", "CROSS"]
_RESTRICTION_RULE_ENUM = ["MUST_BE", "CANNOT_BE"]
_RESTRICTION_TYPE_ENUM = [
    "MAJOR",
    "MINOR",
    "LEVEL",
    "CLASSIFICATION",
    "DEGREE",
    "DEPARTMENT",
    "CAMPUS",
    "COLLEGE",
]
_SEMESTER_ENUM = ["FALL", "SPRING", "SUMMER"]

RELATIONSHIP_ENUM = Enum(*_RELATIONSHIP_ENUM, name="relationship", native_enum=True)
RESTRICTION_RULE_ENUM = Enum(
    *_RESTRICTION_RULE_ENUM, name="restriction_rule", native_enum=True
)
RESTRICTION_TYPE_ENUM = Enum(
    *_RESTRICTION_TYPE_ENUM, name="restriction_type", native_enum=True
)
SEMESTER_ENUM = Enum(*_SEMESTER_ENUM, name="semester", native_enum=True)


class Subject(Base):
    __tablename__ = "subject"

    subj_code = Column(VARCHAR(4), primary_key=True)
    title = Column(VARCHAR(255), nullable=False)


class Attribute(Base):
    __tablename__ = "attribute"

    attr_code = Column(VARCHAR(4), primary_key=True)
    title = Column(VARCHAR(255), nullable=False)


class Restriction(Base):
    __tablename__ = "restriction"

    category = Column(RESTRICTION_TYPE_ENUM, primary_key=True)
    restr_code = Column(VARCHAR(20), primary_key=True)
    title = Column(VARCHAR(255), nullable=False)


class Faculty(Base):
    __tablename__ = "faculty"

    rcsid = Column(VARCHAR(15), primary_key=True)
    first_name = Column(VARCHAR(255), nullable=False)
    last_name = Column(VARCHAR(255), nullable=False)


class Course(Base):
    __tablename__ = "course"

    subj_code = Column(VARCHAR(4), ForeignKey("subject.subj_code"), primary_key=True)
    code_num = Column(VARCHAR(4), primary_key=True)
    title = Column(VARCHAR(255), nullable=False)
    desc_text = Column(TEXT, nullable=False)
    credit_min = Column(TINYINT, nullable=False)
    credit_max = Column(TINYINT, nullable=False)


class Course_Attribute(Base):
    __tablename__ = "course_attribute"

    subj_code = Column(VARCHAR(4), primary_key=True)
    code_num = Column(VARCHAR(4), primary_key=True)
    attr_code = Column(VARCHAR(4), ForeignKey("attribute.attr_code"), primary_key=True)

    __table_args__ = (
        ForeignKeyConstraint(
            ["subj_code", "code_num"], ["course.subj_code", "course.code_num"]
        ),
    )


class Course_Relationship(Base):
    __tablename__ = "course_relationship"

    subj_code = Column(VARCHAR(4), primary_key=True)
    code_num = Column(VARCHAR(4), primary_key=True)
    relationship = Column(RELATIONSHIP_ENUM, nullable=False)
    rel_subj = Column(VARCHAR(4), primary_key=True)
    rel_code_num = Column(VARCHAR(4), primary_key=True)

    __table_args__ = (
        ForeignKeyConstraint(
            ["subj_code", "code_num"], ["course.subj_code", "course.code_num"]
        ),
        ForeignKeyConstraint(
            ["rel_subj", "rel_code_num"], ["course.subj_code", "course.code_num"]
        ),
    )


class Course_Restriction(Base):
    __tablename__ = "course_restriction"

    subj_code = Column(VARCHAR(4), primary_key=True)
    code_num = Column(VARCHAR(4), primary_key=True)
    restr_rule = Column(RESTRICTION_RULE_ENUM, nullable=False)
    category = Column(RESTRICTION_TYPE_ENUM, primary_key=True)
    restr_code = Column(VARCHAR(20), primary_key=True)

    __table_args__ = (
        ForeignKeyConstraint(
            ["subj_code", "code_num"], ["course.subj_code", "course.code_num"]
        ),
        ForeignKeyConstraint(
            ["category", "restr_code"],
            ["restriction.category", "restriction.restr_code"],
        ),
    )


class Course_Offering(Base):
    __tablename__ = "course_offering"

    sem_year = Column(SMALLINT, primary_key=True)
    semester = Column(SEMESTER_ENUM, primary_key=True)
    subj_code = Column(VARCHAR(4), primary_key=True)
    code_num = Column(VARCHAR(4), primary_key=True)
    seats_filled = Column(TINYINT, nullable=False)
    seats_total = Column(TINYINT, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            ["subj_code", "code_num"], ["course.subj_code", "course.code_num"]
        ),
    )


class Course_Faculty(Base):
    __tablename__ = "course_faculty"

    sem_year = Column(SMALLINT, primary_key=True)
    semester = Column(SEMESTER_ENUM, primary_key=True)
    subj_code = Column(VARCHAR(4), primary_key=True)
    code_num = Column(VARCHAR(4), primary_key=True)
    rcsid = Column(VARCHAR(15), ForeignKey("faculty.rcsid"), primary_key=True)

    __table_args__ = (
        ForeignKeyConstraint(
            ["sem_year", "semester", "subj_code", "code_num"],
            [
                "course_offering.sem_year",
                "course_offering.semester",
                "course_offering.subj_code",
                "course_offering.code_num",
            ],
        ),
    )
