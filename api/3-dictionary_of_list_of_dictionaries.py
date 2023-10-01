import requests
import json

def todo_list_progress():
    # Fetch all user data
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_data = requests.get(users_url).json()

    all_users_tasks = {}

    for user_data in users_data:
        employee_id = user_data['id']
        username = user_data['username']

        # Fetch TODO data
        todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        todos_data = requests.get(todos_url).json()

        # Prepare data for JSON export
        tasks = []
        
        for task in todos_data:
            tasks.append({"username": username, "task": task['title'], "completed": task['completed']})
        
        all_users_tasks[employee_id] = tasks

    # Write to JSON file
    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_users_tasks, file)

# Test the function
todo_list_progress()
