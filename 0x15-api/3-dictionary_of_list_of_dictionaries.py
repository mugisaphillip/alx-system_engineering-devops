#!/usr/bin/python3
"""uses a rest api for a given employee ID"""
from requests import get
from json import dump


if __name__ == "__main__":
    e_id = 1
    data = {}
    while True:
        base_url = "https://jsonplaceholder.typicode.com"
        user_data = get(f"{base_url}/users/{e_id}")
        if user_data.status_code != 200:
            break

        name = user_data.json().get("name")
        todos = get(f"{base_url}/users/{e_id}/todos")
        todos = todos.json()

        data[e_id] = []
        for t in todos:
            d = {
                    'username': name,
                    'task': t.get("title"),
                    'completed': t.get("completed")
                }
            data.get(e_id).append(d)
        e_id += 1

    with open(f"todo_all_employees.json", "w") as file:
        dump(data, file)
