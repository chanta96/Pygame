import pygame
screen_height = 800
screen_width = 600
screen_size = (screen_height,screen_width)
screen = pygame.display.set_mode(screen_size)
done = False
pygame.mouse.set_visible(False)
#fondo
bg_image = pygame.image.load("world.jpg").convert()
#player
player_img = pygame.image.load("ship.png").convert()
player_img.set_colorkey((0,0,0))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos [0]
    mouse_y = mouse_pos [1]

    #mostrando background
    screen.blit(bg_image,[0,0])
    #mostrando player 
    screen.blit(player_img,[mouse_x,mouse_y])
    pygame.display.flip()

pygame.quit()