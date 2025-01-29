# main.py
from tasks import add_task, list_tasks, mark_completed, delete_task

def main():
    print("Collaborative To-Do List")
    
    # New Feature: Allow user to add a task from the command line
    task = input("Enter a new task: ")
    if task.strip():  # Ensure the task isn't empty
        add_task(task)
        print(f'Task "{task}" added successfully!')
    else:
        print("Task cannot be empty.")

if __name__ == "__main__":
    main()
