# AlgoTrading Flask Application

This is a Flask application for Algorithmic Trading and Short-term Forecast for Financial Time Series with Machine Learning Models.

## Features

- User Registration and Login
- Dashboard for API Key Configuration
- Flash Messages for User Feedback
- Integration with PostgreSQL Database
- pgAdmin for Database Management

## Prerequisites

- Python 3.10
- PostgreSQL
- Docker (optional, for containerization)

## Installation

1. **Clone the repository:**

    ```sh
    git clone ...
    cd ...
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add the following:

    ```plaintext
    SECRET_KEY=your_secret_key
    SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://username:password@localhost/dbname
    ```

5. **Initialize the database:**

    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

6. **Run the application:**

    ```sh
    flask run
    ```

## Docker (optional)

To run the application using Docker, follow these steps:

1. **Build the Docker image:**

    ```sh
    docker build -t altrasetl .
    ```

2. **Run the Docker container:**

    ```sh
    docker run -d -p 5000:5000 --name altrasetl-container altrasetl-app
    ```

## Usage

- **Register a new user:** Navigate to `/register` to create a new account.
- **Login:** Navigate to `/login` to log in to your account.
- **Dashboard:** Navigate to `/dashboard` to configure your API key.
- **Logout:** Click the logout button to log out of your account.

## Project Structure
````
┌/
├── app/
│ ├── init.py
│ ├── models/
│ │ ├──__init__.py 
│ │ └── user.py
│ ├── static/
│ │ ├── background.png
│ │ └── style.css
│ ├── templates/
│ │ ├── dashboard.html 
│ │ ├── login.html
│ │ ├── portal.html
│ │ ├── register.html
│ │ └── settings.html
│ ├── views/
│ │ ├──__init__.py
│ │ ├── routes_controller.py
│ │ └── forms_controller.py
│ ├── tests/
│ │ ├──__init__.py
│ │ └── test_app.py
│ └── app.py
├── .env
├── .gitignore
├── requirements.txt
├── requirements.in
└── README.md


