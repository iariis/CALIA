import pygame

def check_laser_collisions(bullets, meteor_list, all_sprites, player_group, player, score):
    # Colisión entre balas y meteoritos
    collisions = pygame.sprite.groupcollide(meteor_list, bullets, True, True)
    for meteor in collisions:
        score[0] += 10  # Aumenta el puntaje cuando se destruye un meteorito

    # Colisión entre meteoritos y el jugador
    if pygame.sprite.spritecollideany(player, meteor_list):
        return True  # Si el jugador fue alcanzado, devolver True

    return False
