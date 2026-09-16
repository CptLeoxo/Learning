# Server Status Dashboard (Dockerized)

A lightweight Python Flask web dashboard for monitoring server ping latency. This application is fully containerized using a minimal Alpine Linux base image, making it highly portable and easy to deploy across different environments.

## 🛠 Tech Stack

- **Python 3.11** (Alpine base image for minimal footprint)
- **Flask** (Web framework)
- **Docker** (Containerization)

## 🚀 How to Build and Run

### 1. Build the Docker Image

Navigate to the directory containing the `Dockerfile` and run:

```bash
docker build -t ping-dashboard .
```

### 2. Run the Container

Start the container in detached mode and map port `8080` to your localhost:

```bash
docker run -d -p 8080:8080 --name my-dashboard ping-dashboard
```

### 3. Access the Dashboard

Open your web browser and navigate to:
`http://localhost:8080`

## 🔧 Useful Admin Commands

Check the status of the running container:

```bash
docker ps
```

View application logs (useful for debugging ping logic or checking access logs):

```bash
docker logs my-dashboard
```

Stop the container gracefully:

```bash
docker stop my-dashboard
```

Working on it.
