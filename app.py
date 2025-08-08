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
pygame.display.set_caption("Shooter")
clock = pygame.time.Clock()
background = pygame.image.load("assets/background.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # para que cubra toda la pantalla


# Cargar animaciones de explosión
explosion_anim = []
for i in range(9):
    file = f"assets/regularExplosion0{i}.png"
    img = pygame.image.load(file).convert()
    img.set_colorkey((0, 0, 0))
    img_scale = pygame.transform.scale(img, (70, 70))
    explosion_anim.append(img_scale)


def show_start_screen():
    screen.fill((0, 0, 0))  # Rellenar la pantalla con negro
    font = pygame.font.Font(None, 74)  # Crear una fuente
    text = font.render("Press Enter to Play", True, (255, 255, 255))  # Texto blanco
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Centrar el texto
    screen.blit(text, text_rect)  # Dibujar el texto
    pygame.display.flip()  # Actualizar la pantalla
    # Esperar a que el jugador presione Enter
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Tecla Enter
                    waiting = False

def show_game_over_screen(shots_fired):
    screen.fill((0, 0, 0))  # Fondo negro
    font_big = pygame.font.Font(None, 74)
    font_small = pygame.font.Font(None, 36)

    text = font_big.render("GAME OVER", True, (255, 0, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(text, text_rect)

    shots_text = font_small.render(f"Disparos: {shots_fired}", True, (255, 255, 255))
    shots_rect = shots_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(shots_text, shots_rect)

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

# Grupos de sprites
all_sprites = pygame.sprite.Group()
meteor_group = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player(all_sprites, bullets)
show_start_screen()

# Crear meteoros iniciales
for _ in range(8):
    meteor = Meteor()
    all_sprites.add(meteor)
    meteor_group.add(meteor)
# Contador de colisiones y disparos
collision_count = 0
collision_limit = 4  # Número máximo de colisiones permitidas
shots_fired = 0  # Contador de disparos
score = [0]  # Lista para poder modificar dentro de la función

# Bucle principal del juego
running = True
while running:
    clock.tick(60)  # Limitar a 60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()  # Disparar
                shots_fired += 1  # Incrementar contador de disparos
    # Actualizar todos los sprites
    all_sprites.update()
    # Colisiones láser - meteoros
    game_over = check_laser_collisions(
        bullets,
        meteor_group,
        all_sprites,
        player,
        score,
        explosion_anim
    )

    # Colisiones jugador - meteoro
    hits = pygame.sprite.spritecollide(player, all_sprites, False)
    for hit in hits:
        if isinstance(hit, Meteor):  # Verifica si el sprite colisionado es un meteoro
            collision_count += 1
            hit.kill()  # Elimina el meteoro
            explosion = Explosion(hit.rect.center, explosion_anim)
            all_sprites.add(explosion)
            sounds_music.explosion_sound.play()

            print(f"Colisiones: {collision_count}/{collision_limit}")
            # Generar un nuevo meteoro
            new_meteor = Meteor()
            all_sprites.add(new_meteor)
            meteor_group.add(new_meteor)
            if collision_count >= collision_limit:
                print("¡Game Over!")
                action = show_game_over_screen(shots_fired)  # Ahora recibe la acción
                if action == "restart":
                    # Reiniciar variables y grupos para empezar de nuevo
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
                    continue  # Sigue el loop principal reiniciado
                else:
                    running = False
                    break

    # Dibujar todo
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    # Mostrar el contador de disparos
    font = pygame.font.Font(None, 36)
    shots_text = font.render(f"Disparos: {shots_fired}", True, (255, 255, 255))
    screen.blit(shots_text, (10, 10))  # Mostrar en la esquina superior izquierda
    # Mostrar la barra de vida
    life_bar_width = 200
    life_bar_height = 20
    life_bar_x = 10
    life_bar_y = 50
    life_percentage = (1 - (collision_count / collision_limit)) * life_bar_width
    pygame.draw.rect(screen, (0, 255, 0), (life_bar_x, life_bar_y, life_percentage, life_bar_height))  # Barra verde
    pygame.draw.rect(screen, (255, 0, 0), (life_bar_x, life_bar_y, life_bar_width, life_bar_height), 2)  # Contorno de la barra
    pygame.display.flip()  # Actualizar la pantalla
pygame.quit()


# escudos
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter con Escudos")
clock = pygame.time.Clock()

# Número de escudos
shields = 2

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player(all_sprites, bullets)
for _ in range(8):
    meteor = Meteor()
    all_sprites.add(meteor)

collision_count = 0
shots_fired = 0
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

    hits = pygame.sprite.spritecollide(player, all_sprites, False)
    for hit in hits:
        if isinstance(hit, Meteor):
            if shields > 0:
                shields -= 1
                print(f"¡Escudo usado! Escudos restantes: {shields}")
            else:
                collision_count += 1
                print(f"Colisiones: {collision_count}/{collision_limit}")
            hit.kill()
            explosion = Explosion(hit.rect.center, explosion_anim)
            all_sprites.add(explosion)

            new_meteor = Meteor()
            all_sprites.add(new_meteor)
            if collision_count >= collision_limit:
                print("¡Game Over!")
                show_game_over_screen(shots_fired)
                
                running = False

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    font = pygame.font.Font(None, 36)
    shots_text = font.render(f"Disparos: {shots_fired}", True, (255, 255, 255))
    screen.blit(shots_text, (10, 10))

    # Barra de vida
    life_bar_width = 200
    life_bar_height = 20
    life_bar_x = 10
    life_bar_y = 50
    life_percentage = (1 - (collision_count / collision_limit)) * life_bar_width
    pygame.draw.rect(screen, (0, 255, 0), (life_bar_x, life_bar_y, life_percentage, life_bar_height))
    pygame.draw.rect(screen, (255, 0, 0), (life_bar_x, life_bar_y, life_bar_width, life_bar_height), 2)

    # Mostrar escudos
    shield_text = font.render(f"Escudos: {shields}", True, (0, 191, 255))  # Azul celeste
    screen.blit(shield_text, (10, 80))

    pygame.display.flip()

pygame.quit()
