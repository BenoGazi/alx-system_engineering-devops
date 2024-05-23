#!/usr/bin/python3
"""Export a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    user_name = user.get("username")
    todo_list = requests.get(url + "todos", params={"userId": employee_id}).json()

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todo_list:
            writer.writerow([employee_id, user_name, todo.get("completed"), todo.get("title")])
