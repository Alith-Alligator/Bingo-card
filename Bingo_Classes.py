import random
from csv import DictReader,DictWriter

# --------------------------------------------------------------
# -----------------------Bingo spot class-----------------------
class BingoSpot:
    """A class to reprsent Spots on a bingocard"""

    def __init__(self, desc = 0, mark = False): # Initiate every spot
        self._dictio = {
            "Description":desc,
            "Mark":mark}

    def __repr__(self):
        return f"{self._dictio["Description"]}-:is:-{self._dictio["Mark"]}"

    def keys(self):
        return self._dictio.keys()
    
    def get(self,key,default = None):
        return self._dictio.get(key, default)

# mark property
    @property
    def mark(self):
        return self._dictio["Mark"]

    @mark.setter
    def mark(self,value):
        self._dictio["Mark"] = value

# Description property
    @property
    def description(self):
        return  self._dictio["Description"]

    @description.setter
    def description(self,value): #Set property
        self._dictio["Description"] = value

# Spot Dictionary
    @property
    def dictio(self):
        return self._dictio

    @description.setter
    def dictio(self,value): #Set property
        pass
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

    def save(self,name):
        with open(name,"w", encoding="UTF-8") as bingos: #Create or Open file to write on
            headers =["Description","Mark"]
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
                    self.card[y][x].description = spot.split("-:is:-")[0]
                    self.card[y][x].mark = spot.split("-:is:-")[1]

                    x += 1
                y += 1

            print("Bingo card has been loaded successfully")
        except FileNotFoundError:
            print(f"File '{name}' does not exist")
# -----------------------Bingo card class-----------------------
# --------------------------------------------------------------
