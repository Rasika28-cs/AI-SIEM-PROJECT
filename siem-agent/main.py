from collector import get_system_info
from sender import send_log
from logs.login_logs import collect_login_events
from logs.process_logs import collect_process_events
from logs.network_logs import collect_network_events


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

    # Collect logs
    # Collect logs
    login_logs = collect_login_events()
    process_logs = collect_process_events()
    network_logs = collect_network_events()


    all_logs = (
        login_logs +
        process_logs +
        network_logs
    )

    # Display login logs
    print("\nLogin Events")
    for log in login_logs:
        print(log)

    # Display process logs
    print("\nProcess Events")
    for log in process_logs[:10]:
        print(log)

    # Display network logs
    print("\nNetwork Events")
    for log in network_logs[:10]:
        print(log)
    print("\nSending Logs To Server...\n")


    for log in all_logs:

        send_log(log)

if __name__ == "__main__":
    main()