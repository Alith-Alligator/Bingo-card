import random
from csv import DictReader,DictWriter


# --------------------------------------------------------------
# -----------------------Bingo card class-----------------------
class BingoCard:
    """ A class to reprsent a Bingocard"""

    def __init__(self): #Initate the card with the middle spot as free spot
        self.card = [[{"description":0,"mark":False}, {"description":0,"mark":False}, {"description":0,"mark":False}, {"description":0,"mark":False}, {"description":0,"mark":False}],
                     [{"description":0,"mark":False}, {"description":0,"mark":False}, {"description":0,"mark":False},{"description":0,"mark":False}, {"description":0,"mark":False}],
                     [{"description":0,"mark":False}, {"description":0,"mark":False}, {"description":"Free Spot","mark":True}, {"description":0,"mark":False}, {"description":0,"mark":False}],
                     [{"description":0,"mark":False}, {"description":0,"mark":False}, {"description":0,"mark":False},{"description":0,"mark":False}, {"description":0,"mark":False}],
                     [{"description":0,"mark":False}, {"description":0,"mark":False}, {"description":0,"mark":False}, {"description":0,"mark":False}, {"description":0,"mark":False}]]

    def __repr__(self):
        return self.show()

    def show(self):
        return f"{self.card[0]} \n {self.card[1]} \n {self.card[2]} \n {self.card[3]} \n {self.card[4]} \n"

    def save(self,name):
        with open(name,"w", encoding="UTF-8") as bingos: #Create or Open file to write on
            headers =["description","mark"]
            writer = DictWriter(bingos, fieldnames=headers)
            writer.writeheader()
            for row in self.card:
                for spot in row:
                    writer.writerow(spot)

    def load(self,name): #Load Bingocard from an external file
        try:
            with open(name, "r", encoding="UTF-8") as bingo:
                dataT1 = bingo.readlines()
            dataT2 = [line.split(" -:_j_:- ") for line in dataT1]

            y = 0
            for line in dataT2:
                x = 0
                for spot in line:
                    self.card[y][x]["description"] = spot.split("-:is:-")[0]
                    self.card[y][x]["mark"] = spot.split("-:is:-")[1]

                    x += 1
                y += 1

            print("Bingo card has been loaded successfully")
        except FileNotFoundError:
            print(f"File '{name}' does not exist")
# -----------------------Bingo card class-----------------------
# --------------------------------------------------------------
