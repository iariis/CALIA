import pygame
from enemies import Meteor  

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/laser1.png")
        self.image.set_colorkey((0, 0, 0))  # BLACK
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

# Función para chequear colisiones
def check_laser_collisions(lasers, meteors, all_sprites, explosion_sound, score, player):
    # Colisión láseres vs meteoritos
    hits = pygame.sprite.groupcollide(meteors, lasers, True, True)
    for hit in hits:
        score[0] += 10
        explosion_sound.play()
        m = Meteor()
        all_sprites.add(m)
        meteors.add(m)

    # Colisión meteoritos vs jugador
    player_hits = pygame.sprite.spritecollide(player, meteors, False)
    if player_hits:
        return True  # El jugador fue golpeado

    return False  # No hubo colisión con el jugador

