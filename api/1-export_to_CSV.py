import requests
import csv
import sys

def export_employee_todo_list_to_csv(employee_id):
    """Exports the employee's TODO list to a CSV file."""
    try:
        # Get the employee's TODO list items.
        todo_list_items_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        todo_list_items_response = requests.get(todo_list_items_url)
        todo_list_items_response.raise_for_status()  # Raise an exception for bad responses.
        todo_list_items = todo_list_items_response.json()

        # Open a CSV file for writing.
        csv_file_path = f"{employee_id}.csv"
        with open(csv_file_path, "w", newline="") as csv_file:
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

        print(f"TODO list for employee {employee_id} exported to {csv_file_path}.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching TODO list for employee {employee_id}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    export_employee_todo_list_to_csv(employee_id)
