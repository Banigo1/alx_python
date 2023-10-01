import requests

def get_employee_todo_list_progress(employee_id):
    """Returns information about an employee's TODO list progress, given the employee ID."""

    # Get the employee details
    employee_details_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    employee_details_response = requests.get(employee_details_url)
    employee_details = employee_details_response.json()

    # Get the employee's TODO list items
    todo_list_items_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    todo_list_items_response = requests.get(todo_list_items_url)
    todo_list_items = todo_list_items_response.json()

    # Count the number of completed and non-completed tasks
    completed_tasks = 0
    non_completed_tasks = 0
    for todo_list_item in todo_list_items:
        if todo_list_item["completed"]:
            completed_tasks += 1
        else:
            non_completed_tasks += 1

    # Calculate the TODO list progress percentage
    todo_list_progress = completed_tasks / (completed_tasks + non_completed_tasks)

    # Format the TODO list progress output
    employee_name = employee_details["name"]
    todo_list_progress_string = "Employee {} is done with {} tasks ({}/{}):".format(
        employee_name,
        completed_tasks,
        todo_list_progress,
        (completed_tasks + non_completed_tasks)
    )

    completed_task_titles = []
    for todo_list_item in todo_list_items:
        if todo_list_item["completed"]:
            completed_task_titles.append(todo_list_item["title"])

    completed_task_titles_string = "\n".join(["\t\t{}".format(task_title) for task_title in completed_task_titles])

    return todo_list_progress_string + completed_task_titles_string

# Get the employee TODO list progress from the user-specified employee ID
employee_id = int(input("Enter the employee ID: "))
todo_list_progress = get_employee_todo_list_progress(employee_id)

# Print the employee TODO list progress to the standard output
print(todo_list_progress)
