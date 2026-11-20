def add_task(tasks, task):
    tasks.append(task)
    print("Task added successfully!")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available")

    else:
        for task in tasks:
            print("-", task)

def delete_task(tasks, task_number):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' deleted successfully!")
    else:
        print("Invalid task number!")

def count_tasks(tasks):
    print(f"Total tasks: {len(tasks)}")
