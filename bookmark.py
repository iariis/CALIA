import pygame

# Config
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("bookmark")
clock = pygame.time.Clock()

# Función para dibujar texto (marcador)
def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

# Score inicial
score = 0

# Game Loop
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Simular aumento de score
    score += 1

    # Dibujar fondo
    screen.fill(BLACK)

    # Dibujar marcador
    draw_text(screen, f"Score: {score}", 30, WIDTH // 2, 10)

    pygame.display.flip()

pygame.quit()
