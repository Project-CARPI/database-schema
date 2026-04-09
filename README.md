# database-schema

This repository is a Python package that contains SQLAlchemy data models for use in the CARPI Course Planner project.

## Installing as a Dependency

In your project's dependency list (often named `requirements.txt` or similar), add the following line:

```
carpi-data-model @ git+https://github.com/Project-CARPI/database-schema.git
```

If installing directly on the command line using pip, use the following command:

```bash
pip3 install git+https://github.com/Project-CARPI/database-schema.git
```

## Local Development & Testing

Along with the core SQLAlchemy models, this repository includes a PyTest-based test suite.

### Prerequisites

- **Python >= 3.10**: If you don't have it installed, [download it here.](https://www.python.org/)
- **Docker**: Required to automatically spin up temporary MySQL containers during testing. [Download Docker Desktop here.](https://www.docker.com/products/docker-desktop/)

### Setup Instructions

**1. Set Up a Virtual Environment**
To avoid cluttering your global Python environment, create a virtual environment in the project root:

```bash
# Create a virtual environment directory named .venv
python -m venv .venv
```

**2. Activate the Environment**
Depending on your operating system, activate the virtual environment:

- **Windows:**
  ```powershell
  .venv\Scripts\activate
  ```
- **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

You will see a `(.venv)` prefix in your terminal prompt when the environment is successfully active:

```bash
(.venv) raymond@Macbook-Pro database-schema %
```

**3. Install Required Dependencies**
With the virtual environment active, install the required packages for testing:

```bash
pip install -r requirements.txt
```

### Running the Tests

Once your environment is set up and **Docker is running** in the background, you can execute the test suite using pytest:

```bash
pytest tests/
```

To exit the virtual environment when you are finished, run the deactivate command:

```bash
deactivate
```
