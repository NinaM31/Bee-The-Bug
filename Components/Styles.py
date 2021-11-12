import pygame

def draw_text(screen, size, text, x, y, color):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()

    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)
