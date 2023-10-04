"""
Employee Task Information Retrieval and CSV Export Script

This script retrieves task information for a specified employee using an API
and exports the data in CSV format.

Usage:
    python script_name.py employee_id

APIs:
    - User Todo URL: https://jsonplaceholder.typicode.com/users/{employee_id}/todos
    - User Profile URL: https://jsonplaceholder.typicode.com/users/{employee_id}

Dependencies:
    - requests
    - csv

Script Execution:
    - The script should be executed from the command line with the employee_id as an argument.

Output:
    - Prints the employee's task completion status and titles.
    - Exports data to a CSV file named USER_ID.csv.

CSV Format:
    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

Example:
    python script_name.py 1

"""

import csv
import requests
import sys

# No execution of this file when imported
if __name__ == "__main__":
    
    # Pass employee id on command line
    id = sys.argv[1]

    # APIs 
    userTodoURL = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    userProfile = "https://jsonplaceholder.typicode.com/users/{}".format(id)

    # Make requests on APIs
    todoResponse = requests.get(userTodoURL)
    profileResponse = requests.get(userProfile)

    # Parse responses and store in variables
    todoJson_Data = todoResponse.json()
    profileJson_Data = profileResponse.json()

    # Get employee information
    employeeId = profileJson_Data['id']
    employeeName = profileJson_Data['username']

    # Count total and completed tasks
    totalTasks = 0
    completedTasks = 0

    # List to store task details
    tasks_list = []

    for data in todoJson_Data:
        for key, value in data.items():
            if key == 'completed':
                totalTasks += 1
                if value == True:
                    completedTasks += 1

        # Append task details to the list
        tasks_list.append([employeeId, employeeName, str(data['completed']), data['title']])

    print("Employee {} is done with tasks({}/{}):".format(employeeName, completedTasks, totalTasks))

    # Print tasks
    for task in tasks_list:
        print("\t{}".format(task[3]))

    # Export data to CSV
    csv_filename = "{}.csv".format(employeeId)
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        # Write tasks data
        csv_writer.writerows(tasks_list)

    print("Data exported to {}".format(csv_filename))