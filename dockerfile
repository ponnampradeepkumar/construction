# Use a slim version of Python 3.12 as the base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files into the container
COPY . /app/

# Set the environment variable for Django settings module
ENV DJANGO_SETTINGS_MODULE=construction.settings

# Expose port 8000 for the app
EXPOSE 8000

# Start the Django application using Gunicorn
CMD ["gunicorn", "construction.wsgi:application", "--bind", "0.0.0.0:8000"]

