import socket
import platform
import psutil


def get_system_info():
    """Collect basic system information."""

    hostname = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(hostname)
    except Exception:
        ip_address = "Unknown"

    os_name = platform.system()
    os_version = platform.version()

    cpu_usage = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()

    memory_total = round(memory.total / (1024 ** 3), 2)
    memory_used = round(memory.used / (1024 ** 3), 2)
    memory_percent = memory.percent

    processes = []

    for process in psutil.process_iter(['pid', 'name']):
        try:
            processes.append({
                "pid": process.info["pid"],
                "name": process.info["name"]
            })
        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    return {
        "hostname": hostname,
        "ip_address": ip_address,
        "operating_system": os_name,
        "os_version": os_version,
        "cpu_usage": cpu_usage,
        "memory": {
            "total_gb": memory_total,
            "used_gb": memory_used,
            "usage_percent": memory_percent
        },
        "process_count": len(processes),
        "running_processes": processes
    }