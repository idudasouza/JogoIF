import pygame

def pulo(jogador):
    keys = pygame.key.get_pressed()

    chao_y = 335

    if keys[pygame.K_UP] and not jogador.pulando and not jogador.caindo:
        jogador.pulando = True
        jogador.gravidade = -10 

    if jogador.pulando or jogador.caindo:
        jogador.rect.y += jogador.gravidade
        jogador.gravidade += 0.9

        if jogador.rect.y >= chao_y:
            jogador.rect.y = chao_y
            jogador.pulando = False
            jogador.caindo = False
            jogador.gravidade = 0 
        elif jogador.gravidade > 0:
            jogador.caindo = True