import pygame as pg
import math

class Painter:

    def __init__(self, window, width, height):
        self.__window = window
        self.__width = width
        self.__height = height
        self.__gridThickness = 1
        self.__cellSize = 15
        self.__zoomMultiplier = 1
        self.__showGrid = True

    def __drawGrid(self, cameraPosition):
        actuallCellSize = math.ceil(self.__cellSize*self.__zoomMultiplier)

        for i in range(0, int(self.__width/(actuallCellSize+self.__gridThickness)+2)):
            linePosX = i*(actuallCellSize+self.__gridThickness) - cameraPosition[0]%(actuallCellSize+1)
            linePosY = i*(actuallCellSize+self.__gridThickness) - cameraPosition[1]%(actuallCellSize+1)
            pg.draw.rect(self.__window, pg.Color("#C0C0C0"), ( (linePosX , 0), (self.__gridThickness, self.__height) ) )
            pg.draw.rect(self.__window, pg.Color("#C0C0C0"), ( (0 , linePosY), (self.__width, self.__gridThickness) ) )

    
    def __drawCells(self, cells, cameraPosition):
        actuallCellSize = math.ceil(self.__cellSize*self.__zoomMultiplier)

        for cell in cells:
            cellPos = (cell[0]*(actuallCellSize+self.__gridThickness)+self.__gridThickness-cameraPosition[0], cell[1]*(actuallCellSize+self.__gridThickness)+self.__gridThickness-cameraPosition[1])
            pg.draw.rect(self.__window, pg.Color("yellow"), ( (cellPos[0], cellPos[1]), (actuallCellSize, actuallCellSize) ))

    def draw(self, cells, cameraPosition):
        self.__window.fill(pg.Color("black"))
        if(self.__showGrid):
            self.__drawGrid(cameraPosition)
        self.__drawCells(cells, cameraPosition)
        pg.display.flip()

    def ZoomIn(self):
        self.__zoomMultiplier = min(2, self.__zoomMultiplier+0.25)

    def ZoomOut(self):
        self.__zoomMultiplier = max(0.5, self.__zoomMultiplier-0.25)

    def getActualCellSize(self):
        return self.__cellSize*self.__zoomMultiplier

    def getGridThickness(self):
        return self.__gridThickness