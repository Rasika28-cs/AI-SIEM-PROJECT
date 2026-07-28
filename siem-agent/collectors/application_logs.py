import os
import time
from datetime import datetime


# Application log locations
APPLICATION_LOGS = {
    "Apache": "logs/apache/access.log",
    "MySQL": "logs/mysql/error.log",
    "Custom_App": "logs/application.log"
}


def read_log_file(app_name, file_path):

    logs = []

    if not os.path.exists(file_path):
        return logs


    with open(file_path, "r") as file:

        lines = file.readlines()


    for line in lines:

        log = parse_log(app_name, line)

        if log:
            logs.append(log)


    return logs



def parse_log(app_name, line):

    level = "INFO"


    if "ERROR" in line.upper():
        level = "ERROR"

    elif "WARNING" in line.upper():
        level = "WARNING"



    return {

        "application": app_name,

        "timestamp": datetime.now().isoformat(),

        "level": level,

        "message": line.strip(),

        "source": file_source(app_name)

    }



def file_source(app_name):

    sources = {

        "Apache":"apache/access.log",

        "MySQL":"mysql/error.log",

        "Custom_App":"application.log"

    }


    return sources.get(app_name)



def collect_application_logs():

    all_logs = []


    for app, path in APPLICATION_LOGS.items():

        logs = read_log_file(app,path)

        all_logs.extend(logs)


    return all_logs