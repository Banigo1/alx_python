import requests
import csv
import sys

def get_employee_info(employee_id):
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch employee details
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    user_id = employee_data['id']
    username = employee_data['username']

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare CSV data
    csv_data = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]

    for task in todos_data:
        task_completed_status = "completed" if task['completed'] else "not completed"
        task_title = task['title']
        csv_data.append([user_id, username, task_completed_status, task_title])

        # Display information (optional)
        print(f"Task Title: {task_title}, Completed: {task['completed']}")

    # Write to CSV file
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(csv_data)

    print(f"CSV file '{csv_filename}' created successfully.")

if __name__ == "__main__":import requests
import csv
import sys

def get_employee_info(employee_id):
    # Endpoint URLs for employee details and TODO list
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch employee details
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    user_id = employee_data['id']
    username = employee_data['username']

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare CSV data with header
    csv_data = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]

    # Iterate over tasks and populate CSV data
    for task in todos_data:
        task_completed_status = "completed" if task['completed'] else "not completed"
        task_title = task['title']
        csv_data.append([user_id, username, task_completed_status, task_title])

        # Display information (optional)
        print(f"Task Title: {task_title}, Completed: {task['completed']}")

    # Write to CSV file
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(csv_data)

    print(f"CSV file '{csv_filename}' created successfully.")

if __name__ == "__main__":
    # Check for correct command line usage
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command line argument
    employee_id = int(sys.argv[1])

    # Call the function to get employee info and export to CSV
    get_employee_info(employee_id)

    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
