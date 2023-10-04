"""
Employee Task Information Retrieval and CSV Export Script

This script retrieves task information for a specified employee using an API
and exports the data in CSV format.

Usage:
    python script_name.py employee_id

APIs:
    - User Todo URL: https://jsonplaceholder.typicode.com/users/{employee_id}/todos
    - User Profile URL: https://jsonplaceholder.typicode.com/users/{employee_id}

Dependencies:
    - requests
    - csv

Script Execution:
    - The script should be executed from the command line with the employee_id as an argument.

Output:
    - Prints the employee's task completion status and titles.
    - Exports data to a CSV file named USER_ID.csv.

CSV Format:
    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

Example:
    python script_name.py 1

"""
import csv
import os  # Import the os module
import requests
import sys

def user_info(id):
    try:
        # Try to open the CSV file
        with open(str(id) + ".csv", 'r') as f:
            # Rest of the code for reading and printing tasks
            reader = csv.reader(f)
            header = next(reader)
            print("Number of tasks in CSV:", len(list(reader)))
    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        print(f"CSV file for user {id} not found.")

# No execution of this file when imported
if __name__ == "__main__":
    # Pass employee id on command line
    id = sys.argv[1]

    # Rest of the script remains unchanged
    # ...
