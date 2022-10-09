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
size = [800,500]
screen = pygame.display.set_mode(size)
#coordenadas
cord_x = 400
cord_y = 200
#velocidad cuadrado
speed_x = 3
speed_y = 3

#controlar time
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        print (event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #logica del juego y animaciones
    if cord_x > 780 or cord_x < 0:
        speed_x *= -1
    if cord_y > 480 or cord_y < 0:
        speed_y *= -1

    cord_x += speed_x
    cord_y += speed_y



    #color del fondo
    screen.fill(WHITE)
    ### ZONA DE DIBUJO
    #                where  color  start and stop   ancho de la linea
    pygame.draw.circle(screen,GREEN,(cord_x+20,cord_y+20),30,5)
    pygame.draw.rect(screen,RED,(cord_x,cord_y,40,40))
    
    # actualizar pantalla
    pygame.display.flip()
    clock.tick(60)