import time


from collectors.system_info import collect_system_info
from collectors.network_monitor import collect_network_events


from sender import send_log
from normalizer import normalize_log

from heartbeat import generate_heartbeat


from logs.login_logs import collect_login_events
from logs.process_logs import collect_process_events
from logs.network_logs import collect_network_events


from collectors.application_logs import collect_application_logs
from collectors.windows_logs import collect_windows_events
from collectors.linux_logs import collect_linux_logs


from filters import remove_low_priority_logs


from attack_simulator import (
    simulate_failed_login,
    simulate_port_scan,
    simulate_suspicious_process
)



def main():


    while True:


        # ===========================
        # SYSTEM INFORMATION
        # ===========================


        system_info = collect_system_info()


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



        # ===========================
        # HEARTBEAT
        # ===========================


        print("\n========== AGENT HEARTBEAT ==========\n")


        heartbeat = generate_heartbeat()


        print(heartbeat)


        send_log(heartbeat)



        # ===========================
        # COLLECT LOGS
        # ===========================


        print("\n========== COLLECTING LOGS ==========\n")



        login_logs = collect_login_events()


        process_logs = collect_process_events()


        # Existing network logs
        network_logs = collect_network_events()


        # NEW Network Monitoring
        network_monitor_logs = collect_network_events()



        windows_events = collect_windows_events()


        linux_events = collect_linux_logs()


        application_logs = collect_application_logs()



        # ===========================
        # ATTACK SIMULATION
        # ===========================


        failed_login_logs = simulate_failed_login()


        port_scan_logs = simulate_port_scan()


        suspicious_process_logs = simulate_suspicious_process()



        # ===========================
        # COMBINE ALL LOGS
        # ===========================


        all_logs = (

            login_logs +

            process_logs +

            network_logs +

            network_monitor_logs +

            windows_events +

            linux_events +

            application_logs +

            failed_login_logs +

            port_scan_logs +

            suspicious_process_logs

        )



        print(
            "\nTotal Raw Logs:",
            len(all_logs)
        )



        # ===========================
        # FILTERING
        # ===========================


        filtered_logs = remove_low_priority_logs(
            all_logs
        )


        print(
            "Security Logs After Filtering:",
            len(filtered_logs)
        )



        # ===========================
        # NORMALIZATION
        # ===========================


        print(
            "\n========== NORMALIZING LOGS ==========\n"
        )


        normalized_logs = []



        for log in filtered_logs:


            normalized_event = normalize_log(log)


            normalized_logs.append(
                normalized_event
            )



        print(
            "Total Normalized Events:",
            len(normalized_logs)
        )



        # ===========================
        # DISPLAY EVENTS
        # ===========================


        print(
            "\n========== NORMALIZED EVENTS ==========\n"
        )


        for event in normalized_logs[:10]:

            print(event)



        # ===========================
        # SEND TO BACKEND
        # ===========================


        print(
            "\n========== SENDING LOGS ==========\n"
        )


        logs_to_send = normalized_logs[:20]


        print(
            "Sending",
            len(logs_to_send),
            "logs"
        )



        for event in logs_to_send:

            send_log(event)



        print(
            "\nLogs sent successfully."
        )



        # ===========================
        # REAL TIME COLLECTION
        # ===========================


        print(
            "\nWaiting 5 seconds for next collection..."
        )


        time.sleep(5)




if __name__ == "__main__":

    main()