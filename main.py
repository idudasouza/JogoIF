import pygame
from pulo import pulo
from bibliotecas import movimento, sair, Jogador, animar
from colisão import Block, colisao
from var import tela

# Restante do código de teclas

global tela
pygame.init()
pygame.display.set_caption('Joguin do IF')
clock = pygame.time.Clock()

fundo = pygame.image.load('fundo1.png')

personagem = Jogador(50, 335)
# Criar blocos de chão e parede usando a imagem
block = Block(100, 335, 'block.png')
# Grupo para todos os blocos
all_blocks = pygame.sprite.Group()
all_blocks.add(block)
# Grupo para player
player_group = pygame.sprite.Group()
player_group.add(personagem)

while True:
    global tela
    sair()
  
    direcao = movimento()
    personagem.mover(direcao)
    animar(personagem)
    pulo(personagem)
    colisao(player_group, all_blocks)

    tela.blit(fundo, (0,0))

    # Desenhar todos os blocos
    all_blocks.draw(tela)
    # Desenhar o jogador
    player_group.draw(tela)

    pygame.display.update()
    clock.tick(60)
