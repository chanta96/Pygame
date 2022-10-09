import pygame,sys

pygame.init()
pygame.font.init()
text_font = pygame.font.SysFont("monospace",20)
clock = pygame.time.Clock()

widht = 800
height = 500

screen = pygame.display.set_mode((widht, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255,255,255))
    for i in range(0, 10):
        text =text_font.render(f'{i}',1,(0,0,0))
        screen.blit(text,(200,200))
    
    
    pygame.display.update()
    clock.tick(60)