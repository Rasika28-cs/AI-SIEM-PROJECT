import win32evtlog
from datetime import datetime


SERVER = "localhost"

LOG_NAME = "Security"



def collect_windows_events():

    logs = []


    hand = win32evtlog.OpenEventLog(
        SERVER,
        LOG_NAME
    )


    flags = (
        win32evtlog.EVENTLOG_BACKWARDS_READ |
        win32evtlog.EVENTLOG_SEQUENTIAL_READ
    )


    events = win32evtlog.ReadEventLog(
        hand,
        flags,
        0
    )


    for event in events:


        event_id = event.EventID & 0xffff


        print(
            "Windows Event ID:",
            event_id
        )


        log = convert_event(event_id)


        if log:

            logs.append(log)



    return logs





def convert_event(event_id):


    if event_id == 4624:


        return {

            "source": "Windows",

            "category": "Authentication",

            "event_type": "LOGIN_SUCCESS",

            "severity": "LOW",

            "username": "unknown",

            "message": "Successful login detected"

        }



    elif event_id == 4625:


        return {

            "source": "Windows",

            "category": "Authentication",

            "event_type": "FAILED_LOGIN",

            "severity": "HIGH",

            "username": "unknown",

            "message": "Failed login attempt detected"

        }



    elif event_id == 4688:


        return {

            "source": "Windows",

            "category": "Process",

            "event_type": "PROCESS_CREATE",

            "severity": "MEDIUM",

            "username": "unknown",

            "message": "New process created"

        }



    elif event_id == 4720:


        return {

            "source": "Windows",

            "category": "Account",

            "event_type": "USER_CREATED",

            "severity": "MEDIUM",

            "username": "unknown",

            "message": "New user account created"

        }



    elif event_id == 1102:


        return {

            "source": "Windows",

            "category": "Security",

            "event_type": "AUDIT_LOG_CLEARED",

            "severity": "CRITICAL",

            "username": "unknown",

            "message": "Security audit log cleared"

        }



    return None