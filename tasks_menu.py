# Create empty list

tasks = []

# keeps menu on screen with infinit loop while True
# break this inside the if clauses

while True:
    print("\n1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. Exit")
    print("5. List all tasks" + "\n")

    option = int(input("Select an option: "))

    # option 1 - enter task and append to list.append(var)
    if option == 1:
        task = input(" enter task:  ")
        tasks.append(task)

    # option 2 - if list exists  input index to edit task
    elif option == 2:
        if tasks:
            index = int(input("Enter the task index to edit: "))
            # if index valid, input new task and tasks[index-1] -> new_task
            if 0 < index < len(tasks):
                new_task = input("Enter new task for index selected")
                tasks[index-1] = new_task
                print("Task edited successfully.")
            # else index invalid
            else:
                print("Invalid task index !!!")
        # else no task in list
        else:
            print("no tasks to edit !!!")
    # option 3 - delete task , select index, check if tasks exista, check if index ok
    elif option == 3:
        if tasks:
            index = int(input("Enter task index to delete: "))
            if 0 < index < len(tasks):
                del tasks[index-1]
                print("Task deleted successfully")
            else:
                print("Invalid task index")
        else:
            print("No tasks to delete")
    # option 4 - use break to exit program , print nice message
    elif option == 4:
        print("Exiting program. Goodbye!")
        break
    # option 5 - list tasks
    elif option == 5:
        if tasks:
            for task in tasks:
                print(task + "\n")
        else:
            print("No tasks available")
    else:
        print("Invalid option.")

