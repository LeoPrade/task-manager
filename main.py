import json
import sys
from pathlib import Path
import datetime

p = Path("tasks.json") 

tasks: list = []

def main():
    if len(sys.argv) < 2:
        print("Bitte einen Befehl eingeben!")
        return

    if p.exists():
        with open("tasks.json", "r") as f:
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
    else:
        pass


class Task:
    def __init__(self, id, description, created_at, updated_at):
        self.id = id
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.status = "todo"

def add_task():
    eingabe = " ".join(sys.argv[2:])
    
    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = max(task["id"] for task in tasks) + 1
    created_at = str(datetime.datetime.now())
    updated_at = str(datetime.datetime.now())
    new_task = Task(new_id, eingabe, created_at, updated_at)

    tasks.append(new_task.__dict__)
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def update_task(update_id):
    update = " ".join(sys.argv[3:])
    
    task_index = None
    for i, task in enumerate(tasks):
        if task["id"] == update_id:
            task_index = i
    if task_index is None:
        print("Task was not found.")
        return 

    updated_task = Task(update_id, update, tasks[task_index]["created_at"], str(datetime.datetime.now()))
    tasks[task_index] = updated_task.__dict__
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def delete_task(delete_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != delete_id]
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def mark_in_progress(progress_id):
    task_index = None
    for i, task in enumerate(tasks):
        if task["id"] == progress_id:
            task_index = i
            task["status"] = "in-progress"
    if task_index is None:
        print("Task was not found.")
        return 
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def mark_done(done_id):
    task_index = None
    for i, task in enumerate(tasks):
        if task["id"] == done_id:
            task_index = i
            task["status"] = "done"
    if task_index is None:
        print("Task was not found.")
        return 
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def list_all_tasks():
    for task in tasks:
        print(task["description"])

def list_completed_tasks():
    for task in tasks:
        if task["status"] == "done":
            print(task["description"])

def list_pending_tasks():
    for task in tasks:
        if task["status"] == "in-progress":
            print(task["description"])

def list_undone_tasks():
    for task in tasks:
        if task["status"] == "todo":
            print(task["description"])


if __name__ == "__main__":
    main()