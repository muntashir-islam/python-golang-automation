import os
import json
import re


def detect_failures(log_dir, output_json="failures_report.json"):
    failure_records = []

    # Regex to extract date from filenames like backup_20250103.log
    date_pattern = re.compile(r"backup_(\d{8})\.log")

    for filename in os.listdir(log_dir):
        if not filename.endswith(".log"):
            continue

        match = date_pattern.match(filename)
        if not match:
            continue  # skip files that don't follow naming pattern

        log_date = match.group(1)
        file_path = os.path.join(log_dir, filename)

        try:
            with open(file_path, "r") as f:
                content = f.read()

                if "FAIL" in content or "Exception" in content:
                    print(f"[FAIL] {filename} contains errors.")
                    failure_records.append({"date": log_date, "file": filename})
                else:
                    print(f"[OK] {filename} clean.")

        except Exception as e:
            print(f"[ERROR] Could not read {filename}: {e}")

    # Save JSON report
    report = {"failed_logs": failure_records}

    with open(output_json, "w") as json_out:
        json.dump(report, json_out, indent=4)

    print(f"\nJSON report written to {output_json}")
    return report


# Example usage:
if __name__ == "__main__":
    LOG_DIR = "/path/to/logs"
    detect_failures(LOG_DIR)
