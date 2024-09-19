class ToDoApp:
    def __init__(self):
        self.tasks = {}

    def show_menu(self):
        print("\n==== To-Do List Menu ====")
        print("1. Add a task")
        print("2. Update a task")
        print("3. Delete a task")
        print("4. View all tasks")
        print("5. Mark task as complete")
        print("6. Exit")

    def add_task(self):
        task_name = input("Enter the task: ")
        task_status = "Pending"
        self.tasks[task_name] = task_status
        print(f"Task '{task_name}' added.")

    def update_task(self):
        task_name = input("Enter the task name you want to update: ")
        if task_name in self.tasks:
            new_name = input("Enter the new task name: ")
            self.tasks[new_name] = self.tasks.pop(task_name)
            print(f"Task '{task_name}' updated to '{new_name}'.")
        else:
            print("Task not found.")

    def delete_task(self):
        task_name = input("Enter the task name to delete: ")
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f"Task '{task_name}' deleted.")
        else:
            print("Task not found.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("\n==== To-Do List ====")
            for task_name, status in self.tasks.items():
                print(f"{task_name} - {status}")

    def mark_complete(self):
        task_name = input("Enter the task name to mark as complete: ")
        if task_name in self.tasks:
            self.tasks[task_name] = "Complete"
            print(f"Task '{task_name}' marked as complete.")
        else:
            print("Task not found.")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option (1-6): ")

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.update_task()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                self.view_tasks()
            elif choice == '5':
                self.mark_complete()
            elif choice == '6':
                print("Exiting the application.")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    app = ToDoApp()
    app.run()

