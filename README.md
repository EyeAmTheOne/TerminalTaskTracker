# TerminalTaskTracker

Project idea from https://roadmap.sh/projects/task-tracker

## How to use

Clone this repository and cd into it.

```bash
git clone https://github.com/EyeAmTheOne/TerminalTaskTracker.git
cd TerminalTaskTracker
```

### Commands

```bash

# Add a new task with a name and description
python task.py add "Task Name" "Task Description"

# Update a task with a new name and/or description by its unique ID
python task.py update <task_id> "New Task Name" "New Task Description"

# Delete a task by its unique ID
python task.py delete <task_id>

# Mark a task as done or in-progress
python task.py mark-in-progress <task_id>
python task.py mark-done <task_id>

# List all the tasks or filter by status
python task.py list
python task.py list done
python task.py list todo
python task.py list in-progress
```
