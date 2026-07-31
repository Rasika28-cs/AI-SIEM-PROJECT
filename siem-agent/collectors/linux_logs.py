import subprocess
from datetime import datetime



def detect_event(line):


    text = line.lower()


    event = {

        "source": "Linux",

        "category": "System",

        "event_type": "SYSTEM_EVENT",

        "severity": "LOW",

        "username": "unknown",

        "message": line,

        "timestamp": datetime.now().isoformat()

    }



    if "failed password" in text:


        event["category"] = "Authentication"

        event["event_type"] = "SSH_FAILED_LOGIN"

        event["severity"] = "HIGH"



    elif "accepted password" in text:


        event["category"] = "Authentication"

        event["event_type"] = "SSH_SUCCESS_LOGIN"

        event["severity"] = "LOW"



    elif "authentication failure" in text:


        event["category"] = "Authentication"

        event["event_type"] = "FAILED_AUTHENTICATION"

        event["severity"] = "HIGH"



    elif "sudo" in text:


        event["category"] = "Privilege"

        event["event_type"] = "USER_ACTIVITY"

        event["severity"] = "MEDIUM"



    elif "error" in text:


        event["category"] = "System"

        event["event_type"] = "SYSTEM_ERROR"

        event["severity"] = "MEDIUM"



    return event





def collect_linux_logs():


    logs = []


    try:


        command = [

            "journalctl",

            "-n",

            "50",

            "--no-pager"

        ]


        result = subprocess.run(

            command,

            capture_output=True,

            text=True

        )


        for line in result.stdout.splitlines():


            logs.append(
                detect_event(line)
            )



    except Exception as e:


        print(
            "Linux log collection skipped:",
            e
        )



    return logs





if __name__ == "__main__":


    linux_logs = collect_linux_logs()


    for log in linux_logs:

        print(log)