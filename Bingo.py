import random

# --------------------------------------------------------------
# -----------------------Bingo spot class-----------------------
class BingoSpot:

    def __init__(self, desc = 0, mark = False): # Initiate every spot
        self.Description = desc
        self.marked = mark

    def __repr__(self):
        return f"{self.Description}-:is:-{self.marked}"

# mark property
    @property
    def mark(self):
        return self.marked

    @mark.setter
    def mark(self,Value):
        self.marked = Value

# Description property
    @property
    def description(self):
        return  self.Description

    @description.setter
    def description(self,value): #Set property
        self.Description = value
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
        return self.show()

    def show(self):
        return f"{self.card[0]} \n {self.card[1]} \n {self.card[2]} \n {self.card[3]} \n {self.card[4]} \n"

    def save(self,name): # Save the Bingocard into an external file
        text_trans =" \n".join([" -:_j_:- ".join([str(spot) for spot in row]) for row in self.card]) #Transform the card variable into a savable string

        with open(name,"w", encoding="UTF-8") as bingo: # save it into a file
            bingo.write(text_trans)
        print("Bingo card has been saved successfullu")

    def load(self,name): #Load Bingocard from an external file
        try:
            with open(name, "r", encoding="UTF-8") as bingo:
                dataT1 = bingo.readlines()
            dataT2 = [line.split(" -:_j_:- ") for line in dataT1]

            y = 0
            for line in dataT2:
                x = 0
                for spot in line:
                    self.card[y][x].description = spot.split("-:is:-")[0]
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
def CoL(card1): #Creation or load

    while (True): # While loop to make sure user chooses to load or to start a new card

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
                            card1.card[i][j].description = random.choice(templist)
                            templist.remove(card1.card[i][j].description)

                case 'n':
                    for i in range(5):
                        for j in range(5):
                            if i == 2 and j == 2:
                                continue
                            card1.card[i][j].description = input(f"{i+1},{j+1} - ")

# -----------------------Creation or Load-----------------------
# --------------------------------------------------------------


# --------------------------------------------------------------
# -----------------------------Main-----------------------------
def main():
    card1 = BingoCard()
    while(True):
        choice = input("What would you like to do?\n 1- Print card\n 2- Load or create a card\n 3- Mark a spot\n 4- Reassign a spot\n 5- Save the Bingo card\n 6- Exit the program\n")

        match int(choice):
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
                card1.card[x][y].description = v
            case 5:
                name = input("What file name do you want to save it as? (inclode the files extention, IE .txt or similar)\n")
                card1.save(name)
            case 6:
                e = input("Are you sure you wish to exit? (Insert y to exit):\n").lower()
                if e == "y":
                    break

# -----------------------------Main-----------------------------
# --------------------------------------------------------------

if __name__ == "__main__":
    main()
