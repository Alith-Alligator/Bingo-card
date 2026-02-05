import random
import json

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

        self._bingo = [[0,0,0,0,0],[0,0,0,0,0],[0,0]] #Rows then Collums then diagonals

    def __repr__(self):
        return self.show()

    def show(self): # Return the bingo card in a readable format ( yes it is ugly)
        self.check_for_bingo()
        return f"{list(self.card[0][0].values())} || {list(self.card[0][1].values())} || {list(self.card[0][2].values())} || {list(self.card[0][3].values())} || {list(self.card[0][4].values())} \n {list(self.card[1][0].values())} || {list(self.card[1][1].values())} || {list(self.card[1][2].values())} || {list(self.card[1][3].values())} || {list(self.card[1][4].values())} \n {list(self.card[2][0].values())} || {list(self.card[2][1].values())} || {list(self.card[2][2].values())} || {list(self.card[2][3].values())} || {list(self.card[2][4].values())} \n {list(self.card[3][0].values())} || {list(self.card[3][1].values())} || {list(self.card[3][2].values())} || {list(self.card[3][3].values())} || {list(self.card[3][4].values())} \n {list(self.card[4][0].values())} || {list(self.card[4][1].values())} || {list(self.card[4][2].values())} || {list(self.card[4][3].values())} || {list(self.card[4][4].values())} \n"

    def check_for_bingo(self):
        for row in range(5): #Rows
            bing = all(self.card[row][collumn]["mark"] for collumn in range(5))
            self._bingo[0][row] = bing
                
        for collumn in range(5): #Collumns
            bing = all(self.card[row][collumn]["mark"] for row in range(5))
            self._bingo[1][collumn] = bing

        bing = all(self.card[i][i]["mark"] for i in range(5)) #First diagonal
        self._bingo[2][0] = bing

        bing = all(self.card[i][4-i]["mark"] for i in range(5)) #Second diagonal
        self._bingo[2][1] = bing

        print(self._bingo)
                
            

    def save(self,name):
        with open(name,"w", encoding="UTF-8") as bingos: #Create or Open file to write on
            json.dump(self.card, bingos)

    def load(self,name): #Load Bingocard from an external file
        try:
            with open(name, "r", encoding="UTF-8") as bingos:
               self.card = json.load(bingos)



            print("Bingo card has been loaded successfully")
        except FileNotFoundError:
            print(f"File '{name}' does not exist")
# -----------------------Bingo card class-----------------------
# --------------------------------------------------------------

















