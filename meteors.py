import pygame, random
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
# Lista de imágenes de meteoritos
meteor_images = [
    "assets/meteorGrey_big2.png",
    "assets/meteorGrey_big3.png",
    "assets/meteorGrey_big4.png",
    "assets/meteorGrey_med1.png",
    "assets/meteorGrey_med2.png",
    "assets/meteorGrey_small1.png",
    "assets/meteorGrey_small2.png",
    "assets/meteorGrey_tiny1.png",
    "assets/meteorGrey_tiny2.png"
]
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img_path = random.choice(meteor_images)
        self.image = pygame.image.load(img_path).convert()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(WIDTH-self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speedy=random.randrange(1,10)
        
    def update(self):
        self.react.y+=self.speedy
        
        