import sys

# Import game blueprints
from room import Room
from player import Player

# Utility func to clear screen on all platforms
from utility import clear_terminal

# Add items dir to sys path
sys.path.append("/items")

# Import game handheld items
from items.item import Item
from items.lantern import Lantern
from items.coin import Coin

# Declare all the rooms
# dict with keys... Room instance values
room = {
    "outside": Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons",
        # loot=[
        #     Item("Potato", "It's... Just a potato."),
        #     Item("Rusty Sword", "How long has this been here?",),
        # ],
    ),
    "foyer": Room(
        "Foyer",
        "Dim light filters in from the south. Dusty passages run north and east.",
    ),
    "overlook": Room(
        "Grand Overlook",
        "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.",
    ),
    "narrow": Room(
        "Narrow Passage",
        "The narrow passage bends here from west to north. The smell of gold permeates the air.",
    ),
    "treasure": Room(
        "Treasure Chamber",
        "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",
    ),
}


# Link rooms together

room["outside"].set_exits({"n": room["foyer"]})
room["outside"].set_loot(
    [Item("Potato", "It's... Just a potato."),]
)

room["foyer"].set_exits(
    {"n": room["overlook"], "s": room["outside"], "e": room["narrow"]}
)

room["foyer"].set_loot([Lantern()])

room["overlook"].set_exits({"s": room["foyer"]})
room["narrow"].set_exits({"n": room["treasure"], "w": room["foyer"]})
room["treasure"].set_exits({"s": room["narrow"]})

room["treasure"].set_loot([Coin(13)])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Bob Ross", room["outside"])

# Possible player commands
def eval_verb_command(verb):
    verb_cmds = {
        "n": lambda: player.move("n"),
        "s": lambda: player.move("s"),
        "e": lambda: player.move("e"),
        "w": lambda: player.move("w"),
        "i": lambda: player.inventory.print_contents(),
        "q": lambda: exit(),
    }

    return verb_cmds.get(verb, lambda: print("Invalid command!\n"))


def eval_verb_noun_command(verb, noun):
    verb_noun_cmds = {
        "get": lambda: player.take_item(noun),
        "take": lambda: player.take_item(noun),
        "drop": lambda: player.drop_item(noun),
    }

    return verb_noun_cmds.get(verb, lambda: print("Invalid command!\n"))


def print_guide():
    print("\nMovement commands: [n]orth, [s]outh, [e]ast, [w]est")
    print("Other commands: [i]nventory, [take] [item], [drop] [item], [q]uit\n")


# Clear screen in preparation for game
clear_terminal()

# REPL
while True:

    # Display room and description
    print(player.current_room)

    # Display commands
    print_guide()

    # Get user command
    player_input = input("-> ")

    # Wipe terminal
    clear_terminal()

    # Get command terms
    command = player_input.split(" ")

    # Determine command format
    if len(command) > 1:
        # Command is in the format "verb noun"
        eval_verb_noun_command(command[0], " ".join(command[1:]))()
    else:
        # Command is just a verb
        eval_verb_command(command[0])()

