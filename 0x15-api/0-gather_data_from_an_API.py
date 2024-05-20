#!/usr/bin/python3
""" Returns information about his/her todo list progress and export data to CSV and JSON files """

import requests
import sys
import csv
import json

if __name__ == "__main__":
    """ code process:
    - API Base URL
    - Gets user data
    - Gets todos for the specified user
    - Extract completed tasks
    - Print info about the employee's todo list progress
    - Print titles of tasks completed
    - Export data to CSV file
    - Export data to JSON file
    """

    api_url = "(link unavailable)"
    user_id = sys.argv[1]

    user = requests.get(api_url + "users/{}".format(user_id)).json()
    todos = requests.get(api_url + "todos", params={"userId": user_id}).json()

    done = [u.get("title") for u in todos if u.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"),
        len(done),
        len(todos)
    ))

    [print("\t {}".format(v)) for v in done]

    # Export data to CSV file
    with open('{}.csv'.format(user.get("name")), 'w', newline='') as csvfile:
        fieldnames = ['task_id', 'task_title', 'completed']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in todos:
            writer.writerow({
                'task_id': task.get("id"),
                'task_title': task.get("title"),
                'completed': task.get("completed")
            })

    # Export data to JSON file
    with open('{}.json'.format(user.get("name")), 'w') as jsonfile:
        json.dump(todos, jsonfile)
