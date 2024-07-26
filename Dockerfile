# Use the official Python image as a base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
COPY src/requirements.txt /app/requirements.txt


#RUN pip install --upgrade pip


RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code into the container
COPY ./src /app

# Expose port 80 to the outside world

# Command to run the FastAPI application
CMD ["uvicorn", "app.main:app","--proxy-headers", "--host", "0.0.0.0", "--port", "8002"]



