import json

# Initialize a list to hold the tasks
tasks = []

# Load tasks from file if available
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Add task with unique ID and description
def add_task(description):
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "description": description, "status": "pending"})
    save_tasks()
    print(f"Task {task_id} added.")

# View all tasks
def view_tasks():
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

# Remove task by ID
def remove_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks()
    print(f"Task {task_id} removed.")

# Mark a task as completed by ID
def mark_completed(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = "completed"
            save_tasks()
            print(f"Task {task_id} marked as completed.")
            return
    print("Task not found.")

# Edit a task description by ID
def edit_task(task_id, new_description):
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            save_tasks()
            print(f"Task {task_id} updated.")
            return
    print("Task not found.")

# Search tasks by keyword
def search_task(keyword):
    for task in tasks:
        if keyword.lower() in task['description'].lower():
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

# Filter tasks by status (pending/completed)
def filter_tasks(status):
    for task in tasks:
        if task['status'] == status:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

# Clear all tasks with confirmation
def clear_tasks():
    confirmation = input("Are you sure you want to clear all tasks? (yes/no): ")
    if confirmation.lower() == "yes":
        tasks.clear()
        save_tasks()
        print("All tasks cleared.")

# Sort tasks by ID or status
def sort_tasks(by="id"):
    if by == "status":
        sorted_tasks = sorted(tasks, key=lambda task: task["status"])
    else:
        sorted_tasks = sorted(tasks, key=lambda task: task["id"])
    for task in sorted_tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

# Main function to handle user input
def main():
    global tasks
    tasks = load_tasks()
    
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark as Completed")
        print("5. Edit Task")
        print("6. Search Task")
        print("7. Filter Tasks")
        print("8. Clear All Tasks")
        print("9. Sort Tasks")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Enter task description: ")
            add_task(desc)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to remove: "))
            remove_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_completed(task_id)
        elif choice == "5":
            task_id = int(input("Enter task ID to edit: "))
            desc = input("Enter new description: ")
            edit_task(task_id, desc)
        elif choice == "6":
            keyword = input("Enter keyword to search: ")
            search_task(keyword)
        elif choice == "7":
            status = input("Enter status to filter (pending/completed): ")
            filter_tasks(status)
        elif choice == "8":
            clear_tasks()
        elif choice == "9":
            sort_by = input("Sort by (id/status): ")
            sort_tasks(sort_by)
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
