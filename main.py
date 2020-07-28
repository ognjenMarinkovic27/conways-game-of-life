from painter import Painter
from grid import Grid
import pygame as pg

(width, height) = (800, 600)
window = pg.display.set_mode((width, height))
clock = pg.time.Clock()

painter = Painter(window, width, height)
grid = Grid()

grid.addCell((5,5))
grid.addCell((4,1))

cameraPosition = (0,0)
mousePressed = False

running = True
while running:

    painter.draw(grid.getCells(), cameraPosition)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mousePressed = True
        elif event.type == pg.MOUSEBUTTONUP:
            mousePressed = False

    clock.tick(60)


    mouseMove = pg.mouse.get_rel()
    if(mousePressed):
        cameraPosition = (cameraPosition[0]-mouseMove[0], cameraPosition[1]-mouseMove[1])