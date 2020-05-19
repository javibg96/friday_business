# juego de la vida hecho para testear pygame y por pura curiosidad del juego
# explicado paso a paso en https://www.youtube.com/watch?v=qPtKv9fSHZY por DotCSV

"""
Created on Mon May 20 20:04:11 2020
@author: Javier Blasco
"""

import pygame
import numpy as np
import time

width, height = 800, 800
nX, nY = 80, 80
xSize = width / nX
ySize = height / nY

pygame.init()  # Initialize PyGame

screen = pygame.display.set_mode([width, height])  # Set size of screen

BG_COLOR = (10, 10, 10)  # Define background color
color_vivas = (255, 255, 255)
color_muertas = (128, 128, 128)
# Celdas vivas = 1; Celdas muertas = 0
status = np.zeros((nX, nY))  # Intialize status of cells

pauseRun = False

running = True
while running:

    newStatus = np.copy(status)  # copias el estado anterior

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            pauseRun = not pauseRun

        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            x, y = int(np.floor(posX / xSize)), int(np.floor(posY / ySize))
            # newStatus[x,y] = np.abs(newStatus[x,y]-1)
            newStatus[x, y] = not mouseClick[2]

    screen.fill(BG_COLOR)  # Clean background

    for x in range(0, nX):
        for y in range(0, nY):

            if not pauseRun:

                # Numero de vecinos, los %N son para hacer el "toroide", sales por un lado entras por el otro, sales por
                # arriba vuelves por debajo
                nNeigh = status[(x - 1) % nX, (y - 1) % nY] + status[(x) % nX, (y - 1) % nY] + \
                         status[(x + 1) % nX, (y - 1) % nY] + status[(x - 1) % nX, (y) % nY] + \
                         status[(x + 1) % nX, (y) % nY] + status[(x - 1) % nX, (y + 1) % nY] + \
                         status[(x) % nX, (y + 1) % nY] + status[(x + 1) % nX, (y + 1) % nY]

                # Rule 1: Una celula muerta con 3 vecinas "revive"
                if status[x, y] == 0 and nNeigh == 3:
                    newStatus[x, y] = 1

                # Rule 2: Una celula viva con mas de 3 vecinos o menos de 2 muere
                elif status[x, y] == 1 and (nNeigh < 2 or nNeigh > 3):
                    newStatus[x, y] = 0

            poly = [(x * xSize, y * ySize),
                    ((x + 1) * xSize, y * ySize),
                    ((x + 1) * xSize, (y + 1) * ySize),
                    (x * xSize, (y + 1) * ySize)]

            if newStatus[x, y] == 1:
                pygame.draw.polygon(screen, color_vivas, poly, 0)
            else:
                pygame.draw.polygon(screen, color_muertas, poly, 1)

    status = np.copy(newStatus)
    time.sleep(0.1)
    pygame.display.flip()

pygame.quit()
