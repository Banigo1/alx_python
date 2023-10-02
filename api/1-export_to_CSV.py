"""This module Records all tasks that are owned by this employee
    and exports the data in the CSV format."""

import requests
import csv

def export_employee_todo_list_to_csv(employee_id):
    """Exports the employee's TODO list to a CSV file."""

    # Get the employee's TODO list items.
    todo_list_items_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    todo_list_items_response = requests.get(todo_list_items_url)
    todo_list_items = todo_list_items_response.json()

    # Open a CSV file for writing.
    csv_file = open(f"{employee_id}.csv", "w")

    # Create a CSV writer object.
    csv_writer = csv.writer(csv_file)

    # Write the header row to the CSV file.
    csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

    # Iterate over the employee's TODO list items, and write each item to the CSV file.
    for todo_list_item in todo_list_items:
        csv_writer.writerow([
            employee_id,
            todo_list_item["username"],
            todo_list_item["completed"],
            todo_list_item["title"]
        ])

    # Close the CSV file.
    csv_file.close()

# Pass employee id on command line.
employee_id = sys.argv[1]

# Export the employee's TODO list to a CSV file.
export_employee_todo_list_to_csv(employee_id)
