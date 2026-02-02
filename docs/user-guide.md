# User Guide  
## Monitoring Configuration Validator

---

## 1. Introduction

This guide explains how to use the Monitoring Configuration Validator to check monitoring configuration files before deployment.

The tool helps prevent monitoring failures caused by incorrect configurations.

---

## 2. Prerequisites

- Python 3.9 or higher
- Git
- Docker Desktop (optional, for container usage)

---

## 3. Running the Validator Locally

### Step 1: Clone the repository

git clone https://github.com/anwesha067/devops-project-monitoring-config-validator.git
cd devops-project-monitoring-config-validator



### Step 2: Create virtual environment
python3 -m venv venv
source venv/bin/activate


### Step 3: Install dependencies
pip install -r requirements.txt

### Step 4: Run validation
python src/validator.py src/sample_configs/valid_prometheus.yml


## 4. Running the Validator Using Docker
Step 1: Build Docker image
docker build -t monitoring-config-validator .

Step 2: Run validator
docker run monitoring-config-validator src/sample_configs/valid_prometheus.yml

## 5. Understanding Output
Valid Configuration
✅ Configuration is valid

Invalid Configuration
❌ Validation Failed
- Job 0 missing 'job_name'

## 6. CI/CD Integration
The validator is integrated with GitHub Actions.
On every push or pull request, configurations are automatically validated.
If validation fails, the pipeline fails.

## 7. Troubleshooting
Ensure correct file paths
Ensure YAML syntax is valid
Check GitHub Actions logs if pipeline fails


## 8. Conclusion
This tool enables DevOps teams to validate monitoring configurations automatically, improving reliability and observability.
