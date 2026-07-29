from collector import get_system_info
from sender import send_log
from normalizer import normalize_log

from logs.login_logs import collect_login_events
from logs.process_logs import collect_process_events
from logs.network_logs import collect_network_events

from collectors.application_logs import collect_application_logs
from collectors.windows_logs import collect_windows_events

from attack_simulator import (
    simulate_failed_login,
    simulate_port_scan,
    simulate_suspicious_process
)


def main():

    # ===========================
    # System Information
    # ===========================

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

        print(
            f"PID: {process['pid']} | {process['name']}"
        )


    # ===========================
    # Collect Normal Logs
    # ===========================

    print("\nCollecting Logs...\n")


    login_logs = collect_login_events()

    process_logs = collect_process_events()

    network_logs = collect_network_events()

    windows_events = collect_windows_events()

    application_logs = collect_application_logs()



    # ===========================
    # Simulate Attack Logs
    # ===========================

    failed_login_logs = simulate_failed_login()

    port_scan_logs = simulate_port_scan()

    suspicious_process_logs = simulate_suspicious_process()



    # ===========================
    # Combine All Logs
    # ===========================


    all_logs = (

        login_logs +

        process_logs +

        network_logs +

        windows_events +

        application_logs +

        failed_login_logs +

        port_scan_logs +

        suspicious_process_logs

    )


    print("\nTotal Logs Collected:",
          len(all_logs))



    # ===========================
    # Display Raw Logs
    # ===========================


    print("\n========== RAW LOGS ==========\n")


    for log in all_logs[:10]:

        print(log)



    # ===========================
    # DAY 4
    # Log Normalization
    # ===========================


    print("\n========== NORMALIZING LOGS ==========\n")


    normalized_logs = []


    for log in all_logs:


        # Detect log source

        if isinstance(log, dict):

            source = log.get(
                "source",
                "Application"
            )

            raw_log = str(log)


        else:

            source = "Application"

            raw_log = str(log)



        # Normalize

        normalized_event = normalize_log(source, log)


        normalized_logs.append(
            normalized_event
        )



    # ===========================
    # Display Normalized Events
    # ===========================


    print("\n========== NORMALIZED EVENTS ==========\n")


    for event in normalized_logs[:10]:

        print(event)



    # ===========================
    # Send To SIEM Backend
    # ===========================


    print(
        "\nSending Logs To Server...\n"
    )


    for event in normalized_logs:

        send_log(event)



    print(
        "\nAll normalized logs sent successfully."
    )



if __name__ == "__main__":

    main()