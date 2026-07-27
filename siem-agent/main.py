from collector import get_system_info
from sender import send_log

from logs.login_logs import collect_login_events
from logs.process_logs import collect_process_events
from logs.network_logs import collect_network_events

from attack_simulator import (
    simulate_failed_login,
    simulate_port_scan,
    simulate_suspicious_process
)


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

    # ===========================
    # Collect Normal Logs
    # ===========================

    login_logs = collect_login_events()
    process_logs = collect_process_events()
    network_logs = collect_network_events()

    # ===========================
    # Simulate Attack Logs
    # ===========================

    failed_login_logs = simulate_failed_login()
    port_scan_logs = simulate_port_scan()
    suspicious_process_logs = simulate_suspicious_process()

    # Combine everything

    all_logs = (
        login_logs +
        process_logs +
        network_logs +
        failed_login_logs +
        port_scan_logs +
        suspicious_process_logs
    )

    # ---------------------------
    # Display Normal Logs
    # ---------------------------

    print("\nLogin Events")
    for log in login_logs:
        print(log)

    print("\nProcess Events")
    for log in process_logs[:10]:
        print(log)

    print("\nNetwork Events")
    for log in network_logs[:10]:
        print(log)

    # ---------------------------
    # Display Simulated Attacks
    # ---------------------------

    print("\nSimulated Failed Login Attacks")
    for log in failed_login_logs:
        print(log)

    print("\nSimulated Port Scan")
    for log in port_scan_logs:
        print(log)

    print("\nSimulated Suspicious Process")
    for log in suspicious_process_logs:
        print(log)

    print("\nSending Logs To Server...\n")

    for log in all_logs:
        send_log(log)

    print("\nAll logs sent successfully.")


if __name__ == "__main__":
    main()