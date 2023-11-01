tasks = []

while True:
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    print("\nOptions:")
    print("1. Add task")
    print("2. Remove task")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
    elif choice == "2":
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
