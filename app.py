import pygame
from player import Player
from enemies import Meteor
from bullet import Bullet

WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter")
clock = pygame.time.Clock()

background = pygame.image.load("assets/background.png").convert()

all_sprites = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player(all_sprites, bullets)
all_sprites.add(player)

for i in range(8):
    meteor = Meteor()
    all_sprites.add(meteor)
    meteor_list.add(meteor)

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    # Colisiones meteoro - laser
    hits = pygame.sprite.groupcollide(meteor_list, bullets, True, True)
    for hit in hits:
        meteor = Meteor()
        all_sprites.add(meteor)
        meteor_list.add(meteor)

    # Colisiones jugador - meteoro
    hits = pygame.sprite.spritecollide(player, meteor_list, False)
    if hits:
        running = False

    screen.blit(background, [0, 0])
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
