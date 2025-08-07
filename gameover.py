
def show_go_screen():
    screen.blit(background, [0, 0])
    draw_text(screen, "SHOOTER", 65, WIDTH // 2, HEIGHT / 4)
    draw_text(screen, "(Instructions)", 27, WIDTH // 2, HEIGHT // 2)
    draw_text(screen, "Press key to begin", 17, WIDTH // 2, HEIGHT * 3/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
