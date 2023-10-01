    """
    This module would create a CSV file called 1.csv in the current directory,
    containing the employee's TODO list items.
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
    employeeName = profileJson_Data['name']

    # Count total and completed tasks
    totalTasks = 0
    completedTasks = 0

    for data in todoJson_Data: # Each dict in variable data
        for key, value in data.items():
            if key == 'completed':
                totalTasks += 1
                if value == True:
                    completedTasks += 1

    print("Employee {} is done with "
          "tasks({}/{}):".format(employeeName, completedTasks, totalTasks))

    # Retrieve title of completed tasks and write to CSV file
    with open('{}.csv'.format(id), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for data in todoJson_Data: # Each dict in variable data
            for key, value in data.items():
                if key == 'completed' and value == True:
                    writer.writerow([id, employeeName, value, data['title']])
                    print("\t {}".format(data['title']))
