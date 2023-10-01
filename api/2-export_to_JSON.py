import requests
import json
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

    # Prepare JSON data structure
    json_data = {user_id: []}

    # Iterate over tasks and populate JSON data
    for task in todos_data:
        task_completed_status = "completed" if task['completed'] else "not completed"
        task_title = task['title']
        
        task_info = {
            "task": task_title,
            "completed": task_completed_status,
            "username": username
        }

        json_data[user_id].append(task_info)

        # Display information (optional)
        print(f"Task Title: {task_title}, Completed: {task['completed']}")

    # Write to JSON file
    json_filename = f"{user_id}.json"
    with open(json_filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile, indent=2)

    print(f"JSON file '{json_filename}' created successfully.")

if __name__ == "__main__":
    # Check for correct command line usage
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command line argument
    employee_id = int(sys.argv[1])

    # Call the function to get employee info and export to JSON
    get_employee_info(employee_id)
