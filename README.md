# Monitoring Configuration Validator

Student Name: Anwesha Jain  
Registration No: 23FE10CSE00795  
Course: CSE3253 DevOps [PE6]  
Semester: VI (2025-2026)  
Project Type: Puppet & Monitoring  
Difficulty: Intermediate  

---

## Project Overview

Monitoring Configuration Validator is a DevOps tool designed to validate monitoring configurations (Nagios/Prometheus style configs) and detect syntax errors, missing fields, duplicate alerts, and misconfigurations before deployment.

---

## Problem Statement

Incorrect monitoring configurations can cause:
- Missed alerts
- False positives
- System downtime
- Alert fatigue

There is no automated validation system before deploying monitoring configs. This project solves that problem.

---

## Objectives

- Validate monitoring configuration files
- Detect syntax errors and missing parameters
- Identify duplicate alert rules
- Generate validation reports
- Integrate validation into CI/CD pipeline

---

## Key Features

- Config syntax validation
- Alert rule verification
- Duplicate detection
- Error reporting dashboard
- Dockerized deployment
- CI/CD integration
- Monitoring integration

---

## Technology Stack

### Core Technologies
Programming Language: Python  
Framework: Flask  
Database: None  

### DevOps Tools
Version Control: Git  
CI/CD: GitHub Actions  
Containerization: Docker  
Orchestration: Kubernetes  
Configuration Management: Puppet  
Monitoring: Nagios  

---

## Getting Started

### Prerequisites
- Docker Desktop v20+
- Python 3.8+
- Git

### Installation

1. Clone the repository:
   git clone
   https://github.com/yourusername/devopsprojectmonitoringconfigurationvalidator.git
   cd devopsprojectmonitoringconfigurationvalidator
   
2. Run using Docker:
docker-compose up --build

3. Access:
   http://localhost:8080/
   
---

## CI/CD Pipeline

Stages:
1. Linting
2. Build Docker Image
3. Run Unit Tests
4. Security Scan
5. Deploy

---

## Testing

Unit Tests: pytest  
Integration Tests: pytest tests/integration  

---

## Monitoring Setup

Nagios configured for:
- Service health check
- Application uptime
- Custom validation metrics

---

## Security

- Input validation
- Secure configuration loading
- Environment variables
- Docker image scanning

---

## Challenges

1. Parsing complex monitoring configs  
2. Handling multiple configuration formats  
3. Integration with CI/CD  

---

## Learnings

- Monitoring as Code
- CI/CD automation
- Docker containerization
- DevOps best practices

---

## Contact

Student: Anwesha Jain  
GitHub: https://github.com/anwesha067
