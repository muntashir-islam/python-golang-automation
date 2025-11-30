from collections import defaultdict, Counter

log_file = "access.log"
error_file = "server_errors.log"

url_count = defaultdict(int)
status_count = {"2xx": 0, "4xx": 0, "5xx": 0}
error_lines = []

try:
    with open(log_file, "r") as f:
        lines = f.readlines()

    print(f"Total Requests: {len(lines)}\n")

    for line in lines:
        parts = line.split()

        # Extract info
        status_code = int(parts[-2])
        url = parts[6]  # URL is always 7th part in Nginx log format

        # Count URL hits
        url_count[url] += 1

        # Count status classes
        if 200 <= status_code < 300:
            status_count["2xx"] += 1
        elif 400 <= status_code < 500:
            status_count["4xx"] += 1
        elif 500 <= status_code < 600:
            status_count["5xx"] += 1

        # Collect server error lines
        if status_code == 500:
            error_lines.append(line.strip())

    # Print URL hits
    print("URL Hits:")
    for url, count in url_count.items():
        print(f"{url} → {count} hits")
    print()

    # Print status summary
    print("Status Code Summary:")
    for code, count in status_count.items():
        print(f"{code}: {count}")
    print()

    # Write server errors to file
    with open(error_file, "w") as f:
        f.write("\n".join(error_lines) + "\n")

    # Bonus: Top 3 URLs
    top3 = Counter(url_count).most_common(3)
    print("Top 3 Requested URLs:")
    for url, count in top3:
        print(f"{url} → {count} hits")

except FileNotFoundError:
    print(f"❌ Error: {log_file} not found.")
