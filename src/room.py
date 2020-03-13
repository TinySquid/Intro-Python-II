import textwrap
from inventory import Inventory


class Room:
    """ Blueprint for a single dungeon room """

    def __init__(self, name, description, is_lit=True, loot=[]):
        # Basic room info
        self.name = name
        self.description = description

        # References to connected rooms in each direction
        self.exits = {
            "n": None,
            "s": None,
            "e": None,
            "w": None,
        }

        # Items inside this room
        self.inventory = Inventory(loot)

        # Is this room illuminated or not?
        self.is_lit = is_lit

    def set_exits(self, exits):
        """ Sets a number of exits for a room """

        for key, value in exits.items():
            # Make sure key is a valid direction
            if key not in ("n", "s", "e", "w"):
                raise KeyError("Room directional exits can only be n, s, e, or w")
            else:
                self.exits[key] = value

    def get_exits(self):
        """ Returns a dict of room exits """
        return self.exits

    def set_loot(self, loot):
        """ Adds a list of items into a room """
        self.inventory.set(loot)

    def get_loot(self):
        """ Returns contents of a room's inventory """
        return self.inventory.get()

    # This allows for custom handling of certain items being dropped in a room
    def deposit_loot_item(self, item):
        """ Returns an item to a room's inventory """
        self.inventory.add(item)

    # This allows for custom handling of certain items being taken from a room
    def withdraw_loot_item(self, item):
        """ Removes an item from a room's inventory """
        self.inventory.remove(item)

    def __str__(self):
        if self.is_lit:
            # Display normal information
            pretty_string = f"Room: {self.name}\n"
            pretty_string += textwrap.fill(self.description, 70) + "\n"

            # Append items in room to string
            if self.inventory:
                item_list = "\n| Loot in room |"

                for item in self.inventory.get():
                    item_list += f"\n{item.name} : {item.description}"

                pretty_string += item_list

                return f"{pretty_string}"
            else:
                return f"{pretty_string}"
        else:
            # Room is dark, so you won't be able to see any items or exits!
            return "It's pitch black in here!"

