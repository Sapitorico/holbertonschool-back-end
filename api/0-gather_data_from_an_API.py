#!/usr/bin/python3
"""ss"""
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"

    todos_response = requests.get(todos_url, params={'userId': int(employee_id)})
    user_response = requests.get(users_url, params={'id': int(employee_id)})

    if todos_response.status_code != 200 or user_response.status_code != 200:
        print("Error: Failed to fetch data from the API.")
        sys.exit(1)

    todos = todos_response.json()
    user = user_response.json()

    if not user:
        print("Error: Employee with ID {} not found.".format(employee_id))
        sys.exit(1)

    employee_name = user[0].get('name')
    completed_tasks = []
    total_tasks = len(todos)

    for todo in todos:
        if todo.get('completed'):
            completed_tasks.append(todo.get('title'))

    num_completed_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task))

