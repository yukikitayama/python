import requests

names = ["id", "brand", "model", "production_year", "convertible"]
widths = [10, 15, 10, 20, 15]


def show_head():
    for n, w in zip(names, widths):
        print(n.ljust(w), end="| ")
    print()


def show_car(car):
    for n, w in zip(names, widths):
        print(str(car[n]).ljust(w), end="| ")
    print()


def show(json_):
    show_head()
    for car in json_:
        show_car(car)


try:
    headers = {"Connection": "Close"}
    reply = requests.get("http://localhost:3000/cars", headers=headers)
except requests.RequestException:
    print("Communication error")
else:
    print("Connection=" + reply.headers["Connection"])
    if reply.status_code == requests.codes.ok:
        # print(reply.text)
        print(reply.headers["Content-Type"])
        # print(reply.json())
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print("Server error")

