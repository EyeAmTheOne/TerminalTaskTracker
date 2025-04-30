import argparse
from ToDoList import ToDoList

def main():
    args = retrieve_command()
    l = ToDoList("data.json")
    read_command(args, l)

def read_command(args, list):
    match args.command:
        case "add":
            print(f"Adding task: {args.task_name}")
            list.add_task(args.task_name, args.description)
        case "update":
            print("Updating task")
        case "delete":
            print("Deleting task")
        case "mark-in-progress":
            print("Marking task as in progress")
        case "mark-done":
            print("Marking task as done")
        case "list":
            print("Listing all tasks")
        case _:
            print("Unknown command")

def retrieve_command():
    # Capture a command-line argument and print it out to the console
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for add command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("task_name", type=str, help="Name of the task to add")
    parser_add.add_argument("description", nargs="?", type=str, default="", help="A short description of the task")

    # Subparser for update command
    parser_update = subparsers.add_parser("update", help="Update an existing task")
    parser_update.add_argument("id", type=int, help="ID of the task to update")
    parser_update.add_argument("task_name", type=str, help="New name of the task")

    # Subparser for delete command
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="ID of the task to delete")

    # Subparser for mark-in-progress command
    parser_mark_in_progress = subparsers.add_parser("mark-in-progress", help="Mark a task as in progress")
    parser_mark_in_progress.add_argument("id", type=int, help="ID of the task to mark in progress")

    # Subparser for mark-done command
    parser_mark_done = subparsers.add_parser("mark-done", help="Mark a task as done")
    parser_mark_done.add_argument("id", type=int, help="ID of the task to mark as done")

    # Subparser for list command, can run list on its own, or add extra arguments
    parser_list = subparsers.add_parser("list", help="List tasks")
    parser_list.add_argument("status", nargs="?", choices=["todo", "done", "in-progress"], default="todo", help="List all tasks")

    return parser.parse_args()

if __name__ == "__main__":
    main()
