
import psutil
import socket
from datetime import datetime

from collectors.system_info import collect_system_info
from formatter import format_log


def get_protocol(connection):
    """
    Identify whether the connection is TCP or UDP.
    """

    if connection.type == socket.SOCK_STREAM:
        return "TCP"

    if connection.type == socket.SOCK_DGRAM:
        return "UDP"

    return "UNKNOWN"


def format_address(address):
    """
    Convert a psutil network address into IP:PORT format.
    """

    if not address:
        return None

    try:
        return f"{address.ip}:{address.port}"
    except Exception:
        return str(address)


def collect_network_events():
    """
    Collect active TCP and UDP network connections
    and convert them into SIEM formatted logs.
    """

    events = []

    # Get system information
    try:
        system_info = collect_system_info()
    except Exception:
        system_info = {}

    # Get network connections
    try:
        connections = psutil.net_connections(kind="inet")
    except Exception as error:
        print(f"[NETWORK] Error collecting network connections: {error}")
        return events

    for connection in connections:

        try:
            # Local address
            local_address = format_address(connection.laddr)

            # Remote address
            remote_address = format_address(connection.raddr)

            # Protocol
            protocol = get_protocol(connection)

            # Network event data
            network_data = {
                "event_type": "NETWORK_CONNECTION",
                "source": "Network",
                "protocol": protocol,
                "local_address": local_address,
                "remote_address": remote_address,
                "status": connection.status,
                "pid": connection.pid,
                "timestamp": datetime.now().isoformat()
            }

            # Create common SIEM log format
            log = format_log(
                "NETWORK",
                "LOW",
                f"{local_address} -> {remote_address}",
                system_info,
                extra_data=network_data
            )

            events.append(log)

        except Exception as error:
            print(f"[NETWORK] Error processing connection: {error}")
            continue

    return events
