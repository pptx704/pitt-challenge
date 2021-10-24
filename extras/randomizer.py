import requests
import time

url = "http://151.106.113.197/inf/api"

while True:
    requests.post(f'{url}/randomize')
    time.sleep(60)