import random

# --------------------------------------------------------------
# -----------------------Bingo spot class-----------------------
class BingoSpot:
    markedSpots = 1

    def __init__(self, attribute = 0, mark = False): # Initiate every spot 
        self.Attribute = attribute
        self.marked = mark

    def __repr__(self):
        return f"{self.Attribute}-:is:-{self.marked}"

# mark property
    @property
    def mark(self):
        return self.marked

    @mark.setter
    def mark(self,Value):
        if self.marked == Value: #Check if user is setting the mark to something it already is
            return

        self.marked = Value #Set the mark then increase or decrease count of how many spots are marked
        if Value:
            BingoSpot.markedSpots += 1
        else:
            BingoSpot.markedSpots -= 1

# Attribute property
    @property
    def attribute(self):
        return  self.Attribute

    @attribute.setter
    def attribute(self,Value): #Set property
        self.Attribute = Value
# -----------------------Bingo spot class-----------------------
# --------------------------------------------------------------


# --------------------------------------------------------------
# -----------------------Bingo card class-----------------------
class BingoCard:
    def __init__(self): #Initate the card with the middle spot as free spot
        self.card = [[BingoSpot(), BingoSpot(), BingoSpot(), BingoSpot(), BingoSpot()],
                     [BingoSpot(), BingoSpot(), BingoSpot(),BingoSpot(), BingoSpot()],
                     [BingoSpot(), BingoSpot(), BingoSpot("Free Spot", True), BingoSpot(), BingoSpot()],
                     [BingoSpot(), BingoSpot(), BingoSpot(),BingoSpot(), BingoSpot()],
                     [BingoSpot(), BingoSpot(), BingoSpot(), BingoSpot(), BingoSpot()]]

    def __repr__(self):
        return show()

    def show(self):
        return f"{self.card[0]} \n {self.card[1]} \n {self.card[2]} \n {self.card[3]} \n {self.card[4]} \n"

    def save(self,name): # Save the Bingocard into an external file
        text_trans =" \n".join([" -:_j_:- ".join([str(spot) for spot in row]) for row in self.card]) #Transform the card variable into a savable string

        with open(name,"w") as bingo: # save it into a file
            bingo.write(text_trans)
        print("Bingo card has been saved successfullu")

    def load(self,name): #Load Bingocard from an external file
        try:
            with open(name, "r") as bingo:
                dataT1 = bingo.readlines()
            dataT2 = [line.split(" -:_j_:- ") for line in dataT1]

            y = 0
            for line in dataT2:
                x = 0
                for spot in line:
                    self.card[y][x].attribute = spot.split("-:is:-")[0]
                    self.card[y][x].mark = spot.split("-:is:-")[1]

                    x += 1
                y += 1

            print("Bingo card has been loaded successfully")
        except FileNotFoundError:
            print(f"File '{name}' does not exist")
# -----------------------Bingo card class-----------------------
# --------------------------------------------------------------


# --------------------------------------------------------------
# -----------------------Creation or Load-----------------------
def CoL(card1):

    while (True):

        load = input("would you like to load a previous save or start a new one?('y' for load or 'n' for not): \n").lower()
        if (load in ['y', 'n']):
            break

    match load:
        case 'y':
            name = input("What is the name of the file you would like to load from? (inclode the files extention, IE .txt or similar)\n")
            card1.load(name)
        case 'n':

            while (True):
                x = input("Would you like to insert items in a random orientation, or for you to choose it? ('y' for random or 'n' for not):\n").lower()
                if (x in ['y', 'n']):
                    break

            match x:

                case 'y':
                    templist = list()
                    for i in range(24):
                        x = input(f"{i+1} - ")
                        templist.append(x)

                    for i in range(5):
                        for j in range(5):
                            if i == 2 and j == 2:
                                continue
                            card1.card[i][j].attribute = random.choice(templist)
                            templist.remove(card1.card[i][j].attribute)

                case 'n':
                    for i in range(5):
                        for j in range(5):
                            if i == 2 and j == 2:
                                continue
                            card1.card[i][j].attribute = input(f"{i+1},{j+1} - ")

# -----------------------Creation or Load-----------------------
# --------------------------------------------------------------


# --------------------------------------------------------------
# -----------------------------Main-----------------------------
def main():
    card1 = BingoCard()
    while(True):
        Choice = input("What would you like to do?\n 1- Print card\n 2- Load or create a card\n 3- Mark a spot\n 4- Reassign a spot\n 5- Save the Bingo card\n 6- Exit the program\n")

        match int(Choice):
            case 1:
                print(card1.show())
            case 2:
                CoL(card1)
            case 3:
                v = input("Would you like to mark or unmark the spot? (1 to mark, 0 to unmark)\n")
                x = int(input("Which row is the spot on?\n"))
                y = int(input("Which collumn is the spot on?\n"))
                card1.card[x][y].mark = bool(int(v))
            case 4:
                v = input("What would you like to reassign the spot to?\n")
                x = int(input("Which row is the spot on?\n"))
                y = int(input("Which collumn is the spot on?\n"))
                card1.card[x][y].attribute = v
            case 5:
                name = input("What file name do you want to save it as? (inclode the files extention, IE .txt or similar)\n")
                card1.save(name)
            case 6:
                E = input("Are you sure you wish to exit? (Insert y to exit):\n").lower()
                if E == "y":
                    break

# -----------------------------Main-----------------------------
# --------------------------------------------------------------

main()
