class Item:
    """ Base class for all items in the game """

    def __init__(self, name, description, count=1):
        self.name = name
        self.description = description
        self.count = count

    def on_take(self):
        print(f"You have picked up {self.name}\n")

    def on_drop(self):
        print(f"You dropped {self.name}\n")
