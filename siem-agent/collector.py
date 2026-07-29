from collector.system_info import get_system_info
from collector.process_monitor import get_process_info
from collector.network_monitor import get_network_info
from collector.windows_log import get_windows_logs
from collector.security_logs import get_security_logs


def collect_all():

    collected_data = {

        "system_info": get_system_info(),

        "process_info": get_process_info(),

        "network_info": get_network_info(),

        "windows_logs": get_windows_logs(),

        "security_logs": get_security_logs()

    }

    return collected_data