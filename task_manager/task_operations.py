from task_manager.task import Task

# Add a task to the task list
def add_task(task_list, title, description):
    new_task = Task(title, description)
    task_list.append(new_task)
    print(f"Task '{title}' added successfully!")
    return task_list

# Remove a task from the task list by title
def remove_task(task_list, title):
    task_list_copy = [task for task in task_list if task.title != title]
    if len(task_list_copy) == len(task_list):
        print(f"No task with title '{title}' found.")
    else:
        print(f"Task '{title}' removed successfully!")
    return task_list_copy


# List all tasks
def list_tasks(task_list):
    if not task_list:
        print("No tasks available.")
    else:
        for task in task_list:
            print(f"{task.title} - {task.description}")


