import psutil
from datetime import datetime


def collect_process_info():

    processes = []


    for process in psutil.process_iter(
        ['pid','name','username','cpu_percent','memory_percent']
    ):

        try:

            data = {

                "timestamp": datetime.now().isoformat(),

                "pid": process.info['pid'],

                "process_name": process.info['name'],

                "username": process.info['username'],

                "cpu_usage":
                process.info['cpu_percent'],

                "memory_usage":
                process.info['memory_percent']

            }


            processes.append(data)


        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied
        ):
            pass


    return processes