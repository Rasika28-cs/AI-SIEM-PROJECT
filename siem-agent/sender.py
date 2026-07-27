import requests

from config import SERVER_URL


def send_log(log):

    try:

        response = requests.post(
            SERVER_URL,
            json=log
        )

        print(
            "Log Sent:",
            response.status_code,
            log["type"]
        )

    except Exception as e:

        print("Sending Error:", e)