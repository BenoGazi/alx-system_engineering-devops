#!/usr/bin/python3
"""Returns a to-do list info for a given employee ID"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    com = [t.get("title") for t in todos if t.get("completed") is True]
    name = user.get("name")
    com_count = len(com)
    total_count = len(todos)
    print(f"Employee {name} is done with tasks({com_count}/{total_count}):")
    [print("\t {}".format(c)) for c in com]
