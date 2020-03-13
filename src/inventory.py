class Inventory:
    """ Creates a storage system for items """

    def __init__(self, initial_items=[]):
        self.inventory = initial_items

    def set(self, items):
        self.inventory = items

    def add(self, item):
        """ Add item to inventory """
        self.inventory.append(item)

    def remove(self, item):
        """ Remove item from inventory """
        self.inventory.remove(item)

    def get(self):
        """ Return list of inventory contents"""
        return self.inventory

    def print_contents(self):
        pretty_string = "| Inventory |\n"

        if len(self.inventory) > 0:
            for item in self.inventory:
                pretty_string += f"{item.name} : {item.description}\n"
        else:
            pretty_string += "...Empty!\n"

        print(pretty_string)
