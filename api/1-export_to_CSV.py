import os
import requests
import csv
import sys

def export_employee_todo_list_to_csv(employee_id):
    """Exports the employee's TODO list to a CSV file."""
    try:
        # ... (unchanged code for fetching and exporting TODO list)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching TODO list for employee {employee_id}: {e}")

def user_info(id):
    """Prints the formatted output for a given user."""
    try:
        # Check if the CSV file exists before opening it.
        csv_file_path = str(id) + ".csv"
        if os.path.exists(csv_file_path):
            with open(csv_file_path, 'r') as f:
                csv_reader = csv.reader(f)
                # Skip the header row
                next(csv_reader)
                # Get the first row (user ID, username, task completion status, task title)
                user_info_row = next(csv_reader)
                user_id, username, task_status, task_title = user_info_row
                print(f"Formatting: {user_id},{username},{task_status},{task_title}")
        else:
            print(f"CSV file for user {id} not found.")

    except FileNotFoundError:
        print(f"CSV file for user {id} not found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    export_employee_todo_list_to_csv(employee_id)
    user_info(employee_id)
