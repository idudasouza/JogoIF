#CUIDADO

import pygame
from pygame.locals import QUIT
import sys
import random


class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Sprite
        self.sprites = []
        self.current_sprite = 0
        self.carregar_sprites()
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()

        # Posição
        self.rect.x = x
        self.rect.y = y

        # Velocidades
        self.velocidadeL = 10
        self.velocidadeR = 10
        self.salto = 10

        self.on_ground = False
        self.pulando = False
        self.caindo = False
        self.gravidade = 0

        # Animação
        self.animate = False
        self.flip = False
        self.colidindo = False

        # Pontos
        self.sanidade = random.randint(20, 80)
        self.dinheiro = random.randint(10, 100)

    def carregar_sprites(self):
        self.sprites.append(pygame.image.load('sprite_0.png'))
        self.sprites.append(pygame.image.load('sprite_1.png'))
        self.sprites.append(pygame.image.load('sprite_2.png'))

    def update(self):
        self.image = self.sprites[self.current_sprite]
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, False)

    def mover(self, direcao):
        if direcao == 'r':
            self.rect.x += self.velocidadeR
            if self.flip:
                self.image = pygame.transform.flip(self.image, True, False)
                self.flip = False
        elif direcao == 'l':
            self.rect.x -= self.velocidadeL
            if not self.flip:
                self.image = pygame.transform.flip(self.image, True, False)
                self.flip = True

        if direcao == 'n' or self.colidindo == True or self.pulando == True:
            self.animate = False
            self.current_sprite = 0
        else:
            self.animate = True

def movimento():
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        direcao = 'l'
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        direcao = 'r'
    else:
        direcao = 'n'
    return direcao

def sair():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def animar(jogador):
    if jogador.animate:
        if jogador.current_sprite >= len(jogador.sprites) - 1:
            jogador.current_sprite = 0
        else:
            jogador.current_sprite += 1

    jogador.update()
