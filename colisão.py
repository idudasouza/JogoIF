import pygame
from bibliotecas import movimento

class Block(pygame.sprite.Sprite):
  def __init__(self, x, y, image_path):
    super().__init__()
    self.image = pygame.image.load(image_path)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

def colisao(jogadores, blocos):
  for jogador in jogadores:
    for bloco in blocos:
      colisoes = pygame.sprite.spritecollide(jogador, blocos, False)
      if not colisoes and not jogador.rect.y == 335:
        jogador.caindo = True
      for bloco in colisoes:
        if jogador.rect.y <= bloco.rect.top and jogador.caindo == True:
          jogador.pulando = False
          jogador.caindo = False
          jogador.rect.bottom = bloco.rect.top
        #if jogador.rect.left >= block.rect.rigth: