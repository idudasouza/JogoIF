import pygame
import var
from bibliotecas import Jogador
from var import tela, player_group, fundo1, menu, botao, botao_rect, texto_imagem, botao1, faseAtual, botaoinstruir, botaocredito, botaoinstruir_rect, botaocredito_rect, creditos, fontemenor, creditostexto, comojogar, titulocomojogar, textocomojogar, personagem, grupofase1

def fase(current_phase):
  if current_phase == "menu":
    tela.blit(menu, (0, 0))
    tela.blit(botao, botao_rect.topleft)
    tela.blit(botaoinstruir, botaoinstruir_rect.topleft)
    tela.blit(botaocredito, botaocredito_rect.topleft)
    tela.blit(texto_imagem, (475, 70))
    tela.blit(titulocomojogar, (430, 220))
    tela.blit(creditos, (445, 370))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if botao_rect.collidepoint(mouse_x, mouse_y):
      tela.blit(botao1, botao_rect.topleft)
      if pygame.mouse.get_pressed()[0]:
        current_phase = "jogo"

    if botaoinstruir_rect.collidepoint(mouse_x, mouse_y):
      tela.blit(botao1, botaoinstruir_rect.topleft)
      if pygame.mouse.get_pressed()[0]:
        current_phase = "instruir"

    if botaocredito_rect.collidepoint(mouse_x, mouse_y):
      tela.blit(botao1, botaocredito_rect.topleft)
      if pygame.mouse.get_pressed()[0]:
        current_phase = "creditos"

  elif current_phase == "jogo":
    if faseAtual == 1:
      personagem.rect.x = 5
      personagem.rect.y = 335
      fase1()
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
      return "menu" 
      
  elif current_phase == "instruir":
    tela.blit(comojogar, (0, 0))
    tela.blit(titulocomojogar, (320, 40))
    pos = 155
    for linha in textocomojogar:
        texto = fontemenor.render(linha, True, (0,0,0))
        tela.blit(texto, (450, pos))
        pos += 90
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
      return "menu"
      
  elif current_phase == "creditos":
    tela.blit(menu, (0, 0))
    tela.blit(creditos, (300, 50))
    pos = 125
    for linha in creditostexto:
      texto = fontemenor.render(linha, True, (0,0,0))
      tela.blit(texto, (300, pos))
      pos += 20
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
      return "menu"
      
  return current_phase

def fase1():
  
  global personagem
  personagem = Jogador(5, 335)
  tela.blit(fundo1, (0, 0))
  grupofase1.draw(tela)
  player_group.draw(tela)
 
  