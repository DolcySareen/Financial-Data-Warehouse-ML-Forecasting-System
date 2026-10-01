#!/usr/bin/env sh

# Run database migrations
#flask db upgrade

# Start the Flask application
#flask run --host=0.0.0.0 &

# Start the Flask application
python app.py 

# Start the Celery worker
#celery -A app.controllers.tasks_controller.celery worker --loglevel=info &

# Start the Celery beat scheduler
#celery -A app.controllers.tasks_controller.celery beat --loglevel=info