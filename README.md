# fastapi-contacts-api
A RESTful Contacts API built with FastAPI, PostgreSQL, SQLAlchemy, and Docker. Includes CRUD operations, dependency injection, and containerized development.

* REST API design
* Dependency injection with FastAPI
* PostgreSQL database integration
* SQLAlchemy ORM
* Docker containerization
* Environment configuration with .env
* Automated testing with pytest

## Techstack

| Technology | Purpose                               |
| ---------- | ------------------------------------- |
| FastAPI    | High-performance Python web framework |
| PostgreSQL | Relational database                   |
| SQLAlchemy | ORM for database models               |
| Docker     | Containerized development environment |
| Pytest     | Automated testing                     |
| Pydantic   | Data validation                       |

## Project Structure

fastapi-contacts-api
│
├── main.py                # FastAPI application entry point
├── database.py            # Database engine and session configuration
├── models.py              # SQLAlchemy database models
├── schemas.py             # Pydantic schemas for request/response validation
├── services.py            # Business logic and database operations
│
├── test/
│   ├── docker-compose.yml # PostgreSQL containers for development and testing
│   ├── conftest.py        # Pytest fixtures and test configuration
│   ├── test_contacts_api.py # API endpoint tests
│
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (database connection)
├── .gitignore             # Git ignored files
└── README.md              # Project documentation

## Features

* Create contacts
* Retrieve contacts
* Update contacts
* Delete contacts
* PostgreSQL database integration
* Containerized test database
* Clean architecture separation

## Setup instructions

### 1. Clone the repository
git clone https://github.com/yourusername/fastapi-contacts-api.git
cd fastapi-contacts-api

### 2. Create Python virtual environment
python -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

### 3. Environment configuration
Create a .env file in the project root.
DATABASE_URL=postgresql+psycopg2://USER:PASSWORD@127.0.0.1:4321/DBNAME
TEST_DATABASE_URL=postgresql+psycopg2://USER:PASSWORD@127.0.0.1:4322/TESTDBNAME

### 4. Start PostgreSQL containers
Inside the test folder run:
docker compose up -d
docker ps

### 5. Run the FastAPI server
uvicorn main:app --reload

Open interactive API documentation:
http://127.0.0.1:8000/docs


## Example API Endpoint
POST /api/contacts

```json
{
  "first_name": "Milu",
  "last_name": "Pajuelo",
  "email": "miluspajuelo@gmail.com",
  "phone_number": "2020020202"
}
```

## Inspect the Database
docker exec -it tests-db-1 psql -U myuser -d fastapi_db
\dt
\d contacts
SELECT * FROM contacts;
Example output: 

| id | first_name | last_name | email                   | phone_number | date_created           |
|----|------------|-----------|-------------------------|--------------|------------------------|
| 1  | Milu       | Pajuelo   | miluspajuelo@gmail.com  | 2020020202   | 2026-03-04 17:18:17+00 |

 \q

## Running Tests
docker compose up -d db_test
pytest -q

6 passed, 3 warnings in 0.15s

## Ports used

| Service    | Port |
| ---------- | ---- |
| PostgreSQL | 5432 |
| FastAPI    | 8000 |

## Future Improvements

* Alembic database migrations
* Authentication (JWT)
* Pagination and filtering
* Production deployment configuration
* CI/CD pipeline

## Author
Jhoselyn Miluska Pajuelo
Software Engineer focused on building scalable backend systems and developer tools.

