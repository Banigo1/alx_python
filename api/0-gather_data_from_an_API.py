import requests
import sys

def get_employee_info(employee_id):
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch employee details
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    num_done_tasks = len(done_tasks)

    # Display information
    print(f"Employee {employee_name} is done with tasks ({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
