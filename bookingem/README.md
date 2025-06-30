# Bookingem

Bookingem is a Django-based application designed to manage a collection of books, authors, and reviews. It serves as a practical exercise for understanding and utilizing Django's Object-Relational Mapping (ORM) capabilities.

The project includes models for `Author`, `Book`, and `Review`, and a services layer (`books/services.py`) that contains a comprehensive set of ORM queries for various data retrieval and manipulation tasks.

## Prerequisites

- Python 3.10+
- Poetry

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/uluk001/assgmnts.git
    cd assgmnts/bookingem
    ```

2.  **Install dependencies using Poetry:**

    ```bash
    poetry install
    ```

3.  **Set up the database:**

    The project is configured to use PostgreSQL. Make sure you have a running PostgreSQL instance and create a database for this project.

    Then, create a `.env` file in the root directory and add your database credentials:

    ```env
    DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
    ```

4.  **Apply database migrations:**

    ```bash
    poetry run python manage.py migrate
    ```

## Populating the Database

The project includes a command to populate the database with a large set of mock data using the `Faker` library.

To generate mock data for authors, books, and reviews, run the following command:

```bash
poetry run python manage.py create_mock_data
```

This will create 10,000 authors, 50,000 books, and 100,000 reviews.

## ORM Queries

The `books/services.py` file contains a collection of functions, each wrapping a specific Django ORM query. These functions are designed to demonstrate various querying techniques, from simple filters to complex annotations and aggregations.

Each function is clearly named and includes a docstring (in Russian) that describes the query's purpose, making it an excellent resource for learning and reference.

## Running the Development Server

To run the Django development server, use the following command:

```bash
poetry run python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.
