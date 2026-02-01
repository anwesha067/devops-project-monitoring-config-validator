# Monitoring Configuration Validator

**Student Name:** Anwesha Jain  
**Course:** DevOps  
**Project Type:** Monitoring & CI/CD Automation  
**Difficulty Level:** Intermediate  

---

##  Project Overview

Modern monitoring systems such as Prometheus rely on configuration files written in YAML.  
Even small mistakes in these configuration files can lead to monitoring failures, missed alerts, or system downtime.

This project provides an automated **Monitoring Configuration Validator** that validates monitoring configuration files before they are deployed, ensuring reliability and correctness through CI/CD automation.

---

## Objectives

- Validate monitoring configuration files automatically
- Detect syntax and logical errors in YAML-based configs
- Prevent faulty monitoring configurations from being deployed
- Integrate validation into a CI/CD pipeline
- Containerize the solution using Docker

---

##  Key Features

- YAML configuration validation
- Prometheus monitoring config checks
- Command-line interface (CLI) tool
- Automated CI/CD validation using GitHub Actions
- Dockerized application for portability
- Clear error reporting for invalid configurations

---

##  Technology Stack

### Core Technologies
- **Programming Language:** Python 3
- **Configuration Format:** YAML

### DevOps Tools
- **Version Control:** Git & GitHub
- **CI/CD:** GitHub Actions
- **Containerization:** Docker

---

## Project Structure

devops-project-monitoring-config-validator/
│
├── README.md
├── requirements.txt
├── Dockerfile
│
├── src/
│ ├── validator.py
│ └── sample_configs/
│ ├── valid_prometheus.yml
│ └── invalid_prometheus.yml
│
├── .github/
│ └── workflows/
│ └── ci.yml
│
└── deliverables/

---

##  Getting Started

### Prerequisites
- Python 3.9+
- Git
- Docker Desktop (for container execution)

---

###  Run Locally (Without Docker)

1. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
    pip install -r requirements.txt

3. Run validator:
    python src/validator.py src/sample_configs/valid_prometheus.yml


Run Using Docker
1. Build Docker image:
docker build -t monitoring-config-validator .

2. Run validator:
docker run monitoring-config-validator src/sample_configs/valid_prometheus.yml


CI/CD Pipeline
The project uses GitHub Actions to automatically validate monitoring configurations on every push and pull request.
Pipeline Steps:
Checkout repository
Setup Python environment
Install dependencies
Run configuration validator
If the configuration is invalid, the pipeline fails automatically.

Sample Output

Valid Configuration
✅ Configuration is valid

Invalid Configuration
❌ Validation Failed
- Job 0 missing 'job_name'

Use Case
* This tool can be used by DevOps teams to:
* Validate monitoring configurations before deployment
* Prevent silent monitoring failures
* Enforce configuration standards through CI/CD pipelines


Learning Outcomes
* Practical understanding of CI/CD pipelines
* Hands-on experience with Docker
* YAML configuration validation
* GitHub Actions automation
* DevOps best practices

Conclusion
The Monitoring Configuration Validator improves reliability in monitoring systems by detecting configuration issues early in the development lifecycle.
By integrating validation into CI/CD and containerizing the application, the project demonstrates real-world DevOps practices.


💾 **Save the file**.

---

## 🔹 STEP 3 — Commit README

### 📍 WHERE?
➡️ **Terminal**

```bash
git add README.md
git commit -m "Add project README documentation"
git push
