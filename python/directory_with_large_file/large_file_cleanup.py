import os
import sys

TARGET_DIR = sys.argv[1]
FILE_SIZE_MB = int(sys.argv[2])

def large_file_cleanup(target_dir, file_size_mb):
    max_size_bytes = file_size_mb * 1024 * 1024

    for root, _, files in os.walk(target_dir):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                size = os.path.getsize(file_path)
                if size > max_size_bytes:
                    print(f"Deleting: {file_path} ({size / (1024*1024):.2f} MB)")
                    os.remove(file_path)
            except Exception as e:
                print(f"Error with {file_path}: {e}")

if __name__ == "__main__":
    large_file_cleanup(TARGET_DIR, FILE_SIZE_MB)