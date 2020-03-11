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

    def move(self, direction):
        """ Moves player in provided direction to room exit point """

        paths = {
            "n": self.current_room.n_to,
            "s": self.current_room.s_to,
            "e": self.current_room.e_to,
            "w": self.current_room.w_to,
        }

        next_room = paths[direction]

        if next_room:
            self.current_room = next_room
        else:
            print("Invalid path!")

