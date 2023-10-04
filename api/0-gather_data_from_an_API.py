"""
This script uses an API to retrieve employee task information
and display in a special format.

It retrieves employees name, task completed with their titles.
"""
import requests
import sys
def user_info(id):
    # Rest of the code for reading and printing tasks
    try:
        with open(str(id) + ".csv", 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            print("Number of tasks in CSV:", len(list(reader)))
    except FileNotFoundError:
        print(f"CSV file for user {id} not found.")

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

        tasks_list.append([employeeId, employeeName, str(data['completed']), data['title']])

    print("Employee {} is done with tasks({}/{}):".format(employeeName, completedTasks, totalTasks))

    for task in tasks_list:
        print("\t{}".format(task[3]))

    # Export data to CSV
    csv_filename = "{}.csv".format(employeeId)
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(tasks_list)

    # Print number of tasks
    user_info(employeeId)