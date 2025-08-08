import pygame
import sounds_music

from explosions import Explosion
from meteors import Meteor  # Importá Meteor para poder crear nuevos

def check_laser_collisions(bullets, meteor_list, all_sprites, player, score, explosion_anim):
    # Colisión entre balas y meteoritos
    collisions = pygame.sprite.groupcollide(meteor_list, bullets, True, True)
    for meteor in collisions:
        score[0] += 10  # Aumenta el puntaje
        explosion = Explosion(meteor.rect.center, explosion_anim)
        all_sprites.add(explosion)
        sounds_music.explosion_sound.play()

        # Crear un nuevo meteoro para reemplazar el destruido
        new_meteor = Meteor()
        all_sprites.add(new_meteor)
        meteor_list.add(new_meteor)

    # Colisión entre meteoritos y el jugador
    if pygame.sprite.spritecollideany(player, meteor_list):
        return True

    return False
