class ToDoList:
    def __init__(self, filename):
        self.filename = filename

        # Create the file if it doesn't exist
        with open(self.filename, 'a'):
            pass
