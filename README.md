# Cloud Infrastructure Deployment & Monitoring Capstone

## Project Overview

This project demonstrates a containerized Python Flask application deployed on Render, with automated CI checks using GitHub Actions and uptime monitoring through Grafana Cloud Synthetic Monitoring.

## Architecture

1. Developer pushes code to GitHub.
2. GitHub Actions runs automated tests and code-quality checks.
3. Docker packages the Flask application into a container.
4. Render builds and deploys the containerized application.
5. Grafana Cloud Synthetic Monitoring checks the application's health endpoint.
6. A Grafana alert rule monitors the health-check result.

## Technologies Used

* Python
* Flask
* Docker
* GitHub Actions
* Render
* Grafana Cloud Synthetic Monitoring
* Prometheus-compatible probe metrics

## Live Application

* Application: https://automated-cicd-python.onrender.com
* Health endpoint: https://automated-cicd-python.onrender.com/health

The health endpoint returns HTTP 200 with the JSON response:

```json
{
  "status": "healthy"
}
```

## Environment Configuration

The application reads its port from the `PORT` environment variable and defaults to `10000` when the variable is not set. The application listens on `0.0.0.0` so it can accept connections inside its container.

## Docker Configuration

The Dockerfile uses the lightweight Python 3.13 slim image, installs dependencies from `requirements.txt`, copies the application code, exposes port 10000, and starts the Flask application.

## Continuous Integration

GitHub Actions runs automated tests and code-quality checks. The application tests validate the home endpoint and health endpoint.

## Monitoring and Alerting

Grafana Cloud Synthetic Monitoring checks:

`https://automated-cicd-python.onrender.com/health`

The monitoring check uses an HTTP GET request and tracks probe success, HTTP status code, response duration, and TLS certificate expiry.

A Grafana alert rule named `au
