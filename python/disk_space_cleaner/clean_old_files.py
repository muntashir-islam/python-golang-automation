import os
import time
from datetime import datetime, timedelta


def clean_old_files(target_dir, days_old, log_file='cleanup.log'):
    now = time.time()
    cutoff = now - (days_old * 86400)

    deleted_files = []

    with open(log_file, 'a') as log:
        log.write(f"\n--- Cleanup Started at {datetime.now()} ---\n")
        log.write(f"Target Directory: {target_dir}\n")
        log.write(f"Deleting files older than {days_old} days\n\n")

        for root, dirs, files in os.walk(target_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    file_mtime = os.path.getmtime(file_path)
                    if file_mtime < cutoff:
                        file_age_days = (now - file_mtime) / 86400
                        os.remove(file_path)
                        msg = f"Deleted: {file_path} (Age: {file_age_days:.2f} days)"
                        print(msg)
                        log.write(msg + "\n")
                        deleted_files.append(file_path)
                except Exception as e:
                    err = f"Error deleting {file_path}: {e}"
                    print(err)
                    log.write(err + "\n")
        log.write(f"--- Cleanup Completed at {datetime.now()} ---\n")
    return deleted_files


if __name__ == "__main__":
    TARGET_DIR = "/path/to/folder"
    DAYS_OLD = 7  # delete older than 7 days

    deleted = clean_old_files(TARGET_DIR, DAYS_OLD)

    print("\nSummary:")
    print(f"Deleted {len(deleted)} files.")
