class Room:
    def __init__(self, description: str = "", north: int = 0, east: int = 0, south: int = 0, west: int = 0):
        self.description: str = description
        self.north: int = north
        self.east: int = east
        self.south: int = south
        self.west: int = west


def main():
    room_list = []
    # main room/ intro room
    room = Room(
        "You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?",
        None, 2, 1, 4)

    room_list.append(room)  # cursed room
    room = Room(
        "You have arrived in the cursed room.\nYou hear strange voices. You think you have awoken some of the dead. "
        "Where would you like to go?",
        0, 9, None, 10)

    room_list.append(room)  # dead spider room
    room = Room(
        "You see a wall of dead spiders as you walk into the room. Somebody is watching you. Where would you like "
        "to go?", None, 3, None, 0)

    room_list.append(room)  # strange creature room
    room = Room("A strange wolf-like creature has appeared. You can either run or fight it. What would you like to do?",
                None, None, None, 2)

    room_list.append(room)  # ghost figure room
    room = Room(
        "You see a dark transparent figure appear in the distance. Chills run down your spine. Where would you like "
        "to go?", 6, 0, None, None)

    room_list.append(room)  # backpack room
    room = Room(
        "You discover an empty backpack that has been dropped on the ground. Someone has been here recently. Where "
        "would you like to go?", 7, None, 4, None)

    room_list.append(room)  # exit number eight
    room = Room("You made it! You've found an exit.", None, None, 6, None)

    room_list.append(room)  # exit number ten
    room = Room("You made it! You've found an exit.", None, None, None, 1)

    room_list.append(room)  # Death room eleven
    room = Room("Multiple bleeding zombies start emerging as you enter the room. You are killed.", None, 1, None, None)

    room_list.append(room)

    current_room = 0
    next_room = None

    done = False
    while not done:
        print("\n" + room_list[current_room].description)
        user_input = input("Where would you like to go? ")
        if user_input.upper() == "N" or user_input.upper() == "NORTH":
            next_room = room_list[current_room].north
        elif user_input.upper() == "E" or user_input.upper() == "EAST":
            next_room = room_list[current_room].east
        elif user_input.upper() == "S" or user_input.upper() == "SOUTH":
            next_room = room_list[current_room].south
        elif user_input.upper() == "W" or user_input.upper() == "WEST":
            next_room = room_list[current_room].west
        elif user_input.upper() == "Q" or user_input.upper() == "QUIT":
            done = True
            print("\nYou left the catacombs\nGame Over")
            continue
        else:
            print("Please enter a valid option.")
            next_room = None
            continue

        if next_room is None:
            print("Dead end/ Wall encountered")
        else:
            current_room = next_room

    current_room = 1
    next_room = None

    done = False
    while not done:
        print("\n" + room_list[current_room].description)
        user_input = input("Where would you like to go? ")
        if user_input.upper() == "N" or user_input.upper() == "NORTH":
            next_room = room_list[current_room].north
        elif user_input.upper() == "E" or user_input.upper() == "EAST":
            next_room = room_list[current_room].east
        elif user_input.upper() == "S" or user_input.upper() == "SOUTH":
            next_room = room_list[current_room].south
        elif user_input.upper() == "W" or user_input.upper() == "WEST":
            next_room = room_list[current_room].west
        elif user_input.upper() == "Q" or user_input.upper() == "QUIT":
            done = True
            print("\nYou left the catacombs\nGame Over")
            continue
        else:
            print("Please enter a valid option.")
            next_room = None
            continue

        if next_room is None:
            print("Dead end/ Wall encountered")
        else:
            current_room = next_room

    current_room = 2
    next_room = None

    done = False
    while not done:
        print("\n" + room_list[current_room].description)
        user_input = input("Where would you like to go? ")
        if user_input.upper() == "N" or user_input.upper() == "NORTH":
            next_room = room_list[current_room].north
        elif user_input.upper() == "E" or user_input.upper() == "EAST":
            next_room = room_list[current_room].east
        elif user_input.upper() == "S" or user_input.upper() == "SOUTH":
            next_room = room_list[current_room].south
        elif user_input.upper() == "W" or user_input.upper() == "WEST":
            next_room = room_list[current_room].west
        elif user_input.upper() == "Q" or user_input.upper() == "QUIT":
            done = True
            print("\nYou left the catacombs\nGame Over")
            continue
        else:
            print("Please enter a valid option.")
            next_room = None
            continue

        if next_room is None:
            print("Dead end/ Wall encountered")
        else:
            current_room = next_room

    current_room = 3
    next_room = None

    done = False
    while not done:
        print("\n" + room_list[current_room].description)
        user_input = input("Where would you like to go? ")
        if user_input.upper() == "N" or user_input.upper() == "NORTH":
            next_room = room_list[current_room].north
        elif user_input.upper() == "E" or user_input.upper() == "EAST":
            next_room = room_list[current_room].east
        elif user_input.upper() == "S" or user_input.upper() == "SOUTH":
            next_room = room_list[current_room].south
        elif user_input.upper() == "W" or user_input.upper() == "WEST":
            next_room = room_list[current_room].west
        elif user_input.upper() == "Q" or user_input.upper() == "QUIT":
            done = True
            print("\nYou left the catacombs\nGame Over")
            continue
        else:
            print("Please enter a valid option.")
            next_room = None
            continue

        if next_room is None:
            print("Dead end/ Wall encountered")
        else:
            current_room = next_room

    current_room = 4
    next_room = None

    done = False
    while not done:
        print("\n" + room_list[current_room].description)
        user_input = input("Where would you like to go? ")
        if user_input.upper() == "N" or user_input.upper() == "NORTH":
            next_room = room_list[current_room].north
        elif user_input.upper() == "E" or user_input.upper() == "EAST":
            next_room = room_list[current_room].east
        elif user_input.upper() == "S" or user_input.upper() == "SOUTH":
            next_room = room_list[current_room].south
        elif user_input.upper() == "W" or user_input.upper() == "WEST":
            next_room = room_list[current_room].west
        elif user_input.upper() == "Q" or user_input.upper() == "QUIT":
            done = True
            print("\nYou left the catacombs\nGame Over")
            continue
        else:
            print("Please enter a valid option.")
            next_room = None
            continue

        if next_room is None:
            print("Dead end/ Wall encountered")
        else:
            current_room = next_room

    current_room = 5
    next_room = None

    done = False
    while not done:
        print("\n" + room_list[current_room].description)
        user_input = input("Where would you like to go? ")
        if user_input.upper() == "N" or user_input.upper() == "NORTH":
            next_room = room_list[current_room].north
        elif user_input.upper() == "E" or user_input.upper() == "EAST":
            next_room = room_list[current_room].east
        elif user_input.upper() == "S" or user_input.upper() == "SOUTH":
            next_room = room_list[current_room].south
        elif user_input.upper() == "W" or user_input.upper() == "WEST":
            next_room = room_list[current_room].west
        elif user_input.upper() == "Q" or user_input.upper() == "QUIT":
            done = True
            print("\nYou left the catacombs\nGame Over")
            continue
        else:
            print("Please enter a valid option.")
            next_room = None
            continue

        if next_room is None:
            print("Dead end/ Wall encountered")
        else:
            current_room = next_room

    current_room = 6
    next_room = None

    done = False
    while not done:
        print("\n" + room_list[current_room].description)
        user_input = input("Where would you like to go? ")
        if user_input.upper() == "N" or user_input.upper() == "NORTH":
            next_room = room_list[current_room].north
        elif user_input.upper() == "E" or user_input.upper() == "EAST":
            next_room = room_list[current_room].east
        elif user_input.upper() == "S" or user_input.upper() == "SOUTH":
            next_room = room_list[current_room].south
        elif user_input.upper() == "W" or user_input.upper() == "WEST":
            next_room = room_list[current_room].west
        elif user_input.upper() == "Q" or user_input.upper() == "QUIT":
            done = True
            print("\nYou left the catacombs\nGame Over")
            continue
        else:
            print("Please enter a valid option.")
            next_room = None
            continue

        if next_room is None:
            print("Dead end/ Wall encountered")
        else:
            current_room = next_room

    current_room = 7
    next_room = None

    done = False
    while not done:
        print("\n" + room_list[current_room].description)
        user_input = input("Where would you like to go? ")
        if user_input.upper() == "N" or user_input.upper() == "NORTH":
            next_room = room_list[current_room].north
        elif user_input.upper() == "E" or user_input.upper() == "EAST":
            next_room = room_list[current_room].east
        elif user_input.upper() == "S" or user_input.upper() == "SOUTH":
            next_room = room_list[current_room].south
        elif user_input.upper() == "W" or user_input.upper() == "WEST":
            next_room = room_list[current_room].west
        elif user_input.upper() == "Q" or user_input.upper() == "QUIT":
            done = True
            print("\nYou left the catacombs\nGame Over")
            continue
        else:
            print("Please enter a valid option.")
            next_room = None
            continue

        if next_room is None:
            print("Dead end/ Wall encountered")
        else:
            current_room = next_room

    current_room = 8
    next_room = None

    done = False
    while not done:
        print("\n" + room_list[current_room].description)
        user_input = input("Where would you like to go? ")
        if user_input.upper() == "N" or user_input.upper() == "NORTH":
            next_room = room_list[current_room].north
        elif user_input.upper() == "E" or user_input.upper() == "EAST":
            next_room = room_list[current_room].east
        elif user_input.upper() == "S" or user_input.upper() == "SOUTH":
            next_room = room_list[current_room].south
        elif user_input.upper() == "W" or user_input.upper() == "WEST":
            next_room = room_list[current_room].west
        elif user_input.upper() == "Q" or user_input.upper() == "QUIT":
            done = True
            print("\nYou left the catacombs\nGame Over")
            continue
        else:
            print("Please enter a valid option.")
            next_room = None
            continue

        if next_room is None:
            print("Dead end/ Wall encountered")
        else:
            current_room = next_room
main()
