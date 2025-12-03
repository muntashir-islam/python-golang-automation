import psutil

THRESHOLD = 80


def check_all_disks():
    partitions = psutil.disk_partitions()

    for p in partitions:
        try:
            usage = psutil.disk_usage(p.mountpoint)
            percent = usage.percent
            print(f"{p.mountpoint} → {percent}% used")

            if percent > THRESHOLD:
                print(f"⚠️ ALERT: {p.mountpoint} above {THRESHOLD}%")

        except PermissionError:
            pass  # skip system-protected mounts


if __name__ == "__main__":
    check_all_disks()
