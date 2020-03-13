from items.item import Item


class Coin(Item):
    def __init__(self, count):
        super().__init__(
            "Damaged Gold Coin", "The empire is law. The law is sacred", count
        )

    def on_take(self):
        print(f"You picked up {self.count} damaged coins.\n")
