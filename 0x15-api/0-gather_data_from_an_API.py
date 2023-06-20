#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    _id = sys.argv[1]
    usr_url = "https://jsonplaceholder.typicode.com/users/{}".format(_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            _id)

    user = requests.get(usr_url).json()
    todos = requests.get(todos_url).json()

    completed = 0
    total = 0
    completed_tasks = []

    for task in todos:
        total += 1
        if task.get("completed") is True:
            completed += 1
            completed_tasks.append(task.get("title"))

    sentence = "Employee {} is done with tasks({}/{}):"
    print(sentence.format(user.get("name"), completed, total))
    for task in completed_tasks:
        print("\t {}".format(task))
