import pygame
from pulo import pulo
from bibliotecas import movimento, sair, animar
from colisão import colisao
from var import personagem, tela, player_group, all_blocks, fundo1, clock, current_phase
from fases import fase

pygame.init()
pygame.display.set_caption('Joguin do IF')

while True:
    sair()
  
    direcao = movimento()
    personagem.mover(direcao)
    animar(personagem)
    pulo(personagem)
    colisao(player_group, all_blocks)
    
    tela.blit(fundo1, (0, 0))

    current_phase = fase(current_phase)

    pygame.display.update()
    clock.tick(60)
