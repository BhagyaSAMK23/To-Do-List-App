import json
from task_manager.task import Task

# Save tasks to a JSON file
# Used ChatGPT to learn converting tasks into dictionaries. Usage of list comprehension.
def save_tasks(task_list, filename='task_manager/tasks.json'):
    tasks_data = [{"title": task.title, "description": task.description} for task in task_list]
    
    # Write the list of dictionaries to a JSON file
    with open(filename, 'w') as f:
        json.dump(tasks_data, f, indent=4) 
    
    print(f"Tasks have been saved to {filename}.")
    

def load_tasks(filename='task_manager/tasks.json'):
    try:
        with open(filename, 'r') as f:
            tasks_data = json.load(f)

        # Convert the loaded data into Task objects
        return [Task(task['title'], task['description']) for task in tasks_data]

    except FileNotFoundError:
        print(f"{filename} not found. Returning an empty task list.")
        return []  

  