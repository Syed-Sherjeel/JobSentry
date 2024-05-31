# JobSentry

JobSentry is a comprehensive job posting and management platform built using FastAPI for the backend API and Jinja templates for serving web pages. Leveraging the power of FastAPI, SQLAlchemy ORM, JWT authentication, and PostgreSQL database, this project provides a robust and scalable solution for job seekers and employers alike. With support for unit testing using Pytest, load testing with Locust, and seamless deployment using Docker, FastAPI-JobHub ensures reliability, security, and performance at every step.
![techstack](https://github.com/Syed-Sherjeel/JobSentry/assets/56888046/4669e5a7-c01e-4ba4-b1f9-289fc396dec5)

## Features:

- **Pydantic DataValidation**: Utilizes pydantic for fast, efficient and secure data validation to prevent any malicious actor to sabotage production.
- **FastAPI Backend**: Utilizes FastAPI, a modern web framework for building APIs with Python, ensuring high performance and asynchronous capabilities.
- **Jinja Templates**: Employs Jinja templates for rendering dynamic web pages, providing a user-friendly interface for job posting and viewing.
- **JWT Authentication**: Implements JWT (JSON Web Tokens) for secure authentication, allowing users to authenticate and access protected endpoints. Ensure OSWAP compliance.
- **SQLAlchemy ORM**: Integrates SQLAlchemy ORM for database operations, enabling seamless interaction with the PostgreSQL database.
- **PostgreSQL Database**: Uses PostgreSQL as the primary database, offering reliability and scalability while maintaining flexibility to migrate to other SQL databases if needed.
- **Pytest for Unit Testing**: Includes Pytest for writing and executing unit tests, ensuring code quality and reliability throughout the development process.
- **Locust for Load Testing**: Integrates Locust for load testing, enabling simulation of thousands of concurrent users to evaluate system performance and scalability.
- **Docker Deployment**: Facilitates deployment using Docker, allowing for easy setup and scalability of the web application.
- **Graceful Shutdown**: Implements checks for database connection before starting and ensures graceful shutdown procedures for seamless operation.
- **Exception Handling**: Ensures proper exception handling and appropriate error message 

### Setup Instructions:

1. Setup postgresql: [Follow these instructions and create a database](https://medium.com/@nathaliafriederichs/setting-up-a-postgresql-environment-in-docker-a-step-by-step-guide-55cbcb1061ba)
1. Clone the repository: `git clone https://github.com/your/repository.git`
2. Navigate to the project directory: `cd JobSentry`
3. Install virtualenv: `sudo apt install virtualenv` 
4. Setup virtualenvironmentL  `python3 -m virtualenv env`
5. Install dependencies: `pip install -r requirements.txt`
6. Start the FastAPI server: `POSTGRES_USER=postgres POSTGRES_PASSWORD=1234 POSTGRES_HOST=localhost POSTGRES_PORT=5431 POSTGRES_DB=jobapp  SECRET_KEY=asdfasf12  uvicorn main:app
 uvicorn main:app --reload`

### Testing:

- Run unit tests using Pytest: `pytest`
- Conduct load testing with Locust: WIP `locust -f test/test_load.py`

### Deployment:

- Build Docker image: `docker build -t jobsentry .`
- Run Docker container: `docker run -d -p 8000:8000 fastapi-jobhub`


### License:

This project is licensed under the MIT License 
### Disclaimer:

FastAPI-JobHub is a project for educational and demonstration purposes. It may not be suitable for production environments without further customization and security considerations. Use it at your own risk.

**Happy Job Posting with JobSentry**
