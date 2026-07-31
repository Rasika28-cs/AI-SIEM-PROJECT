import requests
import json
import os

from config import SERVER_URL, HEARTBEAT_URL



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


        if response.status_code in [200, 201]:


            print(
                "Log Sent Successfully"
            )


        else:


            print(
                "Server Error:",
                response.status_code,
                response.text
            )


            save_failed_log(log)



    except Exception as e:


        print(
            "Sending Failed:",
            e
        )


        save_failed_log(log)




def send_heartbeat(heartbeat):

    try:

        print(
            "Sending Heartbeat:",
            heartbeat
        )

        response = requests.post(

            HEARTBEAT_URL,

            json=heartbeat,

            timeout=5

        )

        if response.status_code == 200:

            print(
                "Heartbeat Sent Successfully"
            )

        else:

            print(
                "Heartbeat Error:",
                response.status_code,
                response.text
            )

    except Exception as e:

        print(
            "Heartbeat Failed:",
            e
        )