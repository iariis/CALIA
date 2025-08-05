import pygame
from bullet import Bullet
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
class Player(pygame.sprite.Sprite):
    def __init__(self, all_sprites, bullets):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert_alpha()  # ← usá una imagen de nave
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed = 5
        self.bullets = bullets
        all_sprites.add(self)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.bullets.add(bullet)
