from random import *
import itertools

class Game():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = []
        for i in range(0, height):
            junk = []
            for k in range(0, width):
                junk.append(0)
            self.grid.append(junk)
    # clears grid
    def wipe(self):
        self.__init__(self.height, self.width)
    # sets grid intially
    def set(self):
        y = randint(0, len(self.grid) - 1)
        x = randint(0, len(self.grid[0]) - 1)
        self.grid[y][x] = 2
        h = randint(0, len(self.grid) - 1)
        k = randint(0, len(self.grid[0]) - 1)
        while(self.grid[h][k] == 2):
            h = randint(0, len(self.grid) - 1)
            k = randint(0, len(self.grid[0]) - 1)
        self.grid[h][k] = 2
    # adds in a new tile
    def genTile(self):
        y = randint(0, len(self.grid) - 1)
        x = randint(0, len(self.grid[0]) - 1)
        while(self.grid[y][x] > 0):
            y = randint(0, len(self.grid) - 1)
            x = randint(0, len(self.grid[0]) - 1)
        self.grid[y][x] = 2
    def isRowBlank(self, row):
        for val in row:
            if val != 0:
                return False
        return True
    def shiftUp(self):
        pass
    def shiftDown(self):
        pass
    def shiftLeft(self):
        # loop through each row
        for i in range(len(self.grid)):
            # shift the row to the left by sliding down
            while self.grid[i][0] == 0 and not self.isRowBlank(self.grid[i]):
                k = []
                for z in range(len(self.grid[i])):
                    if z > 0:
                        k.append(self.grid[i][z])
                k.append(0)
                self.grid[i] = k
        # pop in a new tile
        self.genTile()
    def shiftRight(self):
        # loop through each row
        for i in range(len(self.grid)):
            # shift the row to the left by sliding down
            while self.grid[i][len(self.grid[i]) - 1] == 0 and not self.isRowBlank(self.grid[i]):
                self.grid[i].pop()
                self.grid[i].insert(0, 0)
        # pop in a new tile
        self.genTile()
           

board = Game(4,4)
board.set()

# Print the game board
for row in board.grid:
    print row
    
board.shiftLeft()
print "Did  a left shift"

# Print the game board
for row in board.grid:
    print row

board.shiftRight()
print "Did  a right shift"

# Print the game board
for row in board.grid:
    print row
