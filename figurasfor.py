from string import whitespace
import time
import pygame
pygame.init()
#definir colores
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
 

#crear ventana
size = [600,400]
screen = pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
        print (event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #color del fondo
    screen.fill(WHITE)
    pygame.draw.line(screen,BLACK,[1,0],[1,400])
    pygame.draw.line(screen,BLACK,[100,0],[100,400])
    pygame.draw.line(screen,BLACK,[200,0],[200,400])
    pygame.draw.line(screen,BLACK,[300,0],[300,400])
    pygame.draw.line(screen,BLACK,[400,0],[400,400])
    pygame.draw.line(screen,BLACK,[500,0],[500,400])
    pygame.draw.line(screen,BLACK,[600,0],[600,400])
    ### ZONA DE DIBUJO
    #                where  color  start and stop   ancho de la linea
    #pygame.draw.line(screen,GREEN,[0,100],[200,500], 5)
    for x in range (100,600,100):
        for y in range (0,400,100):
            pygame.draw.line(screen,RED,[x,y],[x,y],5)
            time.sleep(0.1)
    

    # actualizar pantalla
    pygame.display.flip()