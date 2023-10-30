import pygame
from pygame.locals import QUIT
import sys

def sair():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()