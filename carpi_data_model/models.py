from sqlalchemy import Column, ForeignKey, ForeignKeyConstraint
from sqlalchemy.dialects.mysql import ENUM, SMALLINT, TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import declarative_base

Base = declarative_base()

_RELATIONSHIP_ENUM = ["Coreq", "Cross"]
_RESTRICTION_RULE_ENUM = ["Must be", "Cannot be"]
_SEMESTER_ENUM = ["Fall", "Spring", "Summer"]


class Subject_Description(Base):
    __tablename__ = "subject_description"

    subj = Column(VARCHAR(4), primary_key=True)
    description = Column(VARCHAR(255), nullable=False)


class Attribute_Description(Base):
    __tablename__ = "attribute_description"

    attr = Column(VARCHAR(4), primary_key=True)
    description = Column(VARCHAR(255), nullable=False)


class Restriction_Description(Base):
    __tablename__ = "restriction_description"

    category = Column(VARCHAR(50), primary_key=True)
    restriction = Column(VARCHAR(20), primary_key=True)
    description = Column(VARCHAR(255), nullable=False)


class Course(Base):
    __tablename__ = "course"

    subj = Column(VARCHAR(4), ForeignKey("subject_description.subj"), primary_key=True)
    code_num = Column(VARCHAR(4), primary_key=True)
    title = Column(VARCHAR(255), nullable=False)
    desc_text = Column(TEXT, nullable=False)
    credit_min = Column(TINYINT, nullable=False)
    credit_max = Column(TINYINT, nullable=False)


class Course_Attribute(Base):
    __tablename__ = "course_attribute"

    subj = Column(VARCHAR(4), primary_key=True)
    code_num = Column(VARCHAR(4), primary_key=True)
    attr = Column(
        VARCHAR(4), ForeignKey("attribute_description.attr"), primary_key=True
    )

    __table_args__ = (
        ForeignKeyConstraint(["subj", "code_num"], ["course.subj", "course.code_num"]),
    )


class Course_Relationship(Base):
    __tablename__ = "course_relationship"

    subj = Column(VARCHAR(4), primary_key=True)
    code_num = Column(VARCHAR(4), primary_key=True)
    relationship = Column(ENUM(*_RELATIONSHIP_ENUM), primary_key=True)
    rel_subj = Column(VARCHAR(4), primary_key=True)
    rel_code_num = Column(VARCHAR(4), primary_key=True)

    __table_args__ = (
        ForeignKeyConstraint(["subj", "code_num"], ["course.subj", "course.code_num"]),
        ForeignKeyConstraint(
            ["rel_subj", "rel_code_num"], ["course.subj", "course.code_num"]
        ),
    )


class Course_Restriction(Base):
    __tablename__ = "course_restriction"

    subj = Column(VARCHAR(4), primary_key=True)
    code_num = Column(VARCHAR(4), primary_key=True)
    category = Column(VARCHAR(50), primary_key=True)
    restr_rule = Column(ENUM(*_RESTRICTION_RULE_ENUM), primary_key=True)
    restriction = Column(VARCHAR(50), primary_key=True)

    __table_args__ = (
        ForeignKeyConstraint(["subj", "code_num"], ["course.subj", "course.code_num"]),
        ForeignKeyConstraint(
            ["category", "restriction"],
            ["restriction_description.category", "restriction_description.restriction"],
        ),
    )


class Course_Seats(Base):
    __tablename__ = "course_seats"

    sem_year = Column(SMALLINT, primary_key=True)
    semester = Column(ENUM(*_SEMESTER_ENUM), primary_key=True)
    subj = Column(VARCHAR(4), primary_key=True)
    code_num = Column(VARCHAR(4), primary_key=True)
    seats_filled = Column(TINYINT, nullable=False)
    seats_total = Column(TINYINT, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(["subj", "code_num"], ["course.subj", "course.code_num"]),
    )


class Professor(Base):
    __tablename__ = "professor"

    sem_year = Column(SMALLINT, primary_key=True)
    semester = Column(ENUM(*_SEMESTER_ENUM), primary_key=True)
    subj = Column(VARCHAR(4), primary_key=True)
    code_num = Column(VARCHAR(4), primary_key=True)
    prof_name = Column(VARCHAR(255), primary_key=True)

    __table_args__ = (
        ForeignKeyConstraint(["subj", "code_num"], ["course.subj", "course.code_num"]),
    )
