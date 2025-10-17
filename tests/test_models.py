"""
Tests for CARPI database models.

This module contains basic tests to verify that all models can be imported
and instantiated correctly.
"""

import pytest
from carpi_db_models import (
    Course,
    Professor,
    Course_Attribute,
    Course_Relationship,
    Course_Restriction,
    Course_Seats,
)


def test_course_model():
    """Test Course model instantiation."""
    course = Course(
        dept="CS",
        code_num="1234",
        title="Test Course",
        desc_text="Test description",
        credit_min=3,
        credit_max=4,
    )
    assert course.dept == "CS"
    assert course.code_num == "1234"
    assert course.title == "Test Course"
    assert course.credit_min == 3
    assert course.credit_max == 4


def test_professor_model():
    """Test Professor model instantiation."""
    prof = Professor(
        sem_year=2024,
        semester="Fall",
        dept="CS",
        code_num="1234",
        prof_name="Dr. Smith",
    )
    assert prof.sem_year == 2024
    assert prof.semester == "Fall"
    assert prof.prof_name == "Dr. Smith"


def test_course_attribute_model():
    """Test Course_Attribute model instantiation."""
    attr = Course_Attribute(
        dept="CS",
        code_num="1234",
        attr="Writing Intensive",
    )
    assert attr.dept == "CS"
    assert attr.attr == "Writing Intensive"


def test_course_relationship_model():
    """Test Course_Relationship model instantiation."""
    rel = Course_Relationship(
        dept="CS",
        code_num="1234",
        relationship="Coreq",
        rel_dept="MA",
        rel_code_num="1021",
    )
    assert rel.relationship == "Coreq"
    assert rel.rel_dept == "MA"


def test_course_restriction_model():
    """Test Course_Restriction model instantiation."""
    restr = Course_Restriction(
        dept="CS",
        code_num="1234",
        category="Major",
        restr_rule="Must be",
        restriction="Computer Science",
    )
    assert restr.category == "Major"
    assert restr.restr_rule == "Must be"


def test_course_seats_model():
    """Test Course_Seats model instantiation."""
    seats = Course_Seats(
        sem_year=2024,
        semester="Fall",
        dept="CS",
        code_num="1234",
        seats_filled=25,
        seats_total=30,
    )
    assert seats.seats_filled == 25
    assert seats.seats_total == 30


def test_all_models_importable():
    """Test that all models can be imported from the package."""
    from carpi_db_models import (
        Course,
        Professor,
        Course_Attribute,
        Course_Relationship,
        Course_Restriction,
        Course_Seats,
    )

    # Verify they are all classes
    assert isinstance(Course, type)
    assert isinstance(Professor, type)
    assert isinstance(Course_Attribute, type)
    assert isinstance(Course_Relationship, type)
    assert isinstance(Course_Restriction, type)
    assert isinstance(Course_Seats, type)
