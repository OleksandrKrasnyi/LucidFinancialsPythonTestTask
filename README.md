# LucidFinancialsPythonTestTask

This is a FastAPI-based web application built as a test task. It implements a simple social media-like API with user authentication and post management, following the MVC pattern.

## Features
- **Signup**: Register a new user with email and password, returns a JWT token.
- **Login**: Authenticate a user and return a token.
- **AddPost**: Create a post (max 1MB) with token authentication.
- **GetPosts**: Retrieve all posts for the authenticated user (cached for 5 minutes).
- **DeletePost**: Delete a specific post by ID.

## Tech Stack
- **Python 3.8+**
- **FastAPI**: Web framework
- **SQLAlchemy**: ORM for MySQL database
- **Pydantic**: Data validation (V2 compatible)
- **PyMySQL**: MySQL driver
- **PyJWT**: JWT token handling
- **Cryptography**: Secure MySQL authentication
- **Uvicorn**: ASGI server

## Project Structure
project/
├── main.py          # Entry point and app initialization
├── routes.py       # API endpoints
├── schemas.py      # Pydantic models for validation
├── models.py       # SQLAlchemy database models
├── dependencies.py # Dependency injection (DB, auth)
├── config.py       # Configuration settings
└── requirements.txt # Project dependencies

## Setup
1. **Clone the repository**:
   git clone https://github.com/OleksandrKrasnyi/LucidFinancialsPythonTestTask.git
   cd LucidFinancialsPythonTestTask/project

2. **Install dependencies**:
   pip install -r requirements.txt

3. **Configure MySQL**:
   • Create a database: CREATE DATABASE myapp;
   • Update config.py with your MySQL credentials:
      DATABASE_URL = "mysql+pymysql://your_username:your_password@localhost/myapp"

4. **Run the application**:
   python -m project.main
