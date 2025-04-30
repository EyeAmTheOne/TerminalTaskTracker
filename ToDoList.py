import json

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

    def add_task(self, name):
        """Add new task to the list."""
        data = self.load_data()
        task = { "id": data["next_id"], "name": name, "status": "todo" }
        data["tasks"].append(task)
        data["next_id"] += 1
        self.save_data(data)


