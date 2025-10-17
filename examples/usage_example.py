#!/usr/bin/env python3
"""
Example script demonstrating how to use the carpi_db_models package.

This script shows how other CARPI repositories can import and use
the database models.
"""

from carpi_db_models import (
    Course,
    Professor,
    Course_Attribute,
    Course_Relationship,
    Course_Restriction,
    Course_Seats,
)


def main():
    """Demonstrate usage of CARPI database models."""
    
    # Example 1: Creating a Course
    print("Example 1: Creating a Course")
    course = Course(
        dept="CS",
        code_num="2102",
        title="Object-Oriented Design Concepts",
        desc_text="Introduction to object-oriented programming",
        credit_min=3,
        credit_max=3,
    )
    print(f"  {course.dept} {course.code_num}: {course.title}")
    print()

    # Example 2: Creating a Professor
    print("Example 2: Creating a Professor")
    professor = Professor(
        sem_year=2024,
        semester="Fall",
        dept="CS",
        code_num="2102",
        prof_name="Dr. Jane Smith",
    )
    print(f"  {professor.prof_name} teaching {professor.dept} {professor.code_num}")
    print()

    # Example 3: Creating Course Attributes
    print("Example 3: Creating Course Attributes")
    attributes = [
        Course_Attribute(dept="CS", code_num="2102", attr="Writing Intensive"),
        Course_Attribute(dept="CS", code_num="2102", attr="HASS Inquiry"),
    ]
    for attr in attributes:
        print(f"  - {attr.attr}")
    print()

    # Example 4: Creating Course Seats
    print("Example 4: Creating Course Seats")
    seats = Course_Seats(
        sem_year=2024,
        semester="Fall",
        dept="CS",
        code_num="2102",
        seats_filled=28,
        seats_total=30,
    )
    print(f"  Seats: {seats.seats_filled}/{seats.seats_total}")
    print()

    # Example 5: Creating Course Relationships
    print("Example 5: Creating Course Relationships")
    relationship = Course_Relationship(
        dept="CS",
        code_num="2102",
        relationship="Coreq",
        rel_dept="MA",
        rel_code_num="1024",
    )
    print(
        f"  {relationship.dept} {relationship.code_num} "
        f"has {relationship.relationship} with "
        f"{relationship.rel_dept} {relationship.rel_code_num}"
    )
    print()

    # Example 6: Creating Course Restrictions
    print("Example 6: Creating Course Restrictions")
    restriction = Course_Restriction(
        dept="CS",
        code_num="2102",
        category="Major",
        restr_rule="Must be",
        restriction="Computer Science or Software Engineering",
    )
    print(f"  {restriction.restr_rule} {restriction.restriction}")


if __name__ == "__main__":
    main()
