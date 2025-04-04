# Use the official Python 3.8.1 image as the base
FROM python:3.8.1

# Set the working directory inside the container to /app
WORKDIR /app

# Install the netcat
RUN apt-get update && apt-get install -y netcat && apt-get clean

# Copy the dependencies 
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the project file to the container
COPY . .

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Expose the port used by the Django development server
EXPOSE 8020

# Set the entrypoint script to be executed when the container starts
ENTRYPOINT ["./entrypoint.sh"]
