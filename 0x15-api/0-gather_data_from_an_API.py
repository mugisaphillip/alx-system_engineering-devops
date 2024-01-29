#!/usr/bin/python3
"""uses a rest api for a given employee ID"""
from requests import get
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user_data = get(f"{base_url}/users/{employee_id}")
    name = user_data.json().get("name")

    todos = get(f"{base_url}/users/{employee_id}/todos")
    todos = todos.json()
    complete = list(filter(lambda t: t.get("completed"), todos))
    print(f"Employee {name} is done with tasks({len(complete)}/{len(todos)}):")
    for todo in complete:
        print(f"\t {todo.get('title')}")
