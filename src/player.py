from inventory import Inventory

""" 
    Player class that provides the ability to traverse dungeon rooms and
    pickup / drop loot
"""


class Player:
    """ Main character class """

    def __init__(self, name, starting_room, starting_items=[]):
        # Player info
        self.name = name
        self.current_room = starting_room
        self.previous_room = None

        # Player inventory
        self.inventory = Inventory(starting_items)

        # Movement text for easier printing later
        self.directions = {"n": "north", "s": "south", "e": "east", "w": "west"}

    def move(self, direction):
        """ Moves player in provided direction to next room """

        # Get all exits for the current room
        possible_paths = self.current_room.get_exits()

        # Get exit in provided direction
        next_room = possible_paths[direction]

        if next_room:
            # Exit is a valid room
            self.previous_room = self.current_room
            self.current_room = next_room

        else:
            print(f"There is no exit to the {self.directions[direction]}\n")

    def take_item(self, item_to_take):
        """ Take item from a room and move it into player inventory """

        for loot_item in self.current_room.get_loot():
            if loot_item.name == item_to_take:
                # The item we are searching for was found
                self.inventory.add(loot_item)
                self.current_room.withdraw_loot_item(loot_item)

                # Fire item take event
                loot_item.on_take()

                # Leave the loop because we're done
                break

    def drop_item(self, item_to_drop):
        """ Drop inventory item onto floor """
        for item in self.inventory.get():
            if item.name == item_to_drop:
                self.inventory.remove(item)
                self.current_room.deposit_loot_item(item)

                # Fire item drop event
                item.on_drop()

                break
