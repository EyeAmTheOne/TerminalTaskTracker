import json
from datetime import datetime

class ToDoList:
    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        """Load data from the JSON file."""
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"next_id": 1, "tasks": []}
        return data

    def save_data(self, data):
        """Save data to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def add_task(self, name, description=""):
        """Add new task to the list."""
        data = self.load_data()
        create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task = { "id": data["next_id"], "name": name, "status": "todo", "description": description, "createdAt": create_time, "updatedAt": None }
        data["tasks"].append(task)
        data["next_id"] += 1
        self.save_data(data)

    def list_tasks(self, status=""):
        """Returns list of tasks with a specified status. Each task is triple of (id, name, description)."""
        data = self.load_data()
        if not status:
            tasks = [(task["id"], task["name"], task["description"]) for task in data["tasks"]]
        else:
            tasks = [(task["id"], task["name"], task["description"]) for task in data["tasks"] if task["status"] == status]
        return tasks

    def mark_task(self, id, status):
        """Mark task with the provided status"""
        data = self.load_data()
        found = False
        for task in data["tasks"]:
            if task["id"] == id:
                task["status"] = status
                found = True
                break
        
        # ID not found
        if not found:
            raise ValueError(f"Task with id {id} not found")
        self.save_data(data)

    def delete_task(self, id):
        """Delete task with a specified id."""
        data = self.load_data()
        found = False
        l = []
        for task in data["tasks"]:
            if task["id"] == id:
                found = True
            else:
                l.append(task)
        data["tasks"] = l

        # ID not found
        if not found:
            raise ValueError(f"Task with id {id} not found")
        self.save_data(data)

    def update_task(self, id, name, description=""):
        """Update task with a specified id."""
        data = self.load_data()
        found = False
        for task in data["tasks"]:
            if task["id"] == id:
                task["name"] = name
                task["description"] = description
                task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                found = True
                break

        # ID not found
        if not found:
            raise ValueError(f"Task with id {id} not found")
        self.save_data(data)
