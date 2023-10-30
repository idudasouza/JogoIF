import pygame
from personagem import movimento, Jogador
import var
from var import Porteiro, Porta, tela, fontemenor

personagem = Jogador(0,0)
falou = False
def colisao(jogadores, fase_atual):
  global falou
  col = 'n'
  for jogador in jogadores:
    for bloco in fase_atual:
      colisoes = pygame.sprite.spritecollide(jogador, fase_atual, False)
      if not colisoes:
        jogador.colidindo = False
        jogador.velocidadeR = 10
        jogador.velocidadeL = 10
        if not jogador.rect.y == personagem.chao:
          jogador.caindo = True
      for bloco in colisoes:
        jogador.colidindo = True
        if isinstance(bloco, Porteiro) and not falou:
          col = 'porteiro'
        elif isinstance(bloco, Porteiro) and falou:
          jogador.podemover = True
        elif isinstance(bloco, Porta):
          var.faseAtual = 2
        elif jogador.rect.y <= bloco.rect.top and jogador.caindo:
          jogador.animate = False
          jogador.pulando = False
          jogador.caindo = False
          jogador.rect.bottom = bloco.rect.top
        elif movimento() == 'r':
          jogador.velocidadeR = 0
        elif movimento() == 'l':
          jogador.velocidadeL = 0


  if col == 'porteiro':
    texto = "Bem-vindo(a) ao jogo Torre IF!\nMas antes de iniciar, me diga,\nqual o seu curso?\nPressione a para automacao,\nm para mecanica ou q para quimica"
    linhas = texto.split('\n')
    pos_x, pos_y = 220, 150
    jogador.podemover = False
    jogador.animate = False
    jogador.current_sprite = 0
    
    for linha in linhas:
      texto_surface = fontemenor.render(linha, True, (255, 255, 255))
      tela.blit(texto_surface, (pos_x, pos_y))
      pos_y += 20      
      
    pygame.display.flip()
    while var.resposta == '': 
      for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
          if evento.key == pygame.K_a:
            var.resposta = 'automacao'
            break
          elif evento.key == pygame.K_m:
            var.resposta = 'mecanica'
            break
          elif evento.key == pygame.K_q:
            var.resposta = 'quimica'
            break

    pos_y += 20
    linhas = f"que otimo {var.resposta} e um curso muito bom"
    texto_surface = fontemenor.render(linhas, True, (255, 255, 255))
    tela.blit(texto_surface, (pos_x, pos_y))
    pygame.display.flip()
    pygame.time.delay(2500)
    col = ''
    falou = True


  