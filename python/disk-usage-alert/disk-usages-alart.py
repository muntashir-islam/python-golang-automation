import shutil

THRESHOLD = 80  # alert if > 80%


def check_disk_usage():
    total, used, free = shutil.disk_usage("/")
    percent_used = (used / total) * 100

    print(f"Disk Usage: {percent_used:.2f}%")

    if percent_used > THRESHOLD:
        print("⚠️ ALERT: Disk usage is above 80%!")
    else:
        print("Disk usage is normal.")


if __name__ == "__main__":
    check_disk_usage()