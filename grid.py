class Grid:

    def __init__(self):
        self.__cellMap = {(3, 1): 0}

    def addCell(self, x_y):
        x, y = x_y
        self.__cellMap[(x, y)] = 0
        if((x-1, y-1) in self.__cellMap):
            self.__cellMap[(x, y)]+=1
            self.__cellMap[(x-1, y-1)]+=1
        if((x, y-1) in self.__cellMap):
            self.__cellMap[(x, y)]+=1
            self.__cellMap[(x, y-1)]+=1
        if((x+1, y-1) in self.__cellMap):
            self.__cellMap[(x, y)]+=1
            self.__cellMap[(x+1, y-1)]+=1
        if((x-1, y) in self.__cellMap):
            self.__cellMap[(x, y)]+=1
            self.__cellMap[(x-1, y)]+=1
        if((x+1, y) in self.__cellMap):
            self.__cellMap[(x, y)]+=1
            self.__cellMap[(x+1, y)]+=1
        if((x-1, y+1) in self.__cellMap):
            self.__cellMap[(x, y)]+=1
            self.__cellMap[(x-1, y+1)]+=1
        if((x, y+1) in self.__cellMap):
            self.__cellMap[(x, y)]+=1
            self.__cellMap[(x, y+1)]+=1
        if((x+1, y+1) in self.__cellMap):
            self.__cellMap[(x, y)]+=1
            self.__cellMap[(x+1, y+1)]+=1

    def removeCell(self, x_y):
        x, y = x_y
        del self.__cellMap[(x, y)]
       
    def getCells(self):
        return self.__cellMap
 
    