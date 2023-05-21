#!/usr/bin/python3
"""API"""
import json
import requests
from sys import argv

src = 'https://jsonplaceholder.typicode.com/'

if __name__ == '__main__':
    todos = requests.get(src + "todos?userId=" + argv[1]).json()
    u = requests.get(src + 'users/' + argv[1]).json()
    uname = u['username']
    done = []
    j = 0
    for i in list(todos):
        if int(i['userId']) == int(argv[1]):
            done.append({"task": i['title'], "completed": i['completed'],
                         "username": uname})

    with open(argv[1] + '.json', 'w') as f:
        f.write(json.dumps({argv[1]: done}))
        f.close()
