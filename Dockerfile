# Use the official Python image as base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR .

# Copy the current directory contents into the container at /app
COPY . .

#install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 5002

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
