import psutil

from collectors.system_info import collect_system_info
from formatter import format_log


def collect_process_events():

    events = []

    system_info = collect_system_info()

    count = 0

    for process in psutil.process_iter(['pid', 'name']):

        if count >= 20:
            break

        try:

            process_name = process.info["name"]

            if process_name:

                events.append(
                    format_log(
                        "PROCESS",
                        "LOW",
                        f"PID:{process.info['pid']} {process_name}",
                        system_info
                    )
                )

                count += 1

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

    return events