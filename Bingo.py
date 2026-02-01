import random
from csv import DictReader,DictWriter
from Bingo_Classes import *

# --------------------------------------------------------------
# ---------------------------Load-------------------------------
def load(card1): 
    """Load a Bingocard savestate"""
    name = input(
            "What is the name of the file you would like to load from? (inclode the files extention, IE .txt or similar)\n")
    card1.load(name)
# ---------------------------Load-------------------------------
# --------------------------------------------------------------


# --------------------------------------------------------------
# -----------------------Radom Creation-------------------------
def random_create(card1):
    """Create a Bingocard with random placement of each spot"""
    templist = list()
    for i in range(24):
        x = input(f"{i+1} - ")
        templist.append(x)

    for i in range(5):
        for j in range(5):
            if i == 2 and j == 2:
                continue
            card1.card[i][j]["description"] = random.choice(templist)
            templist.remove(card1.card[i][j]["description"])
# -----------------------Radom Creation-------------------------
# --------------------------------------------------------------


# --------------------------------------------------------------
# -----------------------Chosen Creation------------------------
def choice_create(card1):
    """Create a Bingocard with Chosen placement of each spot"""
    for i in range(5):
        for j in range(5):
            if i == 2 and j == 2:
                continue
            card1.card[i][j]["description"] = input(f"{i+1},{j+1} - ")
# -----------------------Chosen Creation------------------------
# --------------------------------------------------------------


# --------------------------------------------------------------
# -----------------------------Main-----------------------------
def main():
    card1 = BingoCard()
    while(True):
        choice = input("What would you like to do?\n 1- Print card\n 2- Create or Load a card\n 3- Mark a spot\n 4- Reassign a spot\n 5- Save the Bingo card\n 6- Exit the program\n")

        match int(choice):
            case 1:
                print(card1.show())

            case 2:
                while (True): # While loop to make sure user chooses to load or to start a new card
                    y = input(
                        "would you like to load a previous save or start a new one?('l' for load or 'n' for new): \n").lower()
                    if y == 'l':
                        load(card1)
                        break

                    elif y == 'n':
                        while (True):
                            x = input(
                                "Would you like to insert items in a random orientation, or for you to choose it? ('r' for random or 'c' to choose):\n").lower()
                            if x == 'r':
                                random_create(card1)
                                break
                            if x == 'c':
                                choice_create(card1)
                                break
                        break

            case 3:
                v = input("Would you like to mark or unmark the spot? (1 to mark, 0 to unmark)\n")
                x = int(input("Which row is the spot on?\n"))
                y = int(input("Which collumn is the spot on?\n"))
                card1.card[x-1][y-1]["mark"] = bool(int(v))

            case 4:
                v = input("What would you like to reassign the spot to?\n")
                x = int(input("Which row is the spot on?\n"))
                y = int(input("Which collumn is the spot on?\n"))
                card1.card[x-1][y-1]["description"] = v

            case 5:
                name = "".join([input("What name do you want to save as?\n"),".csv"])
                card1.save(name)

            case 6:
                e = input("Are you sure you wish to exit? (Insert y to exit):\n").lower()
                if e == "y":
                    break

# -----------------------------Main-----------------------------
# --------------------------------------------------------------

if __name__ == "__main__":
    main()
