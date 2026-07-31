from datetime import datetime
import socket
import platform


from config import AGENT_ID


def get_ip_address():

    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        return ip_address

    except Exception:
        return "UNKNOWN"



def generate_heartbeat():

    heartbeat = {

        "agent_id": AGENT_ID,

        "hostname": socket.gethostname(),

        "ip_address": get_ip_address(),

        "operating_system": platform.system(),

        "status": "ONLINE",

        "type": "HEARTBEAT",

        "timestamp": datetime.now().isoformat()

    }


    return heartbeat