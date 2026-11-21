
from task_manager import add_task, view_tasks, count_completed_tasks

print("================================")
print("       PYTHON TASK MANAGER")
print("================================")

tasks = []
completed_tasks = []

while True:

    

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    print("4. View Completed Task Count")

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
    elif choice == "4":
       count_completed_tasks(completed_tasks)

    else:
        print("Invalid choice!")
