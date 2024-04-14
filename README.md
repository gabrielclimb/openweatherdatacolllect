# Open Weather Data Collect

## Project Overview
This project is designed to collect weather data using the OpenWeatherMap API. It organizes the data for further analysis and can be deployed using Docker.

## Setup Instructions

### Environment Setup
1. Clone the repository.
2. Ensure you have Python and Docker installed on your machine.

### Dependency Installation
Run the following command to install required Python packages:
```bash
pip-install
```

### Setting up Pre-commit Hooks
To install pre-commit hooks into your git hooks, run the following command:
```bash
pre-commit install
```

## Running the Application

### Using Docker
To build and run the application using Docker, execute:
```bash
docker build -t openweatherdata .
docker run -d --name weather_app openweatherdata
```

### Using Docker Compose
To simplify the Docker management process, use Docker Compose:
```bash
docker-compose
```

## Running Tests
To run tests, you can use the included Makefile:
```bash
make test
```

## Additional Configuration
- **Environment Variables:** Configure necessary API keys and settings in the `.env` file.
