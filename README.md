# Flask CRUD Application

This is a simple CRUD (Create, Read, Update, Delete) application built using Flask and PostgreSQL.


## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

## Prerequisites

- Python 3.9 or higher
- PostgreSQL
- Git
- Virtualenv (optional but recommended)

## Installation

1. **Clone the repository:**

    ```sh
    git clone [https://github.com/your-username/flask-crud.git](https://github.com/Chandni-thakkar/Flask-CRUD.git)
    cd flask-crud
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. **Create a PostgreSQL database:**

    ```sql
    CREATE DATABASE flask_database;
    ```
    Update the database URL in the .env file (if not already set):
     DB_URL=postgresql://username:password@localhost/flask_db


## Running the Application

1. **Run the application:**

    ```sh
    flask run
    ```

    Access the application in your web browser at http://localhost:5000.

## API Endpoints

Endpoints
GET /employees: Get all employees.
POST /employees: Create a new employee.
GET /employees/<id>: Get employee by ID.
PUT /employees/<id>: Update employee by ID.
DELETE /employees/<id>: Delete employee by ID.

