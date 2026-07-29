import platform
import socket
import psutil
from datetime import datetime


def collect_system_info():

    hostname = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(hostname)
    except:
        ip_address = "Unknown"


    system_data = {

        "timestamp": datetime.now().isoformat(),

        "hostname": hostname,

        "ip_address": ip_address,

        "operating_system": platform.system(),

        "os_version": platform.version(),

        "architecture": platform.machine(),

        "processor": platform.processor(),

        "cpu_usage": psutil.cpu_percent(interval=1),

        "memory_usage": psutil.virtual_memory().percent,

        "disk_usage": psutil.disk_usage('/').percent

    }


    return system_data