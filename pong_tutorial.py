import random
import pygame,sys
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)

size = (800,600)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

#const size of players
PLAYER_HEIGHT = 80
PLAYER_WIDTH = 15
#coords j1 y speed p1
p1_coord_x = 750
p1_coord_y = 300 - 45
speed_y_p1 = 0
#coords j2 y speed p2
p2_coord_x = 35
p2_coord_y = 300 - 45
speed_y_p2 = 0
#ball size and speed
coord_ball_x = 400
coord_ball_y = 300
ball_speed_x = 3
ball_speed_y = 3

def check_ball(coord_ball_y,ball_speed_y):
    if coord_ball_y >= 600 or coord_ball_y <= 0:
        ball_speed_y *= -1
    return ball_speed_y

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    screen.fill(BLACK)

    #reiniciar pelota al salir a los costados
    # if coord_ball_x <=0 or coord_ball_x >=800:
    #     coord_ball_x,coord_ball_y = 800,300
    #     ball_speed_x *= random.randint(-1,1)
    #     ball_speed_y *= random.randint(-1,1)

    #movement of the ball
    # check_ball(coord_ball_y,ball_speed_y)
    if coord_ball_y <= 0 or coord_ball_y >= 600:
        ball_speed_y*=-1
    if coord_ball_x <= 0 or coord_ball_x >= 800:
        coord_ball_x,coord_ball_y = 400,300
        rand= random.randint(1,3)
        if rand != 2:
            ball_speed_x *= -1
            ball_speed_y *= -1

    coord_ball_x += ball_speed_x
    coord_ball_y += ball_speed_y 
    
    #drawing the ball
    ball = pygame.draw.circle(screen,WHITE,(coord_ball_x,coord_ball_y),7,10)
    #dibujando paletas
    jugador1 = pygame.draw.rect(screen,(WHITE),(p1_coord_x,p1_coord_y,PLAYER_WIDTH,PLAYER_HEIGHT))
    jugador2 = pygame.draw.rect(screen,(WHITE),(p2_coord_x,p2_coord_y,PLAYER_WIDTH,PLAYER_HEIGHT))


    pygame.display.flip()
    clock.tick(60)