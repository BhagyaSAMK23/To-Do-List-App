from task_manager import Task, add_task, list_tasks, remove_task, save_tasks, load_tasks

def display_menu():
    print("\nTo-Do List Menu")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Remove a task")
    print("4. Save tasks")
    print("5. Load tasks")
    print("6. Exit")

def main():
    task_list = []
    while True:
        display_menu()
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            list_tasks(task_list)
        
        elif choice == "2":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(task_list, title, description)
        
        elif choice == "3":
            title = input("Enter task title to remove: ")
            task_list = remove_task(task_list, title)
            save_tasks(task_list)
        
        elif choice == "4":
            save_tasks(task_list)
            
       # Used ChatGPT to debug why option 5 wasn't displaying tasks.  
       # It suggested adding `list_tasks(task_list)` after loading, which resolved the issue.      
        elif choice == "5":
            task_list = load_tasks()
            list_tasks(task_list)   
            
        elif choice == "6":
            print("Exiting... Bye! Have a nice day!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
