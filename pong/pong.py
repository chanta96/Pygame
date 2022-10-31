import pygame
pygame.init()
import random

def rand_calc():
    random_number = random.randint(0,1)
    if random_number == 1:
        return -1
    else:
        return 1

#Declaracion de variables
SCREEN_SIZE = (800,600)
PADDLE_ANCHO = (20)
PADDLE_ALTO = (80)
LEFT_PADDLE_LPOSITION = 50 
RIGHT_PADDLE_LPOSITION = 730 #ANCHO - PADDLE_ANCHO/2
HEIGHT_PADDLE_POSITION = 300-PADDLE_ALTO/2
#jug 1
player1_x_coor = LEFT_PADDLE_LPOSITION
player1_y_coor = HEIGHT_PADDLE_POSITION
#velocidad jug1
player1_y_speed = 0

#jug 2
player2_x_coor = RIGHT_PADDLE_LPOSITION
player2_y_coor = HEIGHT_PADDLE_POSITION
#velocidad jug2
player2_y_speed = 0

#coordenadas pelota
pelota_x = 400
pelota_y = 300
pelota_x_speed = 3
pelota_y_speed = 3

#declaracion de colores
BLACK  = (0,0,0)
WHITE = (255,255,255)
RED = (2500,0,0)

#variables de pygame
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
game_over = False

while not game_over:
    #codigo de salida con variable game_over
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True

        if event.type == pygame.KEYDOWN:
            #jugador2
            if event.key == pygame.K_UP:
                player2_y_speed -= 4    
            if event.key == pygame.K_DOWN:
                player2_y_speed += 4
            #jugador1
            if event.key == pygame.K_w:
                player1_y_speed -= 4
            if event.key == pygame.K_s:
                player1_y_speed += 4

        if event.type == pygame.KEYUP:
            #player1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0
    
    #rebote pelota
    if pelota_x <= 0 or pelota_x >= 800:
        pelota_x_speed *= -1
    if pelota_y <= 0 or pelota_y >= 600:
        pelota_y_speed *= -1
    #revisar punto derecho y randomizar reinicio
    #derecha
    if pelota_x >= 740:
        pelota_x = 400
        pelota_x_speed *= rand_calc()
        pelota_y_speed *= rand_calc()
        player1_y_coor = HEIGHT_PADDLE_POSITION
        player2_y_coor = HEIGHT_PADDLE_POSITION
        
    #izquierda
    if pelota_x <= 60:
        pelota_x = 400
        pelota_x_speed *= rand_calc()
        pelota_y_speed *= rand_calc()
        player1_y_coor = HEIGHT_PADDLE_POSITION
        player2_y_coor = HEIGHT_PADDLE_POSITION
        
    #hacer que la pelota sea random en su salida
    #variable random
    

    #movimiento pelota
    pelota_x += pelota_x_speed
    pelota_y += pelota_y_speed

    #movimientos jugadores
    if player1_y_coor <= 0 :
        player1_y_coor = 0
    if player1_y_coor >= 520:
        player1_y_coor = 520
    if player2_y_coor <= 0:
        player2_y_coor = 0
    if player2_y_coor >= 520:
        player2_y_coor = 520

    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed

    screen.fill(BLACK)        
    #zona de dibujo del juego

    #cuadricula
    # if game_over == False:
    #     #vertical
    #     pygame.draw.line(screen, WHITE,(50,0),(50,800))
    #     pygame.draw.line(screen, WHITE,(750,0),(750,800))
    #     #horizontal
    #     pygame.draw.line(screen, WHITE,(0,300),(800,300))
    #     pygame.draw.line(screen, WHITE,(0,260),(800,260))
    #     pygame.draw.line(screen, WHITE,(0,340),(800,340))
    #     #ball vert
    #     pygame.draw.line(screen, WHITE,(400,0),(400,600))

    #paddle drawing
    jugador1 = pygame.draw.rect(screen,WHITE,(player1_x_coor,player1_y_coor,PADDLE_ANCHO,PADDLE_ALTO))
    jugador2 = pygame.draw.rect(screen,WHITE,(player2_x_coor,player2_y_coor,PADDLE_ANCHO,PADDLE_ALTO))
    pelota = pygame.draw.circle(screen,WHITE,(pelota_x,pelota_y),10,10)

    #colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_x_speed *= -1
        

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
