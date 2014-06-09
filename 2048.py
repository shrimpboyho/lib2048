class Game():
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
    def shiftUp(self):
        pass
    def shiftDown(self):
        pass
    def shiftLeft(self):
        pass
    def shiftRight(self):
        pass
           
    
board = Game(4,4)
board.set()

# Print the game board
for row in board.grid:
    print row
