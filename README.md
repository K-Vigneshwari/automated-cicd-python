[![Python CI Pipeline](https://github.com/K-Vigneshwari/automated-cicd-python/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/K-Vigneshwari/automated-cicd-python/actions/workflows/ci.yml)
# Automated CI/CD Pipeline with GitHub Actions

## Project Overview
This project demonstrates an automated Continuous Integration and Continuous Deployment (CI/CD) pipeline using GitHub Actions, Python, Pytest, Docker, and GitHub Container Registry (GHCR).

Whenever code is pushed to the GitHub repository, the workflow automatically runs tests, builds a Docker image, and publishes the image to GHCR.

## Technologies Used
- Python 3.13
- Pytest
- Git and GitHub
- GitHub Actions
- Docker
- GitHub Container Registry (GHCR)

## Project Structure
```text
cicd-python-project/
├── app.py
├── test_app.py
├── Dockerfile
├── .gitignore
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
```

## Application
The Python application displays:

`Hello! Welcome to my CI/CD project.`

## Run Locally
Run the application:

```bash
python app.py
```

Run automated tests:

```bash
python -m pytest
```

## Build and Run with Docker
Build the Docker image:

```bash
docker build -t cicd-python-project .
```

Run the container:

```bash
docker run --rm cicd-python-project
```

## Published Docker Image
The Docker image is published to GitHub Container Registry.

Pull the image:

```bash
docker pull ghcr.io/k-vigneshwari/cicd-python-project:latest
```

Run the published image:

```bash
docker run --rm ghcr.io/k-vigneshwari/cicd-python-project:latest
```

## CI/CD Workflow
1. Checkout the repository.
2. Set up Python.
3. Install Pytest.
4. Run automated tests.
5. Build the Docker image.
6. Publish the image to GHCR.

## Project Outcome
The project successfully automates Python testing and Docker image publishing using GitHub Actions.

## Repository
https://github.com/K-Vigneshwari/automated-cicd-python

## Docker Package
https://github.com/users/K-Vigneshwari/packages/container/cicd-python-project
