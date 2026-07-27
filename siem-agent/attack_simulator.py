def simulate_failed_login():
    logs = []

    for i in range(5):
        logs.append({
            "type": "FAILED_LOGIN",
            "severity": "HIGH",
            "message": f"Failed login attempt {i + 1}",
            "username": "admin"
        })

    return logs


def simulate_port_scan():
    logs = []

    ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443]

    for port in ports:
        logs.append({
            "type": "PORT_SCAN",
            "severity": "MEDIUM",
            "message": f"Port {port} scanned",
            "port": port
        })

    return logs


def simulate_suspicious_process():
    return [
        {
            "type": "SUSPICIOUS_PROCESS",
            "severity": "CRITICAL",
            "message": "Unknown executable detected",
            "process": "evil.exe"
        }
    ]