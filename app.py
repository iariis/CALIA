import pygame
import sounds_music
from player import Player
from meteors import Meteor
from explosions import Explosion
from laser_collisions import check_laser_collisions

# Dimensiones de la ventana
WIDTH = 800
HEIGHT = 600

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CALI")
clock = pygame.time.Clock()
background = pygame.image.load("assets/background.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Cargar animaciones de explosión
explosion_anim = []
for i in range(9):
    file = f"assets/regularExplosion0{i}.png"
    img = pygame.image.load(file).convert()
    img.set_colorkey((0, 0, 0))
    img_scale = pygame.transform.scale(img, (70, 70))
    explosion_anim.append(img_scale)

def show_start_screen():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 74)
    text = font.render("Press Enter to Play", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

def show_game_over_screen(shots_fired, collision_count, score):
    screen.fill((0, 0, 0))
    font_big = pygame.font.Font(None, 74)
    font_small = pygame.font.Font(None, 36)

    text = font_big.render("GAME OVER", True, (255, 0, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(text, text_rect)

    shots_text = font_small.render(f"Disparos: {shots_fired}", True, (255, 255, 255))
    shots_rect = shots_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
    screen.blit(shots_text, shots_rect)

    collision_text = font_small.render(f"Colisiones: {collision_count}", True, (255, 255, 255))
    collision_rect = collision_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(collision_text, collision_rect)

    score_text = font_small.render(f"Puntos: {score[0]}", True, (255, 255, 0))
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
    screen.blit(score_text, score_rect)

    restart_text = font_small.render("Presiona R para reiniciar", True, (255, 255, 255))
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4 - 20))
    screen.blit(restart_text, restart_rect)

    quit_text = font_small.render("Presiona Q para salir", True, (255, 255, 255))
    quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4 + 20))
    screen.blit(quit_text, quit_rect)

    pygame.display.flip()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "restart"
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

def show_victory_screen(shots_fired, collision_count, score):
    screen.fill((0, 0, 0))
    font_big = pygame.font.Font(None, 74)
    font_small = pygame.font.Font(None, 36)

    text = font_big.render("¡VICTORIA!", True, (0, 255, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(text, text_rect)

    shots_text = font_small.render(f"Disparos: {shots_fired}", True, (255, 255, 255))
    shots_rect = shots_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(shots_text, shots_rect)

    collision_text = font_small.render(f"Colisiones: {collision_count}", True, (255, 255, 255))
    collision_rect = collision_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(collision_text, collision_rect)

    score_text = font_small.render(f"Puntos: {score[0]}", True, (255, 255, 0))
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(score_text, score_rect)

    restart_text = font_small.render("Presiona R para jugar de nuevo", True, (255, 255, 255))
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4 - 20))
    screen.blit(restart_text, restart_rect)

    quit_text = font_small.render("Presiona Q para salir", True, (255, 255, 255))
    quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4 + 20))
    screen.blit(quit_text, quit_rect)

    pygame.display.flip()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "restart"
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

# Grupos y jugador
all_sprites = pygame.sprite.Group()
meteor_group = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player(all_sprites, bullets)
show_start_screen()

for _ in range(8):
    meteor = Meteor()
    all_sprites.add(meteor)
    meteor_group.add(meteor)

collision_count = 0
collision_limit = 8
shots_fired = 0
score = [0]
victory_score = 120

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
                shots_fired += 1

    all_sprites.update()

    check_laser_collisions(bullets, meteor_group, all_sprites, player, score, explosion_anim)

    if score[0] >= victory_score:
        action = show_victory_screen(shots_fired, collision_count, score)
        if action == "restart":
            collision_count = 0
            shots_fired = 0
            score[0] = 0
            all_sprites.empty()
            meteor_group.empty()
            bullets.empty()
            player = Player(all_sprites, bullets)
            for _ in range(8):
                meteor = Meteor()
                all_sprites.add(meteor)
                meteor_group.add(meteor)
            continue
        else:
            break

    hits = pygame.sprite.spritecollide(player, all_sprites, False)
    for hit in hits:
        if isinstance(hit, Meteor):
            collision_count += 1
            hit.kill()
            explosion = Explosion(hit.rect.center, explosion_anim)
            all_sprites.add(explosion)
            sounds_music.explosion_sound.play()
            new_meteor = Meteor()
            all_sprites.add(new_meteor)
            meteor_group.add(new_meteor)

            if collision_count >= collision_limit:
                action = show_game_over_screen(shots_fired, collision_count, score)
                if action == "restart":
                    collision_count = 0
                    shots_fired = 0
                    score[0] = 0
                    all_sprites.empty()
                    meteor_group.empty()
                    bullets.empty()
                    player = Player(all_sprites, bullets)
                    for _ in range(8):
                        meteor = Meteor()
                        all_sprites.add(meteor)
                        meteor_group.add(meteor)
                    continue
                else:
                    running = False
                    break

    # Dibujar todo
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    font = pygame.font.Font(None, 36)
    shots_text = font.render(f"Disparos: {shots_fired}", True, (255, 255, 255))
    screen.blit(shots_text, (10, 10))
    score_text = font.render(f"Puntos: {score[0]}", True, (255, 255, 0))
    score_rect = score_text.get_rect(topright=(WIDTH - 10, 10))
    screen.blit(score_text, score_rect)

    life_bar_width = 200
    life_bar_height = 20
    life_bar_x = 10
    life_bar_y = 50
    life_percentage = (1 - (collision_count / collision_limit)) * life_bar_width
    pygame.draw.rect(screen, (0, 255, 0), (life_bar_x, life_bar_y, life_percentage, life_bar_height))
    pygame.draw.rect(screen, (255, 0, 0), (life_bar_x, life_bar_y, life_bar_width, life_bar_height), 2)

    pygame.display.flip()

pygame.quit()