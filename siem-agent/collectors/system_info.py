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

    memory = psutil.virtual_memory()

    running_processes = []

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            running_processes.append({
                "pid": proc.info["pid"],
                "name": proc.info["name"]
            })
        except:
            pass

    return {
        "timestamp": datetime.now().isoformat(),
        "hostname": hostname,
        "ip_address": ip_address,
        "operating_system": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "cpu_usage": psutil.cpu_percent(interval=1),

        "memory": {
            "total_gb": round(memory.total / (1024 ** 3), 2),
            "used_gb": round(memory.used / (1024 ** 3), 2),
            "usage_percent": memory.percent
        },

        "disk_usage": psutil.disk_usage('/').percent,

        "process_count": len(running_processes),

        "running_processes": running_processes
    }