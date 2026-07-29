from datetime import datetime
from config import AGENT_ID


def normalize_log(source, raw_log):
    """
    Convert any log into the standard SIEM event format.
    """

    # ------------------------------------
    # Case 1: Already a structured dictionary
    # ------------------------------------
    if isinstance(raw_log, dict):

        return {
            "time": datetime.now().isoformat(),
            "agent": raw_log.get("agent", AGENT_ID),
            "source": raw_log.get("source", source),
            "type": raw_log.get("type", "UNKNOWN"),
            "severity": raw_log.get("severity", "LOW"),
            "message": raw_log.get("message", ""),
        }

    # ------------------------------------
    # Case 2: Raw text log
    # ------------------------------------

    source = source.lower()
    text = str(raw_log).lower()

    event = {
        "time": datetime.now().isoformat(),
        "agent": AGENT_ID,
        "source": source.title(),
        "type": "UNKNOWN",
        "severity": "LOW",
        "message": str(raw_log)
    }

    # ====================================
    # Windows
    # ====================================

    if source == "windows":

        if "4625" in text or "failed login" in text:
            event["type"] = "FAILED_LOGIN"
            event["severity"] = "HIGH"
            event["message"] = "Windows failed login"

        elif "4624" in text:
            event["type"] = "SUCCESSFUL_LOGIN"
            event["severity"] = "LOW"
            event["message"] = "Windows successful login"

        elif "4720" in text:
            event["type"] = "USER_CREATED"
            event["severity"] = "MEDIUM"

        elif "4726" in text:
            event["type"] = "USER_DELETED"
            event["severity"] = "HIGH"

    # ====================================
    # Linux
    # ====================================

    elif source == "linux":

        if "failed password" in text:
            event["type"] = "FAILED_LOGIN"
            event["severity"] = "HIGH"
            event["message"] = "SSH login failed"

        elif "accepted password" in text:
            event["type"] = "SUCCESSFUL_LOGIN"
            event["severity"] = "LOW"

        elif "sudo" in text:
            event["type"] = "PRIVILEGE_ESCALATION"
            event["severity"] = "MEDIUM"

    # ====================================
    # Application
    # ====================================

    elif source == "application":

        if "critical" in text:
            event["type"] = "APPLICATION_CRITICAL"
            event["severity"] = "CRITICAL"

        elif "error" in text:
            event["type"] = "APPLICATION_ERROR"
            event["severity"] = "HIGH"

        elif "warning" in text:
            event["type"] = "APPLICATION_WARNING"
            event["severity"] = "MEDIUM"

    # ====================================
    # Network
    # ====================================

    elif source == "network":

        if "port scan" in text:
            event["type"] = "PORT_SCAN"
            event["severity"] = "HIGH"

        elif "connection refused" in text:
            event["type"] = "CONNECTION_REFUSED"
            event["severity"] = "MEDIUM"

    # ====================================
    # Generic Threat Detection
    # ====================================

    keywords = {
        "malware": ("MALWARE_DETECTED", "CRITICAL"),
        "ransomware": ("RANSOMWARE", "CRITICAL"),
        "virus": ("VIRUS_DETECTED", "HIGH"),
        "sql injection": ("SQL_INJECTION", "CRITICAL"),
        "xss": ("XSS_ATTACK", "HIGH"),
        "brute force": ("BRUTE_FORCE", "HIGH"),
    }

    for keyword, (event_type, severity) in keywords.items():
        if keyword in text:
            event["type"] = event_type
            event["severity"] = severity
            break

    return event