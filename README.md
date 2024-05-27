# Watchmate API (IMDB Clone)

API mimicking IMDB, including endpoints for movies, streaming platforms, and reviews.

## Installation

### Prerequisites

- Python 3.6+
- Django 3.0+
- Django REST Framework

### Steps

1. Clone the repository:

```bash
git clone https://github.com/manlikeclaro/django-drf-project
cd watchmate
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

## Usage

To access the API documentation, navigate to:

- **Swagger UI**: `http://localhost:8000/watchlist/api/schema/swagger-ui/`
- **Redoc**: `http://localhost:8000/watchlist/api/schema/redoc/`

## API Endpoints

### Movies

- `GET /products/`: Retrieve a list of movies
- `GET /products/{id}/`: Retrieve details of a specific movie
- `POST /products/`: Create a new movie
- `PUT /products/{id}/`: Update an existing movie
- `PATCH /products/{id}/`: Partially update an existing movie
- `DELETE /products/{id}/`: Delete a movie

### Streaming Platforms

- `GET /platforms/`: Retrieve a list of streaming platforms
- `GET /platforms/{id}/`: Retrieve details of a specific streaming platform
- `POST /platforms/`: Create a new streaming platform
- `PUT /platforms/{id}/`: Update an existing streaming platform
- `PATCH /platforms/{id}/`: Partially update an existing streaming platform
- `DELETE /platforms/{id}/`: Delete a streaming platform

### Reviews

- `GET /reviews/`: Retrieve a list of reviews
- `GET /reviews/{id}/`: Retrieve details of a specific review
- `GET /products/{product_id}/reviews/`: Retrieve a list of movie specific reviews
- `POST /products/{product_id}/create-review/`: Create a new review
- `PUT /reviews/{id}/`: Update an existing review
- `PATCH /reviews/{id}/`: Partially update an existing review
- `DELETE /reviews/{id}/`: Delete a review

## Authentication

The Watchmate API uses token-based authentication. You need to include your token in the `Authorization` header of your
requests.

Example:

```
Authorization: Token your_token_here
```

To obtain a token, you can use the following endpoint:

- `POST /accounts/login/`: Obtain a token by providing valid credentials (username and password).

