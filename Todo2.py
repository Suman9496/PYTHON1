class TodoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task, priority):
        self.tasks[task] = priority

    def remove_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
        else:
            print(f"Task '{task}' not found.")

    def display_tasks(self):
        print("Todo List:")
        for task, priority in sorted(self.tasks.items(), key=lambda x: x[1]):
            print(f"Priority {priority}: {task}")

# Create a TodoList instance
todo_list = TodoList()

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task: ")
        priority = int(input("Enter the priority (1-5): "))
        todo_list.add_task(task, priority)

    elif choice == '2':
        task = input("Enter the task to remove: ")
        todo_list.remove_task(task)

    elif choice == '3':
        todo_list.display_tasks()

    elif choice == '4':
        print("Exiting the Todo List Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
