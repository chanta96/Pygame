import pygame
screen_height = 720
screen_width = 720
screen_size = (screen_height,screen_width)
screen = pygame.display.set_mode(screen_size)
done = False
pygame.mouse.set_visible(False)
#fondo
bg_image = pygame.image.load("background.png").convert()
#player
player_img = pygame.image.load("player.png").convert()
player_img.set_colorkey((0,0,0))
#enemy
enemy_img = pygame.image.load("meteor.png").convert()
enemy_img.set_colorkey((0,0,0))
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
    player = screen.blit(player_img,[mouse_x,mouse_y])
    
    ball = pygame.draw.circle(screen,(255,0,0),(mouse_x+22,mouse_y-20),10,10)
    enemy = screen.blit(enemy_img,(20,200))
    
    pygame.display.flip()
    
pygame.quit()