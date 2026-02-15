from todo_app.store import TaskStore


def display_menu():
    """Display the main menu options."""
    print("\n=== TODO CLI ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete")
    print("6. Exit")


def add_task(store):
    """Handle adding a new task."""
    desc = input("Task Description: ")
    task = store.add_task(desc)
    print(f"Added: {task}")


def view_tasks(store):
    """Handle viewing all tasks."""
    tasks = store.list_tasks()
    if tasks:
        for t in tasks:
            print(t)
    else:
        print("No tasks found.")


def update_task(store):
    """Handle updating an existing task."""
    try:
        task_id = int(input("Enter Task ID to Update: "))
        new_desc = input("New Description: ")
        updated = store.update_task(task_id, new_desc)
        if updated:
            print("Task Updated.")
        else:
            print("Task Not Found.")
    except ValueError:
        print("Invalid Task ID. Please enter a number.")


def delete_task(store):
    """Handle deleting a task."""
    try:
        task_id = int(input("Enter Task ID to Delete: "))
        deleted = store.delete_task(task_id)
        if deleted:
            print("Task Deleted.")
        else:
            print("Task Not Found.")
    except ValueError:
        print("Invalid Task ID. Please enter a number.")


def mark_complete(store):
    """Handle marking a task as complete."""
    try:
        task_id = int(input("Enter Task ID to Mark Complete: "))
        task = store.get_task(task_id)
        if task:
            task.is_completed = True
            print("Task marked as complete.")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid Task ID. Please enter a number.")


def main():
    """Main application loop."""
    store = TaskStore()

    while True:
        display_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_task(store)
        elif choice == "2":
            view_tasks(store)
        elif choice == "3":
            update_task(store)
        elif choice == "4":
            delete_task(store)
        elif choice == "5":
            mark_complete(store)
        elif choice == "6":
            print("GoodByeee!!!")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
