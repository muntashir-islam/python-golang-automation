import json

def get_public_ip(instance):
    return instance.get("PublicIpAddress", "N/A")


def main():
    stopped_instances = []
    count_running = 0
    count_stopped = 0

    # Load file
    try:
        with open("ec2_instances.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: ec2_instances.json not found.")
        return

    # Loop through reservations and instances
    for reservation in data["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            state = instance["State"]["Name"]
            public_ip = get_public_ip(instance)

            print(
                f"InstanceId: {instance_id} | "
                f"Type: {instance_type} | "
                f"State: {state} | "
                f"Public IP: {public_ip}"
            )

            if state == "running":
                count_running += 1
            elif state == "stopped":
                stopped_instances.append(instance_id)
                count_stopped += 1

    # Print summary
    print(f"Running: {count_running}")
    print(f"Stopped: {count_stopped}")

    # Write stopped instances to file
    with open("stopped_instances.log", "a") as f:
        f.write("\n".join(stopped_instances) + "\n")


if __name__ == "__main__":
    main()
