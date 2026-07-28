import subprocess
from datetime import datetime


def detect_event(line):

    event = {
        "source": "Linux",
        "event_type": "SYSTEM_EVENT",
        "severity": "LOW",
        "message": line,
        "timestamp": str(datetime.now())
    }


    if "Failed password" in line:
        event["event_type"] = "SSH_FAILED_LOGIN"
        event["severity"] = "HIGH"


    elif "Accepted password" in line:
        event["event_type"] = "SSH_SUCCESS_LOGIN"
        event["severity"] = "MEDIUM"


    elif "authentication failure" in line:
        event["event_type"] = "FAILED_AUTHENTICATION"
        event["severity"] = "HIGH"


    elif "sudo" in line:
        event["event_type"] = "USER_ACTIVITY"
        event["severity"] = "MEDIUM"


    elif "error" in line.lower():
        event["event_type"] = "SYSTEM_ERROR"
        event["severity"] = "MEDIUM"


    return event



def collect_linux_logs():

    logs = []

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


    return logs



if __name__ == "__main__":

    linux_logs = collect_linux_logs()


    for log in linux_logs:
        print(log)