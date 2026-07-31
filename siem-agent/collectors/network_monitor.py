import psutil
import socket
from datetime import datetime


def get_protocol(connection):
    """
    Identify the network protocol from the socket type.
    """

    if connection.type == socket.SOCK_STREAM:
        return "TCP"

    if connection.type == socket.SOCK_DGRAM:
        return "UDP"

    return "UNKNOWN"


def format_address(address):
    """
    Convert psutil address object into IP:PORT format.
    """

    if not address:
        return None

    try:
        return f"{address.ip}:{address.port}"
    except AttributeError:
        return str(address)


def collect_network_events():
    """
    Collect active TCP and UDP network connections.

    Returns:
        list: Raw network event dictionaries.
    """

    network_events = []

    try:
        connections = psutil.net_connections(kind="inet")

    except Exception as error:
        print(f"[NETWORK] Unable to collect connections: {error}")
        return network_events

    for connection in connections:

        try:
            local_address = format_address(connection.laddr)
            remote_address = format_address(connection.raddr)

            protocol = get_protocol(connection)

            event = {
                "event_type": "NETWORK_CONNECTION",

                "source": "Network",

                "protocol": protocol,

                "local_address": local_address,

                "remote_address": remote_address,

                "status": connection.status,

                "pid": connection.pid,

                "timestamp": datetime.now().isoformat(),

            }

            network_events.append(event)

        except Exception:
            continue

    return network_events