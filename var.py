import pygame
import time
import math
import random
import os
from personagem import Jogador
pygame.font.init()

tela = pygame.display.set_mode((700, 500), pygame.SRCALPHA)
clock = pygame.time.Clock()

fonte = pygame.font.Font("Pixels.ttf", 55)
fontemenor = pygame.font.Font("Pixels.ttf", 12)
fontemedia = pygame.font.Font("Pixels.ttf", 23)

recuperacao = False

# Fase 1

fundo1 = pygame.image.load('sprites/fundo1.png')
fundo2 = pygame.image.load('sprites/fundo2.png')

start = False
verde = (0, 255, 0)
amarelo = (255, 255, 0)
vermelho = (255, 0, 0)
class Caixa(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((5, 5))
    self.image.fill(amarelo)
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)

  def colidir_com_mouse(self, mouse_pos):
    global Nota, no, nota, start
    if self.rect.collidepoint(mouse_pos) and self.image.get_at((0, 0)) == amarelo and start:
      self.image.fill(verde)
      if Nota <= 99.8:
        Nota += 0.2
      Nota = float("{:.2f}".format(Nota))
      nota = f"nota: {Nota}/100"
      no = fontemenor.render(nota, True, (255, 255, 255))
class QuadradoReset(pygame.sprite.Sprite):
  def __init__(self, x, y):
      super().__init__()
      self.image = pygame.Surface((5, 5))
      self.image.fill(vermelho)
      self.rect = self.image.get_rect()
      self.rect.topleft = (x, y)

  def colidir_com_mouse(self, mouse_pos):
      global Nota, no, nota, start
      if self.rect.collidepoint(mouse_pos) and start:
        if Nota >= 0.2:
          Nota -= 0.2
        Nota = float("{:.2f}".format(Nota))
        nota = f"nota: {Nota}/100"
        no = fontemenor.render(nota, True, (255, 255, 255))
        time.sleep(0.01)
class inicio(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((20, 20))
    self.image.fill(vermelho)
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.was_mouse_pressed = False

  def colidir_com_mouse(self, mouse_pos):
    global start, faseAtual, recuperacao, caixas, nota2, Nota
    mouse_x, mouse_y = mouse_pos
    is_mouse_pressed = pygame.mouse.get_pressed()[0]
    if self.rect.collidepoint(mouse_pos):
      if is_mouse_pressed and not self.was_mouse_pressed and not start:
        self.image.fill(verde)
        start = True
      elif is_mouse_pressed and not self.was_mouse_pressed and start:
        self.image.fill(vermelho)
        start = False
        if Nota < 60 and recuperacao == False:
          recuperacao = True
          caixas.empty
          caixas = create_boxes()
          nota2 = Nota
          Nota = 0
        else:
          if nota2 < Nota:
            nota2 = Nota
          faseAtual = 4
      
      self.was_mouse_pressed = is_mouse_pressed
veneno = [pygame.image.load("sprites/red.png")]
componentes = [pygame.image.load("sprites/yellow.png"), pygame.image.load("sprites/green.png")]
posicoes_iniciais = [100, 300, 500]
class Elementos(pygame.sprite.Sprite):
  def __init__(self):
      super().__init__()
      self.image = random.choice(componentes)
      self.rect = self.image.get_rect()

  def update(self):
    global Nota, no, nota
    self.rect.y += 10
    if self.rect.y > 500:
        self.kill()
    if self.rect.y >= 300 and self.rect.y <= 350:
      if self.rect.x == posicoes_iniciais[0] and pygame.key.get_pressed()[pygame.K_LEFT]:
        self.kill()
        Nota += 1
        nota = f"nota: {Nota}/100"
        no = fontemenor.render(nota, True, (255, 255, 255))

      if self.rect.x == posicoes_iniciais[1] and pygame.key.get_pressed()[pygame.K_DOWN]:
        self.kill()
        Nota += 1
        nota = f"nota: {Nota}/100"
        no = fontemenor.render(nota, True, (255, 255, 255))

      if self.rect.x == posicoes_iniciais[2] and pygame.key.get_pressed()[pygame.K_RIGHT]:
        self.kill()
        Nota += 1
        nota = f"nota: {Nota}/100"
        no = fontemenor.render(nota, True, (255, 255, 255))
          
def create_boxes():
  caixas = pygame.sprite.Group()
  for i in range(100):
      caixa = Caixa(100 + i * 5, 450)
      quadrado_reset0 = QuadradoReset(100 + i * 5, 445)
      quadrado_reset1 = QuadradoReset(100 + i * 5, 455)
      caixas.add(caixa)
      caixas.add(quadrado_reset0)
      caixas.add(quadrado_reset1)
  for i in range(80):
    if i < 10 or i > 35:
      caixa = Caixa(590, 450 - i * 5)
      quadrado_reset0 = QuadradoReset(595, 450 - i * 5)
      if i != 0 and i < 79:
        quadrado_reset1 = QuadradoReset(585, 450 - i * 5)
    else:
      caixa = Caixa(400, 450 - i * 5)
      quadrado_reset1 = QuadradoReset(405, 450 - i * 5)
      quadrado_reset0 = QuadradoReset(395, 450 - i * 5)
    
    caixas.add(caixa)
    caixas.add(quadrado_reset0)
    caixas.add(quadrado_reset1)
  for i in range(100):
    if i > 58 or i < 22:
      quadrado_reset0 = QuadradoReset(100 + i * 5, 50)
      if i < 98:
        quadrado_reset1 = QuadradoReset(100 + i * 5, 60)
        caixa = Caixa(100 + i * 5, 55)
      if i == 20:
        quadrado_reset1 = Caixa(100 + i * 5, 60)
      if i == 21 or i == 59:
        caixa = QuadradoReset(100 + i * 5, 55)
      caixas.add(caixa)
      caixas.add(quadrado_reset0)
      caixas.add(quadrado_reset1)
  for i in range(81):
    if i < 20 or i > 50:
      if i != 80:
        caixa = Caixa(95, 450 - i * 5)
      else:
        caixa = QuadradoReset(95, 450 - i * 5)
      quadrado_reset1 = QuadradoReset(90, 450 - i * 5)
      if i < 79:
        quadrado_reset0 = QuadradoReset(100, 450 - i * 5)
    else:
      caixa = Caixa(145, 450 - i * 5)
      quadrado_reset1 = QuadradoReset(140, 450 - i * 5)
      quadrado_reset0 = QuadradoReset(150, 450 - i * 5)
        
    caixas.add(caixa)
    caixas.add(quadrado_reset0)
    caixas.add(quadrado_reset1)
  for i in range(11):
    if i > 0:
      quadrado_reset0 = QuadradoReset(100 + i * 5, 195)
    quadrado_reset1 = QuadradoReset(90 + i * 5, 205)
    if i != 0:
      caixa = Caixa(90 + i * 5,200)
    else:
      caixa = QuadradoReset(90 + i * 5,200)
    
    caixas.add(caixa)
    caixas.add(quadrado_reset0)
    caixas.add(quadrado_reset1)
  for i in range(11):
    if i > 0:
      quadrado_reset0 = QuadradoReset(100 + i * 5, 355)
    quadrado_reset1 = QuadradoReset(90 + i * 5, 345)
    if i != 0:
      caixa = Caixa(90 + i * 5,350)
    else:
      caixa = QuadradoReset(90 + i * 5,350)
  
    caixas.add(caixa)
    caixas.add(quadrado_reset0)
    caixas.add(quadrado_reset1)
  for i in range(39):
    quadrado_reset0 = QuadradoReset(395 + i * 5, 405)
    quadrado_reset1 = QuadradoReset(405 + i * 5, 395)
    if i != 38:
      caixa = Caixa(405 + i * 5, 400)
    else:
      caixa = QuadradoReset(405 + i * 5, 400)
    
    caixas.add(caixa)
    caixas.add(quadrado_reset0)
    caixas.add(quadrado_reset1)
  for i in range(39):
    quadrado_reset0 = QuadradoReset(395 + i * 5, 270)
    quadrado_reset1 = QuadradoReset(405 + i * 5, 280)
    if i != 38:
      caixa = Caixa(405 + i * 5, 275)
    else:
      caixa = QuadradoReset(405 + i * 5, 275)
  
    caixas.add(caixa)
    caixas.add(quadrado_reset0)
    caixas.add(quadrado_reset1)
  
  raio = 100
  center_x = 300
  center_y = 60
  numbloco = 70
  angle_increment = math.pi / numbloco
  
  for i in range(numbloco):
    angle = i * angle_increment
    ax = center_x + int(raio * math.cos(angle))
    ay = center_y + int(raio * math.sin(angle))
    caixa = Caixa(ax,ay)
    caixas.add(caixa)
  for i in range(numbloco):
    angle = i * angle_increment
    ax = center_x + int((raio-5) * math.cos(angle))
    ay = center_y + int((raio-5) * math.sin(angle))
    quadrado_reset0 = QuadradoReset(ax,ay)
    caixas.add(quadrado_reset0)
  for i in range(numbloco):
    angle = i * angle_increment
    ax = center_x + int((raio+5) * math.cos(angle))
    ay = center_y + int((raio+5) * math.sin(angle))
    quadrado_reset1 = QuadradoReset(ax,ay)
    caixas.add(quadrado_reset1)
  
  inicio_instancia = inicio(85, 442)
  caixas.add(inicio_instancia)

  return caixas

caixas = create_boxes()
class Veneno(pygame.sprite.Sprite):
  def __init__(self):
      super().__init__()
      self.image = random.choice(veneno)
      self.rect = self.image.get_rect()

  def update(self):
    global Nota, no, nota
    self.rect.y += 15
    if self.rect.y > 500:
        self.kill()
    if self.rect.y >= 300 and self.rect.y <= 350:
      if self.rect.x == posicoes_iniciais[0] and pygame.key.get_pressed()[pygame.K_LEFT]:
        self.kill()
        if Nota >= 2:
          Nota -= 2
          nota = f"nota: {Nota}/100"
          no = fontemenor.render(nota, True, (255, 255, 255))

      if self.rect.x == posicoes_iniciais[1] and pygame.key.get_pressed()[pygame.K_DOWN]:
        self.kill()
        if Nota >= 2:
          Nota -= 2
          nota = f"nota: {Nota}/100"
          no = fontemenor.render(nota, True, (255, 255, 255))
        elif Nota >= 1:
          Nota -= 1
          nota = f"nota: {Nota}/100"
          no = fontemenor.render(nota, True, (255, 255, 255))

      if self.rect.x == posicoes_iniciais[2] and pygame.key.get_pressed()[pygame.K_RIGHT]:
        self.kill()
        if Nota >= 2:
          Nota -= 2
          nota = f"nota: {Nota}/100"
          no = fontemenor.render(nota, True, (255, 255, 255))

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

    def carregar_sprites(self):
      self.sprites.append(pygame.image.load('sprites/sprite_porteiro0.png'))

    def update(self):
      self.image = self.sprites[self.current_sprite]
porteiro = Porteiro(200, 330)

class Porta(pygame.sprite.Sprite):
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
      self.sprites.append(pygame.image.load('sprites/porta.png'))
porta = Porta(600, 330)

grupofase1 = pygame.sprite.Group()
      
grupofase1.add(porteiro)
          
grupofase1.add(porta)

personagem = Jogador(0, 0)
player_group = pygame.sprite.Group()
player_group.add(personagem)

faseAtual = 3
Nota = 0
current_phase = "jogo"
sanidade = f"sanidade: {personagem.sanidade}/100"
san = fontemenor.render(sanidade, True, (255,255,255))
dinheiro = f"dinheiro: {personagem.dinheiro}/100"
din = fontemenor.render(dinheiro, True, (255,255,255))
nota = f"nota: {Nota}/100"
no = fontemenor.render(nota, True, (255,255,255))

# Menu

botao = pygame.image.load("sprites/jogar.png")
botao1 = pygame.image.load("sprites/botao1.png")
botao1.set_alpha(128)

botaoinstruir = pygame.image.load("sprites/instruir.png")
botaoinstruir_rect = botao.get_rect()
botaoinstruir_rect.topleft = (200, 200)
comojogar = pygame.image.load('sprites/como jogar.png')
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
botaocredito = pygame.image.load("sprites/creditos.png")
botaocredito_rect = botao.get_rect()
botaocredito_rect.topleft = (200, 350)
creditos = fonte.render('CREDITOS', True, (0, 0, 0))

botao_rect = botao.get_rect()
botao_rect.topleft = (200, 50) 
texto_imagem = fonte.render('JOGAR', True, (0, 0, 0))
menu = pygame.image.load('sprites/menu.png')

# Fase 2
questoes = [
  '1. Em sua composicao os resistores \npodem ser:',
  'qui 1',
  '1. Durante o processo de acabamento em \nusinagem, como são classificados os \nsulcos e os cavaques?',
  '2. Qual circuito recebe em sua entrada uma \ntensão alternada e devolve em sua saída uma \ntensão continua?',
  'qui 2',
  '2. Quais são os componentes obrigatórios em \num sistema pneumático?',
  '3. A partida estrela triangulo e a soft \nstarter tem como função:',
  'qui 3',
  '3. A radiação eletromagnética de pequeno \ncomprimento de onda, produzida quando os életrons \nem alta velocidadecolidem com uma placa defletora de Tungstênio, é chamado de:',
]
respostasA = [
  'a- Metalico, ceramico e Bobinado',
  'qui V',
  'a- Sulcos são classificados como \ntransversais e cavaques como longitudinais.',
  'a- Retificador',
  'qui F',
  'a- Admissão, Compressão, Explosão, Escape.',
  'a- Controlar a velocidade do motor',
  'qui V',
  'a- Radiação X',
]
respostasB = [
  'b- Bobinado, Metálico e de Carvão e Bobinado',
  'qui F',
  'b- Sulcos são classificados como côncavos e \ncavaques como convexos.',
  'b- Amplificador',
  'qui V',
  'b- fonte, elemento de sinal, elemento de \ncomando, atuador.',
  'b- Reduzir a corrente de partida do motor.',
  'qui F',
  'b- Radiação Gama',
]
questoesGerais = [
  '1. Qual o planeta mais próximo do Sol?',
  '2. Qual o maior oceano do mundo?'
]
respostasgeraisA = [
  'a- marte',
  'a- atlântico'
]
respostasgeraisB = [
  'b- mercúrio',
  'b- pacífico'
]

questaoAtual = 0
parte = 1

mouse_button_pressed = False

resposta = 'quimica'

fimfase = False

questao_atualizada = False

nota1 = 0
nota2 = 0

pos_x, pos_y = 10, 50
pos_x2, pos_y2 = 10, 150
pos_x3, pos_y3 = 10, 250