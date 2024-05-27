# Watchmate API (IMDB Clone)

The Watchmate API mimics IMDB, providing endpoints for managing movies, streaming platforms, and reviews. This API
allows users to discover, review, and track movies and platforms.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
    - [Movies](#movies)
    - [Streaming Platforms](#streaming-platforms)
    - [Reviews](#reviews)
    - [Authentication](#authentication)

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

- `GET /watchlist/products/`: Retrieve a list of movies
- `GET /watchlist/products/{id}/`: Retrieve details of a specific movie
- `POST /watchlist/products/`: Create a new movie
- `PUT /watchlist/products/{id}/`: Update an existing movie
- `PATCH /watchlist/products/{id}/`: Partially update an existing movie
- `DELETE /watchlist/products/{id}/`: Delete a movie

### Streaming Platforms

- `GET /watchlist/platforms/`: Retrieve a list of streaming platforms
- `GET /watchlist/platforms/{id}/`: Retrieve details of a specific streaming platform
- `POST /watchlist/platforms/`: Create a new streaming platform
- `PUT /watchlist/platforms/{id}/`: Update an existing streaming platform
- `PATCH /watchlist/platforms/{id}/`: Partially update an existing streaming platform
- `DELETE /watchlist/platforms/{id}/`: Delete a streaming platform

### Reviews

- `GET /watchlist/reviews/`: Retrieve a list of reviews
- `GET /watchlist/reviews/{id}/`: Retrieve details of a specific review
- `GET /watchlist/products/{product_id}/reviews/`: Retrieve a list of movie specific reviews
- `POST /watchlist/products/{product_id}/create-review/`: Create a new review
- `PUT /watchlist/reviews/{id}/`: Update an existing review
- `PATCH /watchlist/reviews/{id}/`: Partially update an existing review
- `DELETE /watchlist/reviews/{id}/`: Delete a review

## Authentication

The Watchmate API uses token-based authentication. You need to include your token in the `Authorization` header of your
requests.

Example:

```
Authorization: Token your_token_here
```

To manage authentication, you can use the following endpoints:

- `POST /accounts/register/`: Register a new user by providing valid credentials (username, password, email).
- `POST /accounts/login/`: Obtain a token by providing valid credentials (username and password).
- `POST /accounts/logout/`: Logout by invalidating the current token.

