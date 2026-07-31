from collectors.application_logs import collect_application_logs


logs = collect_application_logs()


print("Total Application Logs:",
      len(logs))


for log in logs:

    print(log)