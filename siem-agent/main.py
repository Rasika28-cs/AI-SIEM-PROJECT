from collector import get_system_info


def main():
    system_info = get_system_info()

    print("=" * 50)
    print("AI SIEM Agent - System Information")
    print("=" * 50)

    print(f"Hostname         : {system_info['hostname']}")
    print(f"IP Address       : {system_info['ip_address']}")
    print(f"Operating System : {system_info['operating_system']}")
    print(f"OS Version       : {system_info['os_version']}")
    print(f"CPU Usage        : {system_info['cpu_usage']}%")

    memory = system_info["memory"]

    print(f"Memory Total     : {memory['total_gb']} GB")
    print(f"Memory Used      : {memory['used_gb']} GB")
    print(f"Memory Usage     : {memory['usage_percent']}%")
    print(f"Running Processes: {system_info['process_count']}")

    print("\nFirst 10 Running Processes:\n")

    for process in system_info["running_processes"][:10]:
        print(f"PID: {process['pid']} | {process['name']}")


if __name__ == "__main__":
    main()