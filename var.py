import pygame
from bibliotecas import Jogador
pygame.font.init()

tela = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
fundo1 = pygame.image.load('fundo1.png')

class Porteiro(pygame.sprite.Sprite):
    def __init__(self, x, y):
      super().__init__()
      self.sprites = []
      self.current_sprite = 0
      self.carregar_sprites()
      self.image = self.sprites[self.current_sprite]
      self.rect = self.image.get_rect()

      self.rect.x = x
      self.rect.y = y

      self.agiu = False

    def carregar_sprites(self):
      self.sprites.append(pygame.image.load('sprite_porteiro0.png'))
      self.sprites.append(pygame.image.load('sprite_porteiro1.png'))
porteiro = Porteiro(200, 330)
grupofase1 = pygame.sprite.Group()
grupofase1.add(porteiro)

porta = pygame.sprite.Sprite()
porta.image = pygame.image.load('porta.png')
porta.rect = porta.image.get_rect()
porta.rect.x = 600
porta.rect.y = 330

personagem = Jogador(0, 0)
all_blocks = pygame.sprite.Group()
player_group = pygame.sprite.Group()
player_group.add(personagem)
grupofase1.add(porta)

faseAtual = 1
current_phase = "menu"

#menu
fonte = pygame.font.Font("Pixels.ttf", 75)
fontemenor = pygame.font.Font("Pixels.ttf", 35)

botao = pygame.image.load("botao.png")
botao1 = pygame.image.load("botao1.png")
botao1.set_alpha(128)

botaoinstruir = botao
botaoinstruir_rect = botao.get_rect()
botaoinstruir_rect.topleft = (400, 200)
comojogar = pygame.image.load('como jogar.png')
titulocomojogar = fonte.render('INSTRUCAO', True, (0, 0, 0))
textocomojogar = [
  "Abre o menu",
  "Pula",
  "Anda para a esquerda",
  "Anda para a direita"
]

creditostexto = [
    "Desenvolvedores Principais:",
    "Ana Beatriz - Desenvolvedor/Programador",
    "Eduarda - Desenvolvedor/Designer",
    "",
    "Arte e Design:",
    "Eduarda - Arte, Ilustracoes e",
    "Design de Personagens",
    "",
    "Agradecimentos Especiais:",
    "Agradecemos a todos os nossos amigos e",
    "professores por seu apoio e feedback", 
    "valioso durante o desenvolvimento do jogo.",
    "",
    "Agradecimento ao Software e Ferramentas:",
    "repl.it - Utilizada para Desenvolvimento",
    "piskel - Utilizada para Arte/Design"
]
botaocredito = botao
botaocredito_rect = botao.get_rect()
botaocredito_rect.topleft = (400, 350)
creditos = fonte.render('CREDITOS', True, (0, 0, 0))

botao_rect = botao.get_rect()
botao_rect.topleft = (400, 50) 
texto_imagem = fonte.render('JOGAR', True, (0, 0, 0))
menu = pygame.image.load('menu.png')
