import requests
import csv
import sys

def get_employee_info(employee_id):
    """Get employee details from the API."""
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    response.raise_for_status()  # Raise an exception for bad responses.
    return response.json()

def get_todo_list(employee_id):
    """Get employee's TODO list from the API."""
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)
    response.raise_for_status()  # Raise an exception for bad responses.
    return response.json()

def display_todo_progress(employee_id):
    """Display TODO list progress for a given employee."""
    try:
        # Get employee details
        employee_info = get_employee_info(employee_id)
        employee_name = employee_info["name"]

        # Get TODO list
        todo_list = get_todo_list(employee_id)

        # Count completed and total tasks
        completed_tasks = sum(1 for task in todo_list if task["completed"])
        total_tasks = len(todo_list)

        # Display output
        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

        # Display titles of completed tasks
        for task in todo_list:
            if task["completed"]:
                print(f"\t{task['title']}")

        # Export TODO list to CSV
        export_todo_list_to_csv(employee_id, employee_info, todo_list)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching information: {e}")

def export_todo_list_to_csv(employee_id, employee_info, todo_list):
    """Export TODO list to a CSV file."""
    try:
        # Open a CSV file for writing.
        csv_file_path = f"{employee_id}.csv"
        with open(csv_file_path, "w", newline="") as csv_file:
            # Create a CSV writer object.
            csv_writer = csv.writer(csv_file)

            # Write the header row to the CSV file.
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            # Write TODO list items to the CSV file.
            for task in todo_list:
                csv_writer.writerow([
                    employee_id,
                    employee_info["username"],
                    task["completed"],
                    task["title"]
                ])

        print(f"TODO list for employee {employee_id} exported to {csv_file_path}.")

    except IOError as e:
        print(f"Error exporting TODO list to CSV: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    display_todo_progress(employee_id)
