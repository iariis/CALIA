import pygame
from config import WIDTH, HEIGHT  # Constantes globales

def draw_text(surface, text, size, x, y, color=(255, 255, 255)):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)

def show_go_screen(screen, clock, shots_fired):
    """Pantalla de Game Over que muestra puntuación y opciones"""

    screen.fill((0, 0, 0))  # Fondo negro

    draw_text(screen, "GAME OVER", 64, WIDTH // 2, HEIGHT // 4, (255, 0, 0))
    draw_text(screen, f"Disparos realizados: {shots_fired}", 30, WIDTH // 2, HEIGHT // 2)
    draw_text(screen, "Presiona R para reiniciar", 24, WIDTH // 2, HEIGHT * 3 / 4 - 30)
    draw_text(screen, "Presiona Q para salir", 24, WIDTH // 2, HEIGHT * 3 / 4 + 10)

    pygame.display.flip()

    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False  # Sale para reiniciar el juego
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()
