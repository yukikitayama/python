import requests

# print(requests.codes.__dict__)

try:
    reply = requests.get("http://localhost:3000", timeout=1)
except requests.exceptions.InvalidURL:
    print("Invalid URL")
except requests.exceptions.ConnectionError:
    print("Connection error")
except requests.exceptions.Timeout:
    print("Timeout")
else:
    print(reply.status_code)
    print()
    print(reply.headers)
    print()
    print(reply.text)
