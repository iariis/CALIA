import pygame
from bullet import Bullet
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
class Player(pygame.sprite.Sprite):
    def __init__(self, all_sprites, bullets):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert_alpha() 
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed = 5
        self.bullets = bullets
        self.all_sprites = all_sprites
        self.laser_sound = pygame.mixer.Sound("assets\laser5.ogg")
        self.laser_sound.set_volume(0.3) 
        all_sprites.add(self)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.all_sprites.add(bullet)  # Ahora se dibuja y actualiza
        self.bullets.add(bullet)
        self.laser_sound.play()