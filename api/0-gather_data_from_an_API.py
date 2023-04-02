#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)).json()
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)).json()

    completed_tasks = [task for task in tasks if task['completed']]

    print("Employee {} is done with tasks({}/{}):".format(
        user['name'], len(completed_tasks), len(tasks)))

    for task in completed_tasks:
        print("\t {}".format(task['title']))
