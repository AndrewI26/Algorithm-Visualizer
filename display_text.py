import pygame
#How to display text in pygame referenced from this article
# https://www.geeksforgeeks.org/python-display-text-to-pygame-window/


def display_text(win, x, y, string, color, size):
    font = pygame.font.Font('opensans.ttf', size)
    text = font.render(string, True, color)
    textRect = text.get_rect()
    textRect.center = (x, y)
    win.blit(text, textRect)
