#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, 
returns information about his/her TODO list progress
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./todo.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    user_info_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_info_response = requests.get(user_info_url)
    user_info = user_info_response.json()

    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    num_completed_todos = 0
    for todo in todos:
        if todo['completed']:
            num_completed_todos += 1
    num_total_todos = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(user_info['name'], num_completed_todos, num_total_todos))

    for todo in todos:
        if todo['completed']:
            print("\t {}".format(todo['title']))
