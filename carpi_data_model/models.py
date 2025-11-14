from enum import Enum as PyEnum

from sqlalchemy import Enum as SQLEnum
from sqlalchemy import ForeignKey, ForeignKeyConstraint
from sqlalchemy.dialects.mysql import SMALLINT, TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class RelationshipTypeEnum(str, PyEnum):
    COREQUISITE = "COREQ"
    CROSSLIST = "CROSS"


class RestrictionRuleEnum(str, PyEnum):
    MUST_BE = "MUST_BE"
    CANNOT_BE = "CANNOT_BE"


class RestrictionTypeEnum(str, PyEnum):
    MAJOR = "MAJOR"
    MINOR = "MINOR"
    LEVEL = "LEVEL"
    CLASSIFICATION = "CLASSIFICATION"
    DEGREE = "DEGREE"
    DEPARTMENT = "DEPARTMENT"
    CAMPUS = "CAMPUS"
    COLLEGE = "COLLEGE"


class SemesterEnum(str, PyEnum):
    FALL = "FALL"
    SPRING = "SPRING"
    SUMMER = "SUMMER"


RELATIONSHIP_TYPE_ENUM = SQLEnum(
    RelationshipTypeEnum, name="relationship_type", native_enum=True
)
RESTRICTION_RULE_ENUM = SQLEnum(
    RestrictionRuleEnum, name="restriction_rule", native_enum=True
)
RESTRICTION_TYPE_ENUM = SQLEnum(
    RestrictionTypeEnum, name="restriction_type", native_enum=True
)
SEMESTER_ENUM = SQLEnum(SemesterEnum, name="semester", native_enum=True)


class Subject(Base):
    __tablename__ = "subject"

    subj_code: Mapped[str] = mapped_column(VARCHAR(4), primary_key=True)
    title: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)


class Attribute(Base):
    __tablename__ = "attribute"

    attr_code: Mapped[str] = mapped_column(VARCHAR(4), primary_key=True)
    title: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)


class Restriction(Base):
    __tablename__ = "restriction"

    category: Mapped[RestrictionTypeEnum] = mapped_column(
        RESTRICTION_TYPE_ENUM, primary_key=True
    )
    restr_code: Mapped[str] = mapped_column(VARCHAR(20), primary_key=True)
    title: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)


class Faculty(Base):
    __tablename__ = "faculty"

    rcsid: Mapped[str] = mapped_column(VARCHAR(15), primary_key=True)
    first_name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    last_name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)


class Course(Base):
    __tablename__ = "course"

    subj_code: Mapped[str] = mapped_column(
        VARCHAR(4), ForeignKey("subject.subj_code"), primary_key=True
    )
    code_num: Mapped[str] = mapped_column(VARCHAR(4), primary_key=True)
    title: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    desc_text: Mapped[str] = mapped_column(TEXT, nullable=False)
    credit_min: Mapped[int] = mapped_column(TINYINT, nullable=False)
    credit_max: Mapped[int] = mapped_column(TINYINT, nullable=False)


class Course_Attribute(Base):
    __tablename__ = "course_attribute"

    subj_code: Mapped[str] = mapped_column(VARCHAR(4), primary_key=True)
    code_num: Mapped[str] = mapped_column(VARCHAR(4), primary_key=True)
    attr_code: Mapped[str] = mapped_column(
        VARCHAR(4), ForeignKey("attribute.attr_code"), primary_key=True
    )

    __table_args__ = (
        ForeignKeyConstraint(
            ["subj_code", "code_num"], ["course.subj_code", "course.code_num"]
        ),
    )


class Course_Relationship(Base):
    __tablename__ = "course_relationship"

    subj_code: Mapped[str] = mapped_column(VARCHAR(4), primary_key=True)
    code_num: Mapped[str] = mapped_column(VARCHAR(4), primary_key=True)
    relationship: Mapped[RelationshipTypeEnum] = mapped_column(
        RELATIONSHIP_TYPE_ENUM, nullable=False
    )
    rel_subj: Mapped[str] = mapped_column(VARCHAR(4), primary_key=True)
    rel_code_num: Mapped[str] = mapped_column(VARCHAR(4), primary_key=True)

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

    subj_code: Mapped[str] = mapped_column(VARCHAR(4), primary_key=True)
    code_num: Mapped[str] = mapped_column(VARCHAR(4), primary_key=True)
    restr_rule: Mapped[RestrictionRuleEnum] = mapped_column(
        RESTRICTION_RULE_ENUM, nullable=False
    )
    category: Mapped[RestrictionTypeEnum] = mapped_column(
        RESTRICTION_TYPE_ENUM, primary_key=True
    )
    restr_code: Mapped[str] = mapped_column(VARCHAR(20), primary_key=True)

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

    sem_year: Mapped[int] = mapped_column(SMALLINT, primary_key=True)
    semester: Mapped[SemesterEnum] = mapped_column(SEMESTER_ENUM, primary_key=True)
    subj_code: Mapped[str] = mapped_column(VARCHAR(4), primary_key=True)
    code_num: Mapped[str] = mapped_column(VARCHAR(4), primary_key=True)
    seats_filled: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    seats_total: Mapped[int] = mapped_column(SMALLINT, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            ["subj_code", "code_num"], ["course.subj_code", "course.code_num"]
        ),
    )


class Course_Faculty(Base):
    __tablename__ = "course_faculty"

    sem_year: Mapped[int] = mapped_column(SMALLINT, primary_key=True)
    semester: Mapped[SemesterEnum] = mapped_column(SEMESTER_ENUM, primary_key=True)
    subj_code: Mapped[str] = mapped_column(VARCHAR(4), primary_key=True)
    code_num: Mapped[str] = mapped_column(VARCHAR(4), primary_key=True)
    rcsid: Mapped[str] = mapped_column(
        VARCHAR(15), ForeignKey("faculty.rcsid"), primary_key=True
    )

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
