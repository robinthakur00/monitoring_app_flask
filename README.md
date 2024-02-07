# Monitoring App Deployment on AWS EKS

This project aims to deploy a monitoring application on Amazon EKS (Elastic Kubernetes Service) utilizing Docker for containerization and Amazon ECR (Elastic Container Registry) for efficient image management. The deployment process is orchestrated using Python Boto3 for dynamically creating the ECR repository and the Kubernetes Python Client for deploying the application on Amazon EKS.

## Features

- Containerised application using Docker ensures portability and consistency across different environments.
- Dynamically created Amazon ECR repository using Python Boto3 allows for efficient image management and version control.
- Deployment of the application on Amazon EKS using the Kubernetes Python Client provides scalability and reliability.

## Technologies Used

- Flask: A lightweight WSGI web application framework in Python.
- Docker: A platform for developing, shipping, and running applications in containers.
- Amazon EKS: A fully managed Kubernetes service provided by AWS for deploying, managing, and scaling containerized applications.
- Amazon ECR: A fully managed Docker container registry provided by AWS for storing, managing, and deploying Docker container images.
- Python Boto3: The AWS SDK for Python, used for interacting with AWS services.


1. **Containerisation with Docker**: Ensure Docker is installed on your local machine. Build the Docker image for the monitoring application using the provided Dockerfile.

```bash
docker build -t monitoring-app . 
```

2. **Dynamically Create Amazon ECR Repository**: Use the provided Python script with Boto3 to dynamically create the Amazon ECR repository and push the Docker image to it.

```bash
python ecr.py
```

3. **Deploy Application on Amazon EKS**: Use the Kubernetes Python Client to deploy the application on Amazon EKS.

```bash
python eks.py
```

