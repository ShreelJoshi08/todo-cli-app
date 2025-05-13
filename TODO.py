import json
import os

TASK_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(title, description=""):
    tasks = load_tasks()
    task = {
        "title": title,
        "description": description,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "" if task['completed'] else "w"
        print(f"{idx}. {task['title']} - {status}")
        if task['description']:
            print(f"   📝 {task['description']}")

# Mark a task as completed
def mark_completed(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        save_tasks(tasks)
        print("🎉 Task marked as completed!")
    else:
        print(" Invalid task number.")
# Delete a task
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        deleted = tasks.pop(index)
        save_tasks(tasks)
        print(f" Deleted task: {deleted['title']}")
    else:
        print(" Invalid task number.")

# Main menu
def menu():
    while True:
        print("\n--- To-Do List App ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            add_task(title, description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            try:
                index = int(input("Enter task number to mark as completed: ")) - 1
                mark_completed(index)
            except ValueError:
                print(" Invalid input.")
        elif choice == '4':
            view_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(index)
            except ValueError:
                print(" Invalid input.")
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print(" Please choose a valid option.")

if __name__ == '__main__':
    menu()
