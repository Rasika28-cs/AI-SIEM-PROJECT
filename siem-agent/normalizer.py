from datetime import datetime
from config import AGENT_ID
import socket



def normalize_log(raw_log):

    """
    Convert all SIEM Agent logs into common SIEM format.
    Supports:
    - System logs
    - Process logs
    - Login events
    - Windows events
    - Application logs
    - Network logs
    """

    hostname = socket.gethostname()


    # Safety check

    if not isinstance(raw_log, dict):

        raw_log = {
            "message": str(raw_log)
        }



    # Detect source

    source = raw_log.get(
        "source"
    )


    old_type = raw_log.get(
        "type",
        ""
    )


    event_type = raw_log.get(
        "event_type"
    )



    category = "General"



    # Source based classification

    if source == "Windows":

        category = "Authentication"



    elif source == "Linux":

        category = "Authentication"



    elif source == "Application":

        category = "Application"



    elif source == "Network":

        category = "Network"



    elif old_type == "LOGIN_FAILED":

        source = "Windows"

        category = "Authentication"

        event_type = "LOGIN_FAILED"



    elif old_type == "PROCESS":

        source = "System"

        category = "Process"

        event_type = "PROCESS"



    elif old_type == "NETWORK":

        source = "Network"

        category = "Network"

        event_type = "NETWORK_CONNECTION"



    else:

        source = source or "Unknown"



    # Event type fallback

    if not event_type:

        event_type = old_type or "UNKNOWN"



    # Final normalized SIEM event

    normalized = {


        "agent_id": AGENT_ID,


        "hostname": hostname,


        "timestamp": raw_log.get(
            "timestamp",
            datetime.now().isoformat()
        ),


        "source": source,


        "category": category,


        "event_type": event_type,


        "severity": raw_log.get(
            "severity",
            "LOW"
        ),


        "username": raw_log.get(
            "username",
            raw_log.get(
                "user",
                "unknown"
            )
        ),


        "message": raw_log.get(
            "message",
            ""
        ),



        # Network details

        "ip_address": raw_log.get(
            "ip_address",
            None
        ),


        "local_address": raw_log.get(
            "local_address",
            None
        ),


        "remote_address": raw_log.get(
            "remote_address",
            None
        ),


        "protocol": raw_log.get(
            "protocol",
            None
        ),


        "status": raw_log.get(
            "status",
            None
        ),


        "pid": raw_log.get(
            "pid",
            None
        ),



        "process_name": raw_log.get(
            "process_name",
            None
        ),


        "application": raw_log.get(
            "application",
            None
        ),



        # Original event

        "raw_data": raw_log

    }



    return normalized