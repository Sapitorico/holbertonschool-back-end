#!/usr/bin/python3
"""API"""
import json
import requests


src = 'https://jsonplaceholder.typicode.com/'

if __name__ == '__main__':
    final = {}
    todos = requests.get(src + "todos").json()
    done = []
    j = 0
    for i in list(todos):
        u = requests.get(src + "users/" + str(i['userId'])).json()
        uname = u['username']
        done.append([u['id'], uname, i['title'], i['completed']])

    for i in done:
        try:
            final[str(i[0])]
        except Exception:
            final[str(i[0])] = []
        final[str(i[0])].append({"username": i[1],
                                 "task": i[2],
                                 "completed": i[3]})

    with open('todo_all_employees.json', 'w') as f:
        f.write(json.dumps(final))
        f.close()
