import random
import pygame,sys
pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)
WHITE =(255,255,255)
BLACK = (0,0,0)
clock = pygame.time.Clock()
rand_x = random.randint(0,800)
rand_y = random.randint(0,600)


while True:
    lista_random = []
    lista_random2 = []
    for i in range(1,10):
        lista_random.append(random.randint(0,800))
        lista_random2.append(random.randint(0,600))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    screen.fill(BLACK)
    for i in range(9):
        pygame.draw.circle(screen,WHITE,(lista_random[i],lista_random2[i]),8,8)
    pygame.display.update()
    clock.tick(60)
