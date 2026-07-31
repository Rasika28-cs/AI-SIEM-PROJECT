import requests
import json
import os

from config import SERVER_URL



QUEUE_FILE = "storage/failed_logs.txt"



def save_failed_log(log):

    os.makedirs(
        "storage",
        exist_ok=True
    )


    with open(
        QUEUE_FILE,
        "a"
    ) as file:

        file.write(
            json.dumps(log)
            + "\n"
        )



def send_log(log):

    try:

        print(
            "Sending:",
            log
        )


        response = requests.post(

            SERVER_URL,

            json=log,

            timeout=5

        )


        if response.status_code == 200:


            print(
                "Log Sent Successfully"
            )


        else:


            print(
                "Server Error:",
                response.status_code
            )


            save_failed_log(log)



    except Exception as e:


        print(
            "Sending Failed:",
            e
        )


        save_failed_log(log)