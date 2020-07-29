from painter import Painter
from grid import Grid
import pygame as pg
import math

(width, height) = (800, 600)
window = pg.display.set_mode((width, height))
clock = pg.time.Clock()

painter = Painter(window, width, height)
grid = Grid()


cameraPosition = (0,0)
mousePressed = False

running = True
simulate = False

framesPerStep = 5

framesToNextStep = framesPerStep

tools = ("Move Tool", "Edit Tool")
toolIndex = 1

while running:

    painter.draw(grid.getCells(), cameraPosition)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            if(event.button == 1):
                if(toolIndex == 1):
                    mousePressed = True
                elif(toolIndex == 2):
                    pos = pg.mouse.get_pos()
                    actualCellSize = painter.getActualCellSize()
                    gridThickness = painter.getGridThickness()
                    x = int((pos[0]+cameraPosition[0])/(math.ceil(actualCellSize)+gridThickness))
                    y = int((pos[1]+cameraPosition[1])/(math.ceil(actualCellSize)+gridThickness))
                    if(grid.isCellLive((x, y))):
                        grid.removeCell((x, y))
                    else:
                        grid.addCell((x, y))
            if(event.button == 4):
                painter.ZoomIn()
            if(event.button == 5):
                painter.ZoomOut()

        elif event.type == pg.MOUSEBUTTONUP:
            if(event.button == 1):
                mousePressed = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                simulate = not simulate
            elif event.key == pg.K_1:
                toolIndex = 1
            elif event.key == pg.K_2:
                toolIndex = 2
            elif event.key == pg.K_g:
                painter.toggleGrid()

    clock.tick(60)

    if(simulate):
        if(framesToNextStep == 0):
            grid.nextState()
            framesToNextStep = framesPerStep
        framesToNextStep-=1

    mouseMove = pg.mouse.get_rel()
    if(mousePressed):
        cameraPosition = (cameraPosition[0]-mouseMove[0], cameraPosition[1]-mouseMove[1])