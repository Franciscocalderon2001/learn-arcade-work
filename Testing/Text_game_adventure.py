weapon = False


def strangeCreature():
    actions = ["fight", "flee"]
    global weapon
    print("A strange wolf-like creature has appeared. You can either run or fight it. What would you like to do?")
    userInput = ""
    while userInput not in actions:
        print("Options: flee/fight")
        userInput = input()
        if userInput == "fight":
            if weapon:
                print(
                    "You kill the wolf-like creature with the knife you found earlier. After moving forward, "
                    "you find one of the exits. Congratulations!")
            else:
                print("The wolf-like creature has killed you.")
            quit()
        elif userInput == "flee":
            showDeadSpiders()
        else:
            print("Please enter a valid option.")


def showDeadSpiders():
    directions = ["west", "north", "east"]
    global weapon
    print("You see a wall of dead spiders as you walk into the room. Somebody is watching you. Where would you like "
          "to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: west/north/east")
        userInput = input()
        if userInput == "north":
            print("You find that this door opens into a wall. You open some of the drywall to discover a knife.")
            weapon = True
        elif userInput == "west":
            introScene()
        elif userInput == "east":
            strangeCreature()
        else:
            print("Please enter a valid option.")


def cursedRoom():
    directions = ["north", "west", "east"]
    print("You hear strange voices. You think you have awoken some of the dead. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: north/west/east")
        userInput = input()
        if userInput == "west":
            print("Multiple bleeding zombies start emerging as you enter the room. You are killed.")
            quit()
        elif userInput == "east":
            print("You made it! You've found an exit.")
            quit()
        elif userInput == "north":
            introScene()
        else:
            print("Please enter a valid option.")


def backpackScene():
    directions = ["north", "south"]
    print(
        "You discover an empty backpack that has been dropped on the ground. Someone has been here recently. Where "
        "would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: north/south")
        userInput = input()
        if userInput == "north":
            print("You made it! You've found an exit.")
            quit()
        elif userInput == "south":
            showGhostFigure()
        else:
            print("Please enter a valid option.")


def showGhostFigure():
    directions = ["north", "south", "east"]
    print("You see a dark transparent figure appear in the distance. Chills run down your spine. Where would you like "
          "to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: north/south/east")
        userInput = input()
        if userInput == "north":
            backpackScene()
        elif userInput == "south":
            print("You find that this door opens into a wall.")
        elif userInput == "east":
            introScene()
        else:
            print("Please enter a valid option.")


def introScene():
    directions = ["south", "north", "east", "west"]
    print(
        "You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: south/north/east/west")
        userInput = input()
        if userInput == "south":
            showGhostFigure()
        elif userInput == "east":
            showDeadSpiders()
        elif userInput == "south":
            cursedRoom()
        elif userInput == "north":
            print("You find that this door opens into a wall.")
        else:
            print("Please enter a valid option.")


if __name__ == "__main__":
    while True:
        print("Welcome to Tito's Mansion!")
        print("As a curious traveller, you have decided to visit the Catacombs of Tito's Mansion.")
        print("However, throughout your exploration, you find yourself lost.")
        print("You can choose to walk in multiple directions to find a way out.")
        print("Let's begin with your name: ")
        name = input()
        print("Best of luck, " + name + ".")
        introScene()
