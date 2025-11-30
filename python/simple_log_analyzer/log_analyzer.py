import os

log_file = "application.log"
error_file = "errors.log"
summary_file = "summary.log"

info_count = 0
warning_count = 0
error_count = 0
error_lines = []
latest_error_time = None

try:
    # Read log file
    with open(log_file, "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()

        # Count log levels
        if "INFO" in line:
            info_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "ERROR" in line:
            error_count += 1
            error_lines.append(line)

            # Extract timestamp (first two fields)
            timestamp = " ".join(line.split(" ")[0:2])
            latest_error_time = timestamp

    # Write all ERROR lines to errors.log
    with open(error_file, "w") as f:
        f.write("\n".join(error_lines) + "\n")

    # Print summary
    print(f"INFO: {info_count}")
    print(f"WARNING: {warning_count}")
    print(f"ERROR: {error_count}")

    if latest_error_time:
        print(f"Latest error at: {latest_error_time}")

    # Write summary to summary.log
    with open(summary_file, "w") as f:
        f.write(f"INFO: {info_count}\n")
        f.write(f"WARNING: {warning_count}\n")
        f.write(f"ERROR: {error_count}\n")
        if latest_error_time:
            f.write(f"Latest error at: {latest_error_time}\n")

except FileNotFoundError:
    print(f"❌ Error: '{log_file}' not found. Please create the file first.")
