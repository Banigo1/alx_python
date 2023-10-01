import requests

def todo_list_progress(employee_id):
    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_data = requests.get(user_url).json()
    employee_name = user_data['name']

    # Fetch TODO data
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_data = requests.get(todos_url).json()

    # Calculate progress
    total_tasks = len(todos_data)
    done_tasks = len([task for task in todos_data if task['completed']])
    
    # Display progress
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    
    # Display completed tasks
    for task in todos_data:
        if task['completed']:
            print(f"\t {task['title']}")

# Test the function with an example employee ID
todo_list_progress(1)
