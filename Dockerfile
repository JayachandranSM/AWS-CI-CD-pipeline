# Use the official Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app


COPY . /app

RUN apt update -y && apt install awscli -y

RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Set the entry point for the container
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

