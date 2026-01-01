import random
# Make a 5 item list [ representing the rows ] with each item being a 5 item list [representing the collumns ] | DONE
# Allow user to enter 24 items, one in each spot, and have the middle (3,3) spot be a free spot and already marked. | DONE
# Allow the user to either insert the items in the spots they want, or allocate them randomly. | DONE
# make it all work with classes instead of lists [ class for bingo cards and class for spots?] |Kinda done
# Storage
# Allow user to mark spots


class BingoSpot: #Class to keep track of everybingo spot
    markedSpots = 1

    def __init__(self, attribute = 0, mark = False): # Initiate every spot 
        self.Attribute = attribute
        self.marked = mark

    def __repr__(self):
        return f"{self.Attribute} -:is:- {self.marked}"

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
    def attribute(Self):
        return  self.Attribute

    @attribute.setter
    def attribute(self,Value): #Set property
        self.Attribute = Value


class BingoCard:
    def __init__(self): #Initate the card with the middle spot as free spot
        self.card = [[BingoSpot(), BingoSpot(), BingoSpot(), BingoSpot(), BingoSpot()],
                     [BingoSpot(), BingoSpot(), BingoSpot(),BingoSpot(), BingoSpot()],
                     [BingoSpot(), BingoSpot(), BingoSpot("Free Spot", True), BingoSpot(), BingoSpot()],
                     [BingoSpot(), BingoSpot(), BingoSpot(),BingoSpot(), BingoSpot()],
                     [BingoSpot(), BingoSpot(), BingoSpot(), BingoSpot(), BingoSpot()]]


    def __repr__(self):
        return self.card

    def show(self):
        return f"{self.card[0]} \n {self.card[1]} \n {self.card[2]} \n {self.card[3]} \n {self.card[4]} \n"






card1 = BingoCard()


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
                card1.card[i][j] = random.choice(templist)
                templist.remove(card1.card[i][j])

    case 'n':
        for i in range(5):
            for j in range(5):
                if i == 2 and j == 2:
                    continue
                card1.card[i][j] = input(f"{i+1},{j+1} - ")


print(card1.show())
