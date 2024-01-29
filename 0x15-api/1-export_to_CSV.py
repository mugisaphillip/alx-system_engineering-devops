#!/usr/bin/python3
"""uses a rest api for a given employee ID"""
from requests import get
from sys import argv


if __name__ == "__main__":
    e_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user_data = get(f"{base_url}/users/{e_id}")
    name = user_data.json().get("name")

    todos = get(f"{base_url}/users/{e_id}/todos")
    todos = todos.json()

    with open(f"{e_id}.csv", "w") as file:
        for t in todos:
            file.writelines(f'''"{e_id}","{name}","{t.get("completed")}",
                            "{t.get("title")}"\n''')
