
import pygame, sys
pygame.init()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
size = (800,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
#dejar de ver puntero de mouse
pygame.mouse.set_visible(False)
coord_x = 10
coord_y = 10
x_speed = 0
y_speed = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    #empieza el programa            
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            y_speed = -3
        if event.key == pygame.K_DOWN:
            y_speed = 3
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            y_speed = 0
        if event.key == pygame.K_DOWN:
            y_speed = 0
        
    coord_x += x_speed
    coord_y += y_speed
    
    screen.fill(white)
    # pygame.draw.rect(screen, red, (x,y,100,100))
    # pygame.draw.circle(screen,red,(x,250),1,1)
    pygame.draw.rect(screen,red ,(coord_x,coord_y,100,100))

    #fin codigo
    pygame.display.update()
    clock.tick(60)