# Use an official Python image as the base
FROM python:3.10-slim AS base

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY . .

# Update pip & install pip-tools
RUN pip install --upgrade --no-cache-dir \
    pip \
    pip-tools

# Compile the requirements file
RUN pip-compile requirements.in   

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Use the entrypoint script to start the services
ENTRYPOINT ["/app/entrypoint.sh"]

# # Default command to build the data warehouse and start the Flask app
# CMD ["python", "app.py"]

# # Run the Flask app and Celery worker and beat
# CMD ["sh", "-c", "flask run & celery -A app.controllers.tasks.celery worker --loglevel=info & celery -A app.controllers.tasks.celery beat --loglevel=info"]