import textwrap


class Room:
    def __init__(self, name, description, items=None):
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
        self.items = items

    def set_exits(self, exits):
        for key, value in exits.items():
            if key not in ("n", "s", "e", "w"):
                raise KeyError("Room directional exits can only be n, s, e, or w")
            else:
                self.exits[key] = value

    def get_exits(self):
        return self.exits

    def __str__(self):
        return f"Room: {self.name}\n{textwrap.fill(self.description, 70)}"

