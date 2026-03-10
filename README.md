# Task Tracker CLI

A lightweight command-line tool to manage your tasks — add, update, delete, and track progress, all stored locally in a JSON file.

---

## Requirements

- Python 3.10+

No external dependencies required.

---

## Setup

**Clone or download the project, then navigate to the folder:**

```bash
cd task-tracker
```

**Optional: Create a shortcut so you don't have to type `python3 main.py` every time:**

```bash
echo 'alias task="python3 /ABSOLUTE/PATH/TO/main.py"' >> ~/.zshrc
source ~/.zshrc
```

Replace `/ABSOLUTE/PATH/TO/main.py` with the actual path (use `pwd` inside the project folder to find it).

---

## Usage

```bash
python3 main.py <command> [arguments]
# or with alias:
task <command> [arguments]
```

---

## Commands

### Add a task
```bash
task add "Buy groceries"
# Task added successfully. (ID: 1)
```

### Update a task
```bash
task update <id> "New description"
task update 1 "Buy groceries and cook dinner"
```

### Delete a task
```bash
task delete <id>
task delete 1
```

### Mark as in-progress
```bash
task mark in-progress <id>
task mark in-progress 1
```

### Mark as done
```bash
task mark done <id>
task mark done 1
```

### List tasks
```bash
task list                  # All tasks
task list todo             # Only tasks with status "todo"
task list in-progress      # Only tasks currently in progress
task list done             # Only completed tasks
```

---

## Task Status

| Status        | Description                  |
|---------------|------------------------------|
| `todo`        | Newly created task (default) |
| `in-progress` | Task currently being worked on |
| `done`        | Completed task               |

---

## Data Storage

Tasks are saved automatically in a `tasks.json` file in the same directory as `main.py`. The file is created on first use and updated after every command.

Example `tasks.json`:
```json
[
    {
        "id": 1,
        "description": "Buy groceries",
        "created_at": "2026-03-10 14:00:00",
        "updated_at": "2026-03-10 15:30:00",
        "status": "done"
    }
]
```

---

## Project Structure

```
task-tracker/
├── main.py       # CLI entry point and all task logic
└── tasks.json    # Auto-generated task storage (created on first use)
```
