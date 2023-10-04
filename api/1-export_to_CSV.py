"""
This script uses an API to retrieve employee task information
and display in a special format.

It retrieves employees name, task completed with their titles.
"""
import csv
import os
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data['username']

    # Get employee TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Display progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for todo in todos_data:
        if todo['completed']:
            print(f"\t{todo['title']}")

    # Export data to CSV
    csv_file = f"{employee_id}.csv"
    if not os.path.exists(csv_file):
        print(f"CSV file '{csv_file}' does not exist.")
        return

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        task_count = sum(1 for _ in reader) - 1  # Subtract 1 to exclude the header row

    print(f"Number of tasks in CSV: {task_count}")

# Example usage: get_employee_todo_progress(8)
