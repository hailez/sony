# Use the official Python image from Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy the Flask app code into the container
COPY route.py .

# Expose the port that Flask will run on
EXPOSE 5000

# Define the command to run the app
CMD ["python3", "route.py"]

