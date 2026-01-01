import requests
import time

url = "https://example.com/api"
max_retries = 3
delay = 2

for i in range(max_retries):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            print("Success!")
            break
        else:
            print(f"Failed: {r.status_code}, retrying...")
            time.sleep(delay)
    except Exception as e:
        print(f"Error: {e}, retrying...")
        time.sleep(delay)