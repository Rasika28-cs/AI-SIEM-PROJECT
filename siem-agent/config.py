import json
import os


CONFIG_FILE = "config.json"


if not os.path.exists(CONFIG_FILE):

    raise FileNotFoundError(
        "config.json not found"
    )


with open(CONFIG_FILE, "r") as file:

    config = json.load(file)



AGENT_ID = config.get(
    "agent_id",
    "UNKNOWN"
)


SERVER_URL = config.get(
    "server_url",
    ""
)


HEARTBEAT_URL = config.get(
    "heartbeat_url",
    ""
)