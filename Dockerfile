# Use the official Python 3.10 slim image as the base
FROM python:3.10-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Install the netcat
RUN apt-get update && apt-get install -y netcat && apt-get clean

# Copy the dependencies 
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files to the container
COPY . /app/

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Expose the port used by the Django development server
EXPOSE 8020

# Set the entrypoint script to be executed when the container starts
ENTRYPOINT ["./entrypoint.sh"]
