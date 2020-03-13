from items.item import Item


class Lantern(Item):
    def __init__(self):
        super().__init__("Lantern", "A light source to keep the dark at bay")

    def on_drop(self):
        print("It's not wise to drop your source of light!")
