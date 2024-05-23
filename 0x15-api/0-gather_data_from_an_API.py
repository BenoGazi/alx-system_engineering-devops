#!/usr/bin/python3
"""Returns a to-do list info for a given employee ID"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    com = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with the tasks({}/{}):".format(
        user.get("name"), len(com), len(todos)))
    for c in com:
        print("\t{}".format(c))
