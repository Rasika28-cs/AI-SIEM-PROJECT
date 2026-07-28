AGENT_ID = "PC01"   # Change if your agent_id is different


def simulate_failed_login():
    logs = []

    for i in range(5):
        logs.append({
            "agent": AGENT_ID,
            "type": "FAILED_LOGIN",
            "severity": "HIGH",
            "source": "Attack Simulator",
            "message": f"Failed login attempt {i + 1}",
            "username": "admin"
        })

    return logs


def simulate_port_scan():
    logs = []

    ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443]

    for port in ports:
        logs.append({
            "agent": AGENT_ID,
            "type": "PORT_SCAN",
            "severity": "MEDIUM",
            "source": "Attack Simulator",
            "message": f"Port {port} scanned",
            "port": port
        })

    return logs


def simulate_suspicious_process():
    return [
        {
            "agent": AGENT_ID,
            "type": "SUSPICIOUS_PROCESS",
            "severity": "CRITICAL",
            "source": "Attack Simulator",
            "message": "Unknown executable detected",
            "process": "evil.exe"
        }
    ]