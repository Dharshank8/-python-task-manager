
from task_manager import add_task, view_tasks

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

        task = input("Enter task name: ").strip()

        if task:
            add_task(tasks, task)
        else:
            print("Task name cannot be empty!")

    elif choice == "2":

        print("\nYour Tasks:")
        view_tasks(tasks)

    elif choice == "3":

        print("Exiting application...")
        break

    else:
        print("Invalid choice!")
