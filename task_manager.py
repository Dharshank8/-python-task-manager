def add_task(tasks, task):
    tasks.append(task)
    print("Task added successfully!")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available")

    else:
        for task in tasks:
            print("-", task)