#!/usr/bin/python3
"""API"""
import csv
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
            done.append([argv[1], uname, i['completed'], i['title']])

    with open(argv[1] + '.csv', 'w') as csvfile:
        sw = csv.writer(csvfile, delimiter=',', lineterminator='\r\n',
                        quoting=csv.QUOTE_ALL)
        for i in done:
            sw.writerow(i)
