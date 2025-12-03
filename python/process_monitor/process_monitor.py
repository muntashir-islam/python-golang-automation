import psutil


def find_process_by_name(process_name):
    process_list = []
    for process in psutil.process_iter(['name', 'pid', 'cpu_percent']):
        try:
            if process.name() and process.name().lower() == process_name.lower():
                process_list.append(process)
        except psutil.NoSuchProcess:
            pass
    return process_list


def monitor_process(process_name, interval=5, cpu_threshold=80):
    print(f"Monitoring process: {process_name}")
    print(f"Checking every {interval} seconds...\n")
    process_list = find_process_by_name(process_name)
    if not process_list:
        print(f"[ALERT] Process '{process_name}' is NOT running!")
    else:
        for process in process_list:
            try:
                cpu = process.cpu_percent(interval=0.1)
                pid = process.pid

                if cpu > cpu_threshold:
                    print(f"[WARNING] PID {pid} CPU usage high: {cpu}%")
                else:
                    print(f"PID {pid} OK | CPU: {cpu}%")
            except psutil.NoSuchProcess:
                print(f"[INFO] Process ended before reading CPU usage.")


if __name__ == "__main__":
    monitor_process("python", interval=5, cpu_threshold=80)