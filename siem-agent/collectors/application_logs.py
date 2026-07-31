import os
from datetime import datetime



APPLICATION_LOGS = {

    "Apache": "logs/apache/access.log",

    "MySQL": "logs/mysql/error.log",

    "Custom_App": "logs/application.log"

}



def parse_log(app_name, line):


    line = line.strip()


    # Remove empty logs

    if not line:

        return None



    severity = "LOW"

    event_type = "APPLICATION_EVENT"



    text = line.lower()



    if "critical" in text:

        severity = "CRITICAL"

        event_type = "APPLICATION_CRITICAL"



    elif "error" in text:

        severity = "HIGH"

        event_type = "APPLICATION_ERROR"



    elif "warning" in text:

        severity = "MEDIUM"

        event_type = "APPLICATION_WARNING"



    return {


        "source": "Application",


        "category": "Application",


        "event_type": event_type,


        "severity": severity,


        "message": line,


        "application": app_name,


        "timestamp": datetime.now().isoformat()

    }





def read_log_file(app_name, file_path):


    logs = []



    if not os.path.exists(file_path):

        return logs



    with open(
        file_path,
        "r",
        errors="ignore"
    ) as file:



        for line in file.readlines():


            event = parse_log(
                app_name,
                line
            )


            # Skip empty events

            if event:

                logs.append(event)



    return logs





def collect_application_logs():


    all_logs = []



    for app, path in APPLICATION_LOGS.items():


        logs = read_log_file(
            app,
            path
        )


        all_logs.extend(logs)



    return all_logs