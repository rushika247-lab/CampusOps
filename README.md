# CampusOps

CampusOps is a **College DevOps Automation Platform** created to automate the process of building, testing, and deploying a college-based application using DevOps practices.

This project was built as part of a **CI/CD macro project** to understand how real companies automate software delivery using tools like GitHub Actions, Docker, versioning, and deployment pipelines.

The idea behind this project is simple: instead of manually testing and deploying code every time, the system should automatically verify code, build Docker images, store versions, and make deployment easier.

---

## Problem Statement

In many colleges, portals such as assignment systems or placement systems are updated manually. This can create problems like:

* Manual errors during deployment
* No proper version tracking
* Difficulty in rollback if something breaks
* Time-consuming testing process

CampusOps helps solve this by introducing **CI/CD automation** into a college codebase.

---

## Features

### Student Side

* Assignment submission
* Placement tracking
* Resume upload
* Deadline monitoring

### Faculty Side

* Review student submissions
* Provide feedback

### Admin/HOD Side

* Monitor activities
* Track reports

### DevOps Features

* GitHub Actions CI/CD Pipeline
* Docker containerization
* Docker Hub integration
* Automatic Docker image build
* Semantic versioning
* Commit SHA tagging
* GitHub build artifacts

---

## Tech Stack Used

* Python
* Flask
* Git & GitHub
* GitHub Actions
* Docker
* Docker Hub

Planned integrations:

* SonarQube
* Nexus
* Kubernetes
* Prometheus & Grafana

---

## How the Project Works

Whenever code is pushed to GitHub:

```text
Code Push
   ↓
GitHub Actions Trigger
   ↓
Install Dependencies
   ↓
Verify Flask App
   ↓
Build Docker Image
   ↓
Push Image to Docker Hub
   ↓
Generate Build Artifact
   ↓
Pipeline Success
```

This reduces manual effort and helps maintain proper software quality.

---

## Project Structure

```text
CampusOps/
│── .github/
│   └── workflows/
│       └── ci.yml
│
│── templates/
│   └── index.html
│
│── app.py
│── Dockerfile
│── requirements.txt
│── VERSION
│── CHANGELOG.md
│── README.md
```

---

## How to Run the Project

### Clone the Repository

```bash
git clone https://github.com/rushika247-lab/CampusOps.git
cd CampusOps
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Flask App

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## Run Using Docker

Build Docker image:

```bash
docker build -t campusops .
```

Run container:

```bash
docker run -p 5000:5000 campusops
```

Open:

```text
http://localhost:5000
```

---

## Versioning

This project follows **semantic versioning**.

Example:

```text
v1.0.0 → Initial version
v1.1.0 → Added new features
v2.0.0 → Major updates
```

Docker images are also tagged using:

* Latest version
* Commit SHA
* Semantic version

---

## Build Artifacts

GitHub Actions automatically generates a build artifact after every successful workflow.

Artifact name:

```text
campusops-build
```

This can be downloaded from the **Actions tab** in GitHub.

---

## Future Improvements

* SonarQube for code quality
* Nexus for artifact storage
* Kubernetes deployment
* Monitoring using Prometheus & Grafana

---

## Author

**Rushika Gaikwad**

CI/CD Pipeline for College Codebase
