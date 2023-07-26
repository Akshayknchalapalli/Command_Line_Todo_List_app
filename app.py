# command_line_todo.py

tasks = []

def add_task(title, description):
    tasks.append({'title': title, 'description': description, 'status': 'incomplete'})

def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]

def update_task(task_index, title, description, status):
    if 0 <= task_index < len(tasks):
        tasks[task_index] = {'title': title, 'description': description, 'status': status}

def display_tasks():
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['title']} - {task['description']} (Status: {task['status']})")

def main():
    while True:
        print("===== To-Do List =====")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Update Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == '2':
            display_tasks()
            task_index = int(input("Enter task index to delete: ")) - 1
            delete_task(task_index)
        elif choice == '3':
            display_tasks()
            task_index = int(input("Enter task index to update: ")) - 1
            title = input("Enter new task title: ")
            description = input("Enter new task description: ")
            status = input("Enter new task status: ")
            update_task(task_index, title, description, status)
        elif choice == '4':
            display_tasks()
            print("--------------------------------------------")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
