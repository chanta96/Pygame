import random
import pygame,sys
from pygame import mixer
pygame.init()
black = (0,0,0)
white = (255,255,255)
size = (800,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
#musica
mixer.music.load('ball_sound.wav')
fallo_ia = 0

#numero1:

def numero1():
    pygame.draw.line(screen,white,(320,100),(350,50),3)
    pygame.draw.line(screen,white,(350,50),(350,150),3)

def numero2():
    pygame.draw.line(screen,white,(320,100),(380,100),3)
#p1
pos_x_p1 = 50
pos_y_p1 = 200
speed_y_p1 = 0
#p2
pos_x_p2 = 700
pos_y_p2 = 200
speed_y_p2 = 0
#ball position:
ball_x = 400
ball_y = 250
speed_ball_x = 3
speed_ball_y = 3
puntos_p1 = 0
puntos_p2 = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    
    #movimiento p1
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            speed_y_p1 = -3
        if event.key == pygame.K_DOWN:
            speed_y_p1 = 3
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            speed_y_p1 = 0
        if event.key == pygame.K_DOWN:
            speed_y_p1 = 0
    pos_y_p1 += speed_y_p1
    
    #movimiento paleta 2 ia\
    #check ball goes to the ia 
    fallo_ia = random.randint(1,100)
    if fallo_ia == 100:
        pygame.draw.rect(screen,white, (200,200,20,20),1,5)
    if (fallo_ia >= 1 and fallo_ia <= 98) and speed_ball_x > 0:
        #check if ball is up or below the padel
        if ball_y > pos_y_p2-40:
            pos_y_p2 += 3
        if ball_y < pos_y_p2+40:
            pos_y_p2 -= 3
    else:
        if speed_ball_x > 0:
            if ball_y > pos_y_p2-40:
                pos_y_p2 += 2
            if ball_y < pos_y_p2+40:
                pos_y_p2 -= 2
    #no superar limites con paleta superior e inferior
    if pos_y_p1 <= 0:
        pos_y_p1 = 0
    if pos_y_p1 >= 420:
        pos_y_p1 = 420
    if pos_y_p2<=0:
        pos_y_p2 = 0
    if pos_y_p2 >= 420:
        pos_y_p2 = 420

    #rebote de la pelota
    if ball_x <=0 or ball_x >= 800:
        ball_x = 400
        ball_y = 250
        speed_ball_x *= -1
        speed_ball_y *= -1

    if ball_y <= 0 or ball_y >= 500:
        speed_ball_y *= -1

    #rebote contra paleta izquierda
    if ball_x == pos_x_p1+20:
        if ball_y >= pos_y_p1 and ball_y <= pos_y_p1+80:
            speed_ball_x *=-1
            mixer.music.play(1)
    #rebote paleta derecha
    if ball_x == pos_x_p2:
        if ball_y >= pos_y_p2 and ball_y <= pos_y_p2+80:
            speed_ball_x *= -1
            mixer.music.play(1)
    
    #movimiento ball
    ball_x += speed_ball_x
    ball_y += speed_ball_y
    screen.fill(black)

    #dibujo paletas                     x     y   ancho alto
    pygame.draw.rect(screen,white,(pos_x_p1,pos_y_p1,20,80))
    pygame.draw.rect(screen, white,(pos_x_p2,pos_y_p2,20,80))
    #dibujo pelota
    pygame.draw.circle(screen, white,(ball_x,ball_y),10,10)
    #dibujo linea
    pygame.draw.line(screen, white,(400,0),(400,500),2)
    #numeros
    
    
    
    pygame.display.update()
    clock.tick(100)
