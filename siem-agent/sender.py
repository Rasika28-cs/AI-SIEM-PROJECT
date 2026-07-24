import requests
from config import SERVER_URL

def send_data(data):
    try:
        response = requests.post(SERVER_URL, json=data)
        print("Status Code:", response.status_code)
    except Exception as e:
        print("Server not available:", e)