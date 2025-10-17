# database-schema
CARPI MySQL database schemas as Pydantic models.

## Overview
This package provides Pydantic models (using SQLModel) for CARPI's MySQL database tables. These models can be shared across multiple repositories to ensure consistency in database schema definitions.

## Installation

```bash
pip install git+https://github.com/Project-CARPI/database-schema.git
```

## Usage

```python
from carpi_db_models import Course, Professor, Course_Seats

# Use the models in your application
course = Course(
    dept="CS",
    code_num="1234",
    title="Introduction to Programming",
    desc_text="A beginner's course in programming",
    credit_min=3,
    credit_max=3
)
```

## Available Models

- `Course`: Course information
- `Professor`: Professor assignments
- `Course_Attribute`: Course attributes (e.g., Writing Intensive)
- `Course_Relationship`: Course relationships (Coreq, Cross-listed)
- `Course_Restriction`: Course restrictions
- `Course_Seats`: Course seat availability

## Development

### Running Tests

```bash
pip install -e ".[dev]"
pytest tests/
```

### Building the Package

```bash
pip install build
python -m build
```
