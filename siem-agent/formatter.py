from datetime import datetime
from config import AGENT_ID


def format_log(event_type, severity, message, system_info, extra_data=None):

    log = {

        "agent": AGENT_ID,

        "hostname": system_info["hostname"],

        "ip_address": system_info["ip_address"],

        "type": event_type,

        "severity": severity,

        "message": message,

        "timestamp":
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    }


    if extra_data:

        log.update(extra_data)


    return log