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
    ### ZONA DE DIBUJO
    #                where  color  start and stop   ancho de la linea
    pygame.draw.line(screen,GREEN,[0,100],[200,500], 5)
    pygame.draw.rect(screen,RED,[100,100,80,80], 5)
    pygame.draw.circle(screen,BLACK,[300,200],25,3)
    # actualizar pantalla
    pygame.display.flip()