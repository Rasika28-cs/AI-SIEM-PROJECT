def filter_by_severity(logs, severity):

    filtered_logs = []


    for log in logs:

        if log.get("severity") == severity:

            filtered_logs.append(log)


    return filtered_logs





def filter_by_source(logs, source):

    filtered_logs = []


    for log in logs:

        if log.get("source") == source:

            filtered_logs.append(log)


    return filtered_logs





def filter_by_event_type(logs, event_type):

    filtered_logs = []


    for log in logs:

        if log.get("event_type") == event_type:

            filtered_logs.append(log)


    return filtered_logs





def remove_low_priority_logs(logs):

    priority_logs = []


    ignored_levels = [

        "LOW"

    ]


    for log in logs:

        if log.get("severity") not in ignored_levels:

            priority_logs.append(log)


    return priority_logs