# Flask App + with Docker Compose

This repository contains a simple Flask app that can be run using Docker Compose. Follow the instructions below to run
the Flask app on your local machine.

## Requirements

- Flask
- Docker
- Postman or any other API testing tool

## Running the App in Flask

1. Clone the repository to your local machine.

2. Open a terminal and navigate to the project directory.

3. Run the following command to build and run the Docker containers:

   ```bash
   python app.py

## Running the App in Docker

1. Clone the repository to your local machine.

2. Open a terminal and navigate to the project directory.

3. Run the following command to build and run the Docker containers:

   ```bash
   docker-compose up --build

### Once the containers are up and running, the Flask app will be accessible at http://localhost:5002/predict. or http://127.0.0.1:5002/predict by postman

## Testing the App

1. Open Postman or any other API testing tool.

1. Create a POST request to http://localhost:5002/predict.

3. Set the request header Content-Type to application/json.

4. Set the request body to a JSON object with the required data. For example:
   `  
   {
   "month": 1
   }`

5. Send the request and observe the response from the Flask app.

## Stopping the App

To stop the containers, press `Ctrl + C` in the terminal where the containers are running. Then, run the following
command:

   ```bash
docker-compose down
