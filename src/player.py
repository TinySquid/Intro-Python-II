# Write a class to hold player information, e.g. what room they are in currently.
# Players should have a name and current_room attributes

# Add capability to add Items to the player's inventory.
# The inventory can also be a list of items "in" the player, similar to how Items can be in a Room.


class Player:
    """ Main character  """

    def __init__(self, name, initial_room):
        # Player info
        self.name = name
        self.current_room = initial_room

        # Player inventory
        self.inventory = []

        self.directions = {"n": "north", "s": "south", "e": "east", "w": "west"}

    def move(self, direction):
        """ Moves player in provided direction to room exit point """

        possible_paths = self.current_room.get_exits()

        next_room = possible_paths[direction]

        if next_room:
            self.current_room = next_room
        else:
            print(f"There is no exit to the {self.directions[direction]}\n")
