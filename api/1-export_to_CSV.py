import csv
import requests
import sys

def export_employee_todo_list_to_csv(employee_id):
    """Exports the employee's TODO list to a CSV file.

    Args:
        employee_id (int): The ID of the employee whose TODO list is to be exported.

    Raises:
        requests.exceptions.RequestException: An error occurred while making the HTTP request.
    """

    try:
        # Get the employee's TODO list items.
        todo_list_items_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
        todo_list_items_response = requests.get(todo_list_items_url)
        todo_list_items_response.raise_for_status()  # Raise an exception for bad responses.
        todo_list_items = todo_list_items_response.json()

        # Open a CSV file for writing.
        csv_file = open(f"{employee_id}.csv", "w", newline="")  # newline parameter for cross-platform compatibility.

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

        print(f"TODO list for employee {employee_id} exported to {employee_id}.csv.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching TODO list for employee {employee_id}: {e}")

if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument.
    if len(sys.argv) < 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command-line arguments.
    employee_id = int(sys.argv[1])

    # Export the employee's TODO list to a CSV file.
    export_employee_todo_list_to_csv(employee_id)
