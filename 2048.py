# Used to generate random numbers
from random import *

# Import WConio to handle keypresses and whatnot
import WConio

# Useless nonsense
import types
import math

# Import OS to access ability to flush stdout
import os
clear = lambda: os.system('cls')

'''import ctypes

LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font.nFont = 12
font.dwFontSize.X = 11
font.dwFontSize.Y = 18
font.FontFamily = 54
font.FontWeight = 400
font.FaceName = "Lucida Console"

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        handle, ctypes.c_long(False), ctypes.pointer(font)) '''

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
        pass
    def shiftDown(self):
        pass
    def shiftLeft(self):
        # loop through each row
        for i in range(len(self.grid)):
            # shift the row to the left by sliding down
            row = self.grid[i]
            if not self.isRowBlank(row):
                row = filter(lambda a: a != 0, row)
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
                for k in range(self.width - len(row)):
                    row.insert(0,0)
            self.grid[i] = row
        # pop in a new tile
        self.genTile()
           

# Create Game
board = Game(4,4)
board.set()

# Prints the graphics to the console
def printGraphics(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print '\n'.join(table)

# Enter input loop
key = ' '
while key != 'q':
    # Print the game board
    clear()
    print "2048.py (Use arrow keys. Enter 'q' to quit.)"
    #printGraphics(board.grid)
    for row in board.grid:
        print row

    # Get the key press
    key = WConio.getkey()
    if key == 'up':
        pass
    elif key == 'down':
        pass
    elif key == 'left':
        board.shiftLeft()
    elif key == 'right':
        board.shiftRight()