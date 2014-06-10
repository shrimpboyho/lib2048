# Used to generate random numbers
from random import *

# Main game class
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
        # loop through each column
        for i in range(self.width):
            row = self.getColumn(i)
            # shift the row to the left by sliding down
            if not self.isRowBlank(row):
                row = filter(lambda a: a != 0, row)
                for z in range(len(row)):
                    if(z + 1  < len(row)):
                        if (row[z] == row[z + 1]):
                            row[z] += row[z + 1]
                            row.pop(z + 1) 
                for k in range(self.width - len(row)):
                    row.append(0)
            self.setColumn(i, row)
        # pop in a new tile
        self.genTile()
    def shiftDown(self):
        # loop through each row
        for i in range(self.width):
            # shift the row to the right by sliding down
            row = self.getColumn(i)
            if not self.isRowBlank(row):
                row = filter(lambda a: a != 0, row)
                row.reverse()
                for z in range(len(row)):
                    if(z + 1  < len(row)):
                        if (row[z] == row[z + 1]):
                            row[z] += row[z + 1]
                            row.pop(z + 1)
                row.reverse()
                for k in range(self.width - len(row)):
                    row.insert(0,0)
            self.setColumn(i, row)
        # pop in a new tile
        self.genTile()
    def shiftLeft(self):
        # loop through each row
        for i in range(len(self.grid)):
            # shift the row to the left by sliding down
            row = self.grid[i]
            if not self.isRowBlank(row):
                row = filter(lambda a: a != 0, row)
                for z in range(len(row)):
                    if(z + 1  < len(row)):
                        if (row[z] == row[z + 1]):
                            row[z] += row[z + 1]
                            row.pop(z + 1) 
                for k in range(self.width - len(row)):
                    row.append(0)
            self.grid[i] = row
        # pop in a new tile
        self.genTile()
    def shiftRight(self):
        # loop through each row
        for i in range(len(self.grid)):
            # shift the row to the right by sliding down
            row = self.grid[i]
            if not self.isRowBlank(row):
                row = filter(lambda a: a != 0, row)
                row.reverse()
                for z in range(len(row)):
                    if(z + 1  < len(row)):
                        if (row[z] == row[z + 1]):
                            row[z] += row[z + 1]
                            row.pop(z + 1)
                row.reverse()
                for k in range(self.width - len(row)):
                    row.insert(0,0)
            self.grid[i] = row
        # pop in a new tile
        self.genTile()
    # Returns a column
    def getColumn(self, index):
        z = []
        for row in self.grid:
            z.append(row[index])
        return z
    # Sets a column
    def setColumn(self, index, column):
        for i in range(len(self.grid)):
            self.grid[i][index] = column[i]