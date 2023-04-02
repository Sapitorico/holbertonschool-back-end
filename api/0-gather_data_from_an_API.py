#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress
"""

import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    user_info = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)).json()

    tasks = [task for task in todos if task.get('completed')]

    print('Employee {} is done with tasks({}/{}):'.format(
        user_info.get('name'),
        len(tasks),
        len(todos)
    ))

    for task in tasks:
        print('\t{}'.format(task.get('title')))