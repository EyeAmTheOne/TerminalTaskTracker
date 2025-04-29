import json

class ToDoList:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}

        # Create the file if it doesn't exist
        with open(self.filename, 'a'):
            pass

        # Load data from json file to parameter
        self.load_data()

    def load_data(self):
        """Load data from the JSON file."""
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = {}

    def save_data(self):
        """Save data to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    # def add_task(self, name):
    #     """Add new task to the list."""
    #    if name in self.data: 


