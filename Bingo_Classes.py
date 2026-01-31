import random

# --------------------------------------------------------------
# -----------------------Bingo spot class-----------------------
class BingoSpot:
    """A class to reprsent Spots on a bingocard"""

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
    """ A class to reprsent a Bingocard"""

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
