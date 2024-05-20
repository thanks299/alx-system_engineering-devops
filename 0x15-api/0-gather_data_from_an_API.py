#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 (link unavailable) <employee_id>")
    sys.exit(1)

employee_id = int(sys.argv[1])

response = requests.get(f'(link unavailable)')
user_data = response.json()

todo_response = requests.get(f'(link unavailable)')
todo_data = todo_response.json()

completed_tasks = [task['title'] for task in todo_data if task['completed']]
total_tasks = len(todo_data)

print(f'Employee {user_data["name"]} is done with tasks({len(completed_tasks)}/{total_tasks}):')
for task in completed_tasks:
    print(f'\t{task}')
