# Use the official Python 3.11.5 image from Docker Hub with Alpine Linux
FROM docker.io/library/python:3.11.5-alpine

# Set environment variables for Python and Django settings module
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=shopping_list.settings

# Create a non-root user named "app" to own and run the application
RUN addgroup app \
    && adduser -s /bin/false -G app -D -H app

# Copy the requirements.txt file to the root directory of the container
COPY requirements.txt /requirements.txt

# Install Python dependencies listed in the requirements.txt, without caching
RUN pip install --no-cache-dir -r /requirements.txt

# Switch to the "app" user, so the application does not run as root
USER app

# Set the working directory inside the container to /opt/app
WORKDIR /opt/app

# Copy the entire project directory into the container
COPY --chown=app:app . .

# Collect static files
RUN python manage.py collectstatic --no-input --clear

# Expose port 8000 to allow external access to the application
EXPOSE 8000

# Start gunicorn to serve the Django application
CMD ["gunicorn", "shopping_list.wsgi:application", "--bind", "0.0.0.0:8000"]
