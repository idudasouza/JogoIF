import pygame
import var
from função import sair
from colisão import colisao
from var import personagem, player_group, grupofase1, clock, current_phase,tela
from personagem import movimento, animar
from fases import fase

pygame.init()
pygame.display.set_caption('Joguin do IF')

while True:
  sair()
  
  direcao = movimento()
  personagem.mover(direcao)
  animar(personagem)
  personagem.pulo()
  colisao(var.player_group, grupofase1)
  
  current_phase = fase(current_phase)
    
  pygame.display.update()
  clock.tick(60)