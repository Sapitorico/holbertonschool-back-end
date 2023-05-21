#!/usr/bin/python3
"""sqws"""
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/todos"
    get_name = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(
        url,
        params={'userId': int(user_id)})
    user_response = requests.get(
        get_name,
        params={'id': int(user_id)})
    count = 0
    total_tasks = 0
    tasks_text = []

    for key in response.json():
        if key['completed'] is True:
            count += 1
            tasks_text.append(key['title'])
        total_tasks += 1
    employee_name = ''
    for name in user_response.json():
        if 'name' in name.keys():
            employee_name = name['name']

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          count,
                                                          total_tasks))
    for task in tasks_text:
        print("\t {}".format(task))
