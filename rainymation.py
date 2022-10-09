import time
from turtle import circle
import pygame,sys
import random
INITIAL_POSITION_X = [400]
INITIAL_POSITION_Y = [250]
WHITE = (255,255,255)
BLACK = (0,0,0)

pygame.init()

def generate_random_x():
    num = random.randint(0,800)
    return num
     
def generate_random_y():
    num = random.randint(0,500)
    return num
coor_list = []
for i in range (60):
    x = random.randint(0,800)
    y = random.randint(0,500)
    coor_list.append([x,y])

size = (800,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
def derecha ():
    pygame.draw.circle(screen,BLACK,[450,250],5,1)
    pygame.draw.circle(screen,WHITE,[400,250],5,1)
def izquierda():
    pygame.draw.circle(screen,BLACK,[350,250],5,1)
    pygame.draw.circle(screen,WHITE,[400,250],5,1)
def abajo():
    pygame.draw.circle(screen,BLACK,[400,300],5,1)
    pygame.draw.circle(screen,WHITE,[400,250],5,1)
def arriba():
    pygame.draw.circle(screen,BLACK,[400,200],5,1)
    pygame.draw.circle(screen,WHITE,[400,250],5,1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    #logica de programa
    #rain position
    screen.fill(WHITE)
    # for coord in coor_list:
    #     pygame.draw.circle(screen,BLACK,coord,2)
    #     coord[1] += 10
    #     if coord[1] > 500:
    #         coord[1] = 0
    pygame.draw.circle(screen,BLACK,[400,250],5,1)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            pygame.draw.circle(screen,BLACK,[400,200],5,1)
            pygame.draw.circle(screen,WHITE,[400,250],5,1)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            abajo()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            izquierda()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            derecha()
            
#actualizar pantalla 
    pygame.display.flip()
#fps del juego
    clock.tick(60)
