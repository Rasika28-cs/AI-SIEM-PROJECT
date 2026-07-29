import psutil
from datetime import datetime


def collect_network_connections():

    connections = []


    for conn in psutil.net_connections(kind="inet"):

        try:

            network_data = {


                "timestamp":
                datetime.now().isoformat(),


                "local_address":
                str(conn.laddr)
                if conn.laddr else None,


                "remote_address":
                str(conn.raddr)
                if conn.raddr else None,


                "status":
                conn.status,


                "protocol":
                "TCP"
                if conn.type == 1
                else "UDP",


                "pid":
                conn.pid

            }


            connections.append(network_data)


        except Exception:

            pass


    return connections