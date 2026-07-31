import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from formatter import format_log
from collectors.system_info import collect_system_info


def collect_login_events():

    system_info = collect_system_info()

    logs = []

    logs.append(
        format_log(
            "LOGIN_FAILED",
            "HIGH",
            "Multiple failed login attempts",
            system_info
        )
    )

    return logs