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
                    "You kill the wolf with the knife you found earlier. After moving forward, you find one of the exits. Congratulations!")
            else:
                print("The wolf-like creature has killed you.")
            quit()
        elif userInput == "flee":
            showSkeletons()
        else:
            print("Please enter a valid option.")


def showSkeletons():
    directions = ["backward", "forward"]
    global weapon
    print("You see a wall of skeletons as you walk into the room. Someone is watching you. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/backward/forward")
        userInput = input()
        if userInput == "left":
            print("You find that this door opens into a wall. You open some of the drywall to discover a knife.")
            weapon = True
        elif userInput == "backward":
            introScene()
        elif userInput == "forward":
            strangeCreature()
        else:
            print("Please enter a valid option.")


def hauntedRoom():
    directions = ["right", "left", "backward"]
    print("You hear strange voices. You think you have awoken some of the dead. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/left/backward")
        userInput = input()
        if userInput == "right":
            print("Multiple goul-like creatures start emerging as you enter the room. You are killed.")
            quit()
        elif userInput == "left":
            print("You made it! You've found an exit.")
            quit()
        elif userInput == "backward":
            introScene()
        else:
            print("Please enter a valid option.")


def backpackScene():
    directions = ["north", "south"]
    print(
        "You discover an empty backpack that has been dropped on the ground. Someone has been here recently. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: north/south")
        userInput = input()
        if userInput == "north":
            print("You made it! You've found an exit.")
            quit()
        elif userInput == "south":
            showShadowFigure()
        else:
            print("Please enter a valid option.")


def showGhostFigure():
    directions = ["north", "south", "east"]
    print("You see a dark transparent figure appear in the distance. You are creeped out. Where would you like to go?")
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
    directions = ["left", "right", "forward"]
    print(
        "You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/backward/forward")
        userInput = input()
        if userInput == "left":
            showShadowFigure()
        elif userInput == "right":
            showSkeletons()
        elif userInput == "forward":
            hauntedRoom()
        elif userInput == "backward":
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