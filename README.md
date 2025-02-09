# To-Do-List-App
Modularized To-Do List Application

## Project Structure

```
todo_app/
│── main.py                    # Main entry point
│── task_manager/
│   ├── __init__.py             # Makes task_manager a package
│   ├── task.py                 # Task class definition
│   ├── task_storage.py         # Handles saving/loading tasks
│   ├── task_operations.py      # Contains functions for task management
```

## Features

- View all tasks
- Add a new task
- Remove a task
- Save tasks to a JSON file
- Load tasks from a JSON file

## Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
```

### 2. Run the Program
Make sure Python is installed, then run:
```bash
python main.py
```

### 3. Follow the Menu
```
To-Do List Menu
1. View all tasks
2. Add a new task
3. Remove a task
4. Save tasks
5. Load tasks
6. Exit
```

## Notes
- Tasks are stored in `tasks.json`.
- Deleting a task requires saving the updated list.
- If `tasks.json` doesn't exist, it will be created automatically.

## License
This project is open-source and free to use.
