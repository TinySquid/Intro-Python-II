import textwrap


class Room:
    """ Blueprint for a single dungeon room """

    def __init__(self, name, description, is_lit=False):
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
        self.items = []

        # Is this room illuminated or not?
        self.is_lit = is_lit

    def set_exits(self, exits):
        for key, value in exits.items():
            # Make sure key is a valid direction
            if key not in ("n", "s", "e", "w"):
                raise KeyError("Room directional exits can only be n, s, e, or w")
            else:
                self.exits[key] = value

    def get_exits(self):
        return self.exits

    def set_items(self, items):
        for item in items:
            self.items.append(item)

    def __str__(self):
        if self.is_lit:
            # Display normal information
            room = f"Room: {self.name}"
            description = textwrap.fill(self.description, 70)

            # Append items in room to string
            if len(self.items) >= 1:
                item_list = "Items in room: - "

                for item in self.items:
                    item_list += item.name + " - "

                return f"{room}\n{description}\n{item_list}"

            return f"{room}\n{description}"
        else:
            # Room is dark, so you won't be able to see any items or exits!
            return "It's pitch black in here!"

