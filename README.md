# Command-Line To-Do List App
- The Command-Line To-Do List App is a simple Python program that allows users to manage their tasks from the command-line interface (CLI). With this app, users can add, update, delete, and display tasks, all within the terminal or command prompt.

## Features

- Add new tasks with a title, description, and initial status (incomplete).
- Update existing tasks by modifying their title, description, and status.
- Delete tasks to remove them from the list.
- Display all tasks in a clear and organized manner, separated by lines.

## Prerequisites

- [Python 3.x](https://www.python.org/downloads/) installed on your computer.

## Getting Started

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Akshayknchalapalli/command-line-todo.git
   cd command-line-todo

2. Run the command-line To-Do List app:

        python command_line_todo.py

3. Follow the on-screen instructions to interact with the app.

## Usage
The app provides a menu of options to perform various actions on the To-Do List:

- Add Task: Add a new task by providing the title and description.
- Delete Task: Remove a task from the list by selecting its index.
- Update Task: Modify the title, description, and status of an existing task.
- Display Tasks: View all tasks in the To-Do List.

## Example
            ===== To-Do List =====
            1. Complete assignment - Finish the project (Status: in-progress)
            --------------------------
            2. Buy groceries - Get milk and bread (Status: incomplete)
            --------------------------
            3. Pay bills - Electricity and internet (Status: completed)
            --------------------------
            4. Clean the house - Vacuum and dusting (Status: incomplete)
            --------------------------
            5. Submit reports - Send weekly status (Status: in-progress)
            --------------------------
            
            1. Add Task
            2. Delete Task
            3. Update Task
            4. Display Tasks
            5. Exit
            
            Enter your choice: 3
            
            ===== To-Do List =====
            1. Complete assignment - Finish the project (Status: in-progress)
            --------------------------
            2. Buy groceries - Get milk and bread (Status: incomplete)
            --------------------------
            3. Pay bills - Electricity and internet (Status: completed)
            --------------------------
            4. Clean the house - Vacuum and dusting (Status: incomplete)
            --------------------------
            5. Submit reports - Send weekly status (Status: in-progress)
            --------------------------

            Enter task index to update: 2
            Enter new task title: Buy groceries
            Enter new task description: Get milk, bread, and eggs
            Enter new task status: in-progress
            
            ===== To-Do List =====
            1. Complete assignment - Finish the project (Status: in-progress)
            --------------------------
            2. Buy groceries - Get milk, bread, and eggs (Status: in-progress)
            --------------------------
            3. Pay bills - Electricity and internet (Status: completed)
            --------------------------
            4. Clean the house - Vacuum and dusting (Status: incomplete)
            --------------------------
            5. Submit reports - Send weekly status (Status: in-progress)
            --------------------------
            
            1. Add Task
            2. Delete Task
            3. Update Task
            4. Display Tasks
            5. Exit
            
            Enter your choice: 5

## Contributing
- Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License
- This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- The inspiration for this project comes from the desire to create a simple command-line To-Do List app for personal use.

**Enjoy managing your tasks with the Command-Line To-Do List App! Happy coding! 😄**
