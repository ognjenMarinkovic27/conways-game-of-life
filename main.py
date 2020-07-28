from painter import Painter
import pygame as pg

(width, height) = (800, 600)

window = pg.display.set_mode((width, height))

clock = pg.time.Clock()

painter = Painter(window, width, height)

cells = set([(0, 0) , (5, 4)])

cameraPosition = (0,0)

mousePressed = False

running = True
while running:

    painter.draw(cells, cameraPosition)
    
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
        cameraPosition = (cameraPosition[0]+mouseMove[0], cameraPosition[1]+mouseMove[1])