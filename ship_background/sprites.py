import pygame
import random
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)

class Disparo(pygame.sprite.Sprite):
    pass

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.y +=1 
        if self.rect.y >= 720:
            self.rect.y = -10
            self.rect.x = random.randrange(600)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
    
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = mouse_pos[1]

screen = pygame.display.set_mode([720,720])
clock = pygame.time.Clock()
done = False
#lista vacia de sprites
meteor_lista = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

player = Player()
all_sprite_list.add(player)
score = 0
for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(900)
    meteor.rect.y = random.randrange(600)
    meteor_lista.add(meteor)
    all_sprite_list.add(meteor)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    meteor_hit_list = pygame.sprite.spritecollide(player, meteor_lista,True)
    
    all_sprite_list.update()

    for meteor in meteor_hit_list:
        score+=1
        print(score) 
    

    screen.fill(WHITE)
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()