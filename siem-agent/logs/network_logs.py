import psutil

from collector import get_system_info
from formatter import format_log


def collect_network_events():

    events = []

    system_info = get_system_info()


    for connection in psutil.net_connections():

        try:

            address = str(connection.laddr)

            events.append(
                format_log(
                    "NETWORK",
                    "LOW",
                    f"Network connection {address}",
                    system_info
                )
            )


        except Exception:
            pass


    return events