import pygame as pg

class Painter:
    gridThickness = 1
    cellSize = 30

    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height

    def __drawGrid(self, cameraPosition):
        for i in range(0, int(self.width/(self.cellSize+self.gridThickness)+2)):
            linePosX = i*(self.cellSize+self.gridThickness) - cameraPosition[0]%(self.cellSize+1)
            linePosY = i*(self.cellSize+self.gridThickness) - cameraPosition[1]%(self.cellSize+1)
            pg.draw.rect(self.window, pg.Color("white"), ( (linePosX , 0), (self.gridThickness, self.height) ) )
            pg.draw.rect(self.window, pg.Color("white"), ( (0 , linePosY), (self.width, self.gridThickness) ) )

    
    def __drawCells(self, cells, cameraPosition):
        for cell in cells:
            cellPos = (cell[0]*(self.cellSize+self.gridThickness)+self.gridThickness-cameraPosition[0], cell[1]*(self.cellSize+self.gridThickness)+self.gridThickness-cameraPosition[1])
            pg.draw.rect(self.window, pg.Color("white"), ( (cellPos[0], cellPos[1]), (self.cellSize, self.cellSize) ))

    def draw(self, cells, cameraPosition):
        self.window.fill(pg.Color("black"))
        self.__drawGrid(cameraPosition)
        self.__drawCells(cells, cameraPosition)
        pg.display.flip()