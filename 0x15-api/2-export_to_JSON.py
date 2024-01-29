#!/usr/bin/python3
"""uses a rest api for a given employee ID"""
from requests import get
from sys import argv
from json import dump


if __name__ == "__main__":
    e_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user_data = get(f"{base_url}/users/{e_id}")
    name = user_data.json().get("name")

    todos = get(f"{base_url}/users/{e_id}/todos")
    todos = todos.json()

    data = {e_id: []}
    for t in todos:
        d = {
                'task': t.get("title"),
                'completed': t.get("completed"),
                'username': name
            }
        data.get(e_id).append(d)

    with open(f"{e_id}.json", "w") as file:
        dump(data, file)
