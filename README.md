# API Test Framework

This project is a test framework for testing a REST API using Python and `pytest`. The API to be tested is an HTTP GET API.

## Project Structure

```
rest-api-test-python/
├── helpers/
│   ├── api_helper.py
├── tests/
│   ├── test_api.py
│   ├── conftest.py
├── requirements.txt
├── .gitignore
├── README.md
```

## Requirements

- Python 3.7+
- `requests` library
- `pytest` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/sorokoletovdu/rest-api-test-python.git
    cd rest-api-test-python
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
   
4. Add the project to the Python path:
   ```sh
   export PYTHONPATH=$(pwd)
   ```

## Usage

To run the tests, simply use `pytest`:

```sh
pytest