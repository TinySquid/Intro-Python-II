class Room:
    def __init__(self, name, description, items=None):
        # Basic room info
        self.name = name
        self.description = description

        # These are the connected rooms in each direction
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

        # Items inside this room
        self.items = items

    def __str__(self):
        return f"You entered the {self.name} room.\n{self.description}\n Items: {self.items}"
