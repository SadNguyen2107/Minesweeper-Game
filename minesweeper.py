# Create a Minesweeper Game using Python Terminal
# Author: Sad Nguyen
# -----------------------------------------------------------------------------------------
# Welcome to my Minesweeper Game Project
# ----------------------------------------------------------------------------------------

#! Think of an idea
# Who do you want to build something for? Yourself? Your friends? Your family? Your co-workers?
# I want to build it for myself and my friends to play

# What are your/their hobbies?
# To create more fun games

# Do you want to build something more fun or something more useful?
# Yes, I will definitely try my best to develop such a thing that's bring joy to everyone

#! Project Brainstorming
# What does your program do?
# Challenge the player to allocate all the bombs on the map and win

# * How will it work in a terminal?
# ? Step 1: Print out the board
# ? Step 2: let the player press the index
# ? Step 3: if boom ? kaboom : continue
# ? Step 4: if out_of_boom ? win : continue
# ? Step 5: Print out the Victory Screen

# Is it one player or two players?
# One Player Game
import random
import sys

def translateintoHumanReadable(Pos):
    x_coordinate, y_coordinate = Pos
    return x_coordinate + 1, y_coordinate + 1

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.isExploded = False

    def __repr__(self) -> str:
        description = f"{self.name} is currently "
        if self.isExploded:
            description += "exploded into piece"

        description += "has not explode"
        return description

    def choosePos(self):
        x_coordinate = int(input("X_coordinate: ")) - 1
        y_coordinate = int(input("Y_coordinate: ")) - 1
        return x_coordinate, y_coordinate

    def checkSituation(self):
        if self.isExploded:
            print(f"{self.name} just have exploded")
            

    def winGame(self, winSignal: bool):
        if winSignal:
            print("Congratulations")
            print(f"{self.name} just win the Minesweeper Game")


class SafeSpot:
    ID = 1
    safeSpots = set()

    def __init__(self) -> None:
        self.representation = int()
        self.ID = SafeSpot.ID
        SafeSpot.ID += 1

    def __repr__(self) -> str:
        description = f"Spot with ID {self.ID} is currently located at {self.boomPos}"
        return description


class Boom:
    ID = 1
    booms = set()

    @classmethod
    def genBoomPosition(cls):
        boom_X_coordinate = random.randint(0, 2)
        boom_Y_coordinate = random.randint(0, 2)
        boomPos = (boom_X_coordinate, boom_Y_coordinate)
        if boomPos not in cls.booms:
            cls.booms.add(boomPos)
            return boomPos

        return cls.genBoomPosition()

    def __init__(self) -> None:
        self.representation = "@"
        self.ID = Boom.ID
        self.boomPos = Boom.genBoomPosition()
        Boom.ID += 1

    def __repr__(self) -> str:
        description = f"Boom with ID {self.ID} is currently located at {self.boomPos}"
        return description


class Map:
    def __init__(self, player, booms: set):
        self.player = player
        self.booms = booms

        # * Use for checking how many booms left
        self.currentBomb = len(self.booms)

        # Mineswepper Map
        self.array1 = ["#", "#", "#"]
        self.array2 = ["#", "#", "#"]
        self.array3 = ["#", "#", "#"]

    def printMap(self):
        print("-----------------------------------------------------------------")
        print(self.array1)
        print(self.array2)
        print(self.array3)
        print(f"Booms left: {len(self.booms)}")
        print("-----------------------------------------------------------------")

    # # ? For checking boom
    def checkUp(self, x_coordinate, y_coordinate):
        for boom in self.booms:
            if (x_coordinate, y_coordinate - 1) == boom.boomPos:
                return 1

        return 0

    def checkDown(self, x_coordinate, y_coordinate):
        for boom in self.booms:
            if (x_coordinate, y_coordinate + 1) == boom.boomPos:
                return 1

        return 0

    def checkRight(self, x_coordinate, y_coordinate):
        for boom in self.booms:
            if (x_coordinate + 1, y_coordinate) == boom.boomPos:
                return 1

        return 0

    def checkLeft(self, x_coordinate, y_coordinate):
        for boom in self.booms:
            if (x_coordinate - 1, y_coordinate) == boom.boomPos:
                return 1

        return 0

    def checkUpRight(self, x_coordinate, y_coordinate):
        for boom in self.booms:
            if (x_coordinate + 1, y_coordinate - 1) == boom.boomPos:
                return 1

        return 0

    def checkRightDown(self, x_coordinate, y_coordinate):
        for boom in self.booms:
            if (x_coordinate + 1, y_coordinate + 1) == boom.boomPos:
                return 1

        return 0

    def checkDownLeft(self, x_coordinate, y_coordinate):
        for boom in self.booms:
            if (x_coordinate - 1, y_coordinate + 1) == boom.boomPos:
                return 1

        return 0

    def checkLeftUp(self, x_coordinate, y_coordinate):
        for boom in self.booms:
            if (x_coordinate - 1, y_coordinate - 1) == boom.boomPos:
                return 1
        return 0

    def checkSafe(self, x_coordinate, y_coordinate):
        self.nowBomb = 0
        self.nowBomb += self.checkUp(x_coordinate, y_coordinate)
        self.nowBomb += self.checkDown(x_coordinate, y_coordinate)
        self.nowBomb += self.checkRight(x_coordinate, y_coordinate)
        self.nowBomb += self.checkLeft(x_coordinate, y_coordinate)
        self.nowBomb += self.checkUpRight(x_coordinate, y_coordinate)
        self.nowBomb += self.checkLeftUp(x_coordinate, y_coordinate)
        self.nowBomb += self.checkDownLeft(x_coordinate, y_coordinate)
        self.nowBomb += self.checkRightDown(x_coordinate, y_coordinate)

    # ? Use for player
    def checkBoom(self, x_coordinate: int, y_coordinate: int):
        for boom in self.booms:
            print(translateintoHumanReadable(boom.boomPos))
            # If Explode
            if (x_coordinate, y_coordinate) == boom.boomPos:
                self.player.isExploded = True
                self.player.checkSituation()

                # If explode
                if y_coordinate == 0:
                    self.array1[x_coordinate] = boom.representation
                elif y_coordinate == 1:
                    self.array2[x_coordinate] = boom.representation
                else:
                    self.array3[x_coordinate] = boom.representation

                self.booms.remove(boom)
                self.printMap()
                print("Thank you for playing!!")
                sys.exit()

        self.checkSafe(x_coordinate, y_coordinate)
        # If don't explode
        if y_coordinate == 0:
            self.array1[x_coordinate] = self.nowBomb
        elif y_coordinate == 1:
            self.array2[x_coordinate] = self.nowBomb
        else:
            self.array3[x_coordinate] = self.nowBomb
        
        self.printMap()
        
