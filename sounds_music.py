# sounds_music.py
import pygame

pygame.mixer.init()

# Música de fondo
pygame.mixer.music.load("assets/music.ogg")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops=-1)

# Sonido de explosión
explosion_sound = pygame.mixer.Sound("assets/assets_explosion.wav")
explosion_sound.set_volume(0.5)  # Ajusta volumen a gusto
