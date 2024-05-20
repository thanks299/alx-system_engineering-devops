#!/usr/bin/python3
""" Returns information about his/her todo list progress and export data to CSV file """

import requests
import sys
import csv

if __name__ == "__main__":
    """ code process:
    - API Base URL
    - Gets user data
    - Gets todos for the specified user
    - Extract completed tasks
    - Print info about the employee's todo list progress
    - Print titles of tasks completed
    - Export data to CSV file
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
    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in todos:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': user.get("name"),
                'TASK_COMPLETED_STATUS': task.get("completed"),
                'TASK_TITLE': task.get("title")
            })
