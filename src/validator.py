import yaml
import sys

def validate_prometheus_config(file_path):
    errors = []

    try:
        with open(file_path, "r") as f:
            config = yaml.safe_load(f)
    except Exception as e:
        return [f"YAML Parsing Error: {e}"]

    if "scrape_configs" not in config:
        errors.append("Missing 'scrape_configs' section")
    else:
        for index, job in enumerate(config["scrape_configs"]):
            if "job_name" not in job:
                errors.append(f"Job {index} missing 'job_name'")
            if "static_configs" not in job:
                errors.append(f"Job {index} missing 'static_configs'")

    return errors


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validator.py <config-file>")
        sys.exit(1)

    config_file = sys.argv[1]
    errors = validate_prometheus_config(config_file)

    if errors:
        print("❌ Validation Failed")
        for err in errors:
            print("-", err)
        sys.exit(1)
    else:
        print("✅ Configuration is valid")
