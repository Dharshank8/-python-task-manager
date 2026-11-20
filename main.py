
print("================================")
print("       PYTHON TASK MANAGER")
print("================================")

tasks = []

while True:

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        task = input("Enter task name: ")
        tasks.append(task)

        print("Task added successfully!")

    elif choice == "2":

        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks available")

        else:
            for task in tasks:
                print("-", task)

    elif choice == "3":

        print("Exiting application...")
        break

    else:
        print("Invalid choice!")
