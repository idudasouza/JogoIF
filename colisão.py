import pygame
from bibliotecas import movimento

class Block(pygame.sprite.Sprite):
  def __init__(self, x, y, image_path):
    super().__init__()
    self.image = pygame.image.load(image_path)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

def colisao(jogadores, fase_atual):
  for jogador in jogadores:
    for bloco in fase_atual:
      colisoes = pygame.sprite.spritecollide(jogador, fase_atual, False)
      if not colisoes:
        jogador.colidindo = False
        jogador.velocidadeR = 10
        jogador.velocidadeL = 10
        if  not jogador.rect.y == 335:
          jogador.caindo = True
      for bloco in colisoes:
        jogador.colidindo = True
        if jogador.rect.y <= bloco.rect.top and jogador.caindo:
          jogador.animate = False
          jogador.pulando = False
          jogador.caindo = False
          jogador.rect.bottom = bloco.rect.top
        elif movimento() == 'r':
          jogador.velocidadeR = 0
        elif movimento() == 'l':
          jogador.velocidadeL = 0
