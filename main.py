import json
import sys
from pathlib import Path
import datetime
from typing import Any

FILE_NAME = "tasks.json"
p = Path(FILE_NAME) 

tasks: list[dict[str, Any]] = []

def main():
    if len(sys.argv) < 2:
        print("Please provide a command: add, update, delete, mark, list")
        return

    if p.exists():
        with open(FILE_NAME, "r") as f:
            tasks.extend(json.load(f))

    if sys.argv[1] == "add":
        add_task()
    elif sys.argv[1] == "update":
        update_task(int(sys.argv[2]))
    elif sys.argv[1] == "delete":
        delete_task(int(sys.argv[2]))
    elif sys.argv[1] == "mark":
        if sys.argv[2] == "in-progress":
            mark_in_progress(int(sys.argv[3]))
        elif sys.argv[2] == "done":
            mark_done(int(sys.argv[3]))
        else:
            print("Invalid input for mark command. Use 'in-progress' or 'done'.")
    elif sys.argv[1] == "list":
        if len(sys.argv) < 3:
            list_all_tasks()
        elif sys.argv[2] == "done":
            list_completed_tasks()
        elif sys.argv[2] == "in-progress":
            list_pending_tasks()
        elif sys.argv[2] == "todo":
            list_undone_tasks()
        else: 
            print("Invalid input for list command. Use 'done', 'in-progress', 'todo' or leave empty for all tasks.")


class Task:
    def __init__(self, id: int, description: str, created_at: str, updated_at: str):
        self.id = id
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.status = "todo"

def load_tasks() -> None:
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def print_task(task: dict) -> None:
    print(f"{task['description']} (ID: {task['id']}, Status: {task['status']})")

def add_task() -> None:
    """
    Add a new task to the tasks list.
    
    Syntax: add <task description>
    """

    if len(sys.argv) < 3:
        print("Please provide a task description.")
        return
    eingabe: str = " ".join(sys.argv[2:])
    
    if len(tasks) == 0:
        new_id: int = 1
    else:
        new_id: int = max(task["id"] for task in tasks) + 1
    created_at: str = str(datetime.datetime.now())
    updated_at: str = str(datetime.datetime.now())
    new_task: Task = Task(new_id, eingabe, created_at, updated_at)

    tasks.append(new_task.__dict__)
    print(f"Task added succesfully. (ID: {new_id})")
    load_tasks()

def update_task(update_id: int) -> None:
    """
    Update a existing task in the tasks list.
    
    Syntax: update <task id> <task description>
    """

    if len(sys.argv) < 4:
        print("Please provide a task description.")
        return
    update: str = " ".join(sys.argv[3:])
    
    task_index: int | None = None
    for i, task in enumerate(tasks):
        if task["id"] == update_id:
            task_index = i
    if task_index is None:
        print("Task was not found.")
        return 

    updated_task: Task = Task(update_id, update, tasks[task_index]["created_at"], str(datetime.datetime.now()))
    tasks[task_index] = updated_task.__dict__
    load_tasks()

def delete_task(delete_id: int) -> None:
    """
    Remove a existing task from the tasks list.
    
    Syntax: delete <task id>
    """

    if len(sys.argv) < 3:
        print("Please provide a task ID.")
        return
    global tasks
    tasks = [task for task in tasks if task["id"] != delete_id]
    load_tasks()

def mark_in_progress(progress_id: int) -> None:
    """
    Mark the status of a task as "in-progress".
    
    Syntax: mark in-progress <task id>
    """
    
    if len(sys.argv) < 4:
        print("Please provide a task ID.")
        return
    task_index: int | None = None
    for i, task in enumerate(tasks):
        if task["id"] == progress_id:
            task_index = i
            task["status"] = "in-progress"
    if task_index is None:
        print("Task was not found.")
        return 
    load_tasks()

def mark_done(done_id: int) -> None:
    """
    Mark the status of a task as "done".
    
    Syntax: mark done <task id>
    """

    if len(sys.argv) < 4:
        print("Please provide a task ID.")
        return
    task_index: int | None = None
    for i, task in enumerate(tasks):
        if task["id"] == done_id:
            task_index = i
            task["status"] = "done"
    if task_index is None:
        print("Task was not found.")
        return 
    load_tasks()

def list_all_tasks() -> None:
    for task in tasks:
        print_task(task)

def list_completed_tasks() -> None:
    for task in tasks:
        if task["status"] == "done":
            print_task(task)

def list_pending_tasks() -> None:
    for task in tasks:
        if task["status"] == "in-progress":
            print_task(task)

def list_undone_tasks() -> None:
    for task in tasks:
        if task["status"] == "todo":
            print_task(task)


if __name__ == "__main__":
    main()