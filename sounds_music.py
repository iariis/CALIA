import pygame

# Inicialización de música
pygame.mixer.init()

# Cargar y reproducir música
pygame.mixer.music.load("assets/music.ogg")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops=-1)
