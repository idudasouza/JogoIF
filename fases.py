import pygame
from personagem import Jogador
import var
from var import tela, player_group, fundo1, menu, botao, botao_rect, botao1, botaoinstruir, botaocredito, botaoinstruir_rect, botaocredito_rect, creditos, fontemenor, creditostexto, comojogar, titulocomojogar, textocomojogar, personagem, grupofase1, fundo2, questoesGerais, fontemedia, respostasgeraisA, respostasgeraisB, questoes, respostasA, respostasB


def fase(current_phase):
  if current_phase == "menu":
    tela.blit(menu, (0, 0))
    tela.blit(botao, botao_rect.topleft)
    tela.blit(botaoinstruir, botaoinstruir_rect.topleft)
    tela.blit(botaocredito, botaocredito_rect.topleft)

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
    if var.faseAtual == 1:
      personagem.rect.x = 5
      personagem.rect.y = 335
      personagem.chao = 335
      fase1()
    elif var.faseAtual == 2:
      fase2()
    elif var.faseAtual == 3:
      fase3()
    elif var.faseAtual == 4:
      tela.blit(fundo1, (0, 0))
    tela.blit(var.san, (580, 5))
    tela.blit(var.din, (580, 20))
    tela.blit(var.no, (580, 35))

    pygame.display.flip()

    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
      return "menu"
  elif current_phase == "instruir":
    tela.blit(comojogar, (0, 0))
    tela.blit(titulocomojogar, (320, 40))
    pos = 155
    for linha in textocomojogar:
      texto = fontemenor.render(linha, True, (0, 0, 0))
      tela.blit(texto, (450, pos))
      pos += 90
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
      return "menu"
  elif current_phase == "creditos":
    tela.blit(menu, (0, 0))
    tela.blit(creditos, (300, 50))
    pos = 125
    for linha in creditostexto:
      texto = fontemenor.render(linha, True, (0, 0, 0))
      tela.blit(texto, (300, pos))
      pos += 20
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
      return "menu"

  return current_phase

def fase1():
  global personagem
  personagem = Jogador(0, 0)
  tela.blit(fundo1, (0, 0))
  grupofase1.draw(tela)
  player_group.draw(tela)

def fase2():
  def conferir(certoOUerrado):
    if certoOUerrado == 'errado' and var.questao_atualizada:
      if var.Nota <= 0:
        var.Nota = 0
      else:
        var.Nota -= 20
    var.nota = f"nota: {var.Nota}/100"
    var.no = fontemenor.render(var.nota, True, (255, 255, 255))
    if var.parte == 2 and var.fimfase:
      var.fimfase = False
    if var.parte == 1 and var.questaoAtual == 0:
      var.questaoAtual = 1
    elif var.parte == 1 and var.questaoAtual == 1:
      var.parte = 2
      var.fimfase = True
      if var.resposta == 'automacao':
        var.questaoAtual = 0
      elif var.resposta == 'quimica':
        var.questaoAtual = 1
      else:
        var.questaoAtual = 2
    elif var.parte == 2 and not var.fimfase and var.questao_atualizada:
      if var.questaoAtual == 6 or var.questaoAtual == 7 or var.questaoAtual == 8:
        if var.Nota >= 60 or var.recuperacao == True:
          if var.Nota >= 80:
            personagem.sanidade += 10
            var.sanidade = f"sanidade: {personagem.sanidade}/100"
            var.san = fontemenor.render(var.sanidade, True, (255, 255, 255))
          if var.recuperacao:
            personagem.sanidade -= 10
            var.sanidade = f"sanidade: {personagem.sanidade}/100"
            var.san = fontemenor.render(var.sanidade, True, (255, 255, 255))
          if var.nota1 < var.Nota:
            var.nota1 = var.Nota
          var.faseAtual = 3
          var.recuperacao = False
          var.Nota = 0
        else:
          personagem.sanidade -= 10
          var.sanidade = f"sanidade: {personagem.sanidade}/100"
          var.san = fontemenor.render(var.sanidade, True, (255, 255, 255))
          var.nota1 = var.Nota
          var.parte = 1
          var.questaoAtual = 0
          var.recuperacao = True
          var.Nota = 100
        var.nota = f"nota: {var.Nota}/100"
        var.no = fontemenor.render(var.nota, True, (255, 255, 255))
      else:
        var.questaoAtual += 3
        var.questao_atualizada = False

  tela.blit(fundo2, (0, 0))
  grupofase1.empty()
  player_group.empty()

  player_group.add(personagem)

  questao = None
  rA = None
  rB = None
  if var.parte == 1:
    questao = questoesGerais[var.questaoAtual]
    rA = respostasgeraisA[var.questaoAtual]
    rB = respostasgeraisB[var.questaoAtual]
    linhas = questao.split('\n')
    pergunta = [fontemedia.render(linha, True, (150, 0, 0)) for linha in linhas]
    linhasa = rA.split('\n')
    respostaA = [fontemedia.render(linha, True, (0, 0, 0)) for linha in linhasa]
    linhasb = rB.split('\n')
    respostaB = [fontemedia.render(linha, True, (0, 0, 0)) for linha in linhasb]
  if var.parte == 2:
    questao = questoes[var.questaoAtual]
    rA = respostasA[var.questaoAtual]
    rB = respostasB[var.questaoAtual]
    linhas = questao.split('\n')
    pergunta = [fontemedia.render(linha, True, (150, 0, 0)) for linha in linhas]
    linhasa = rA.split('\n')
    respostaA = [fontemedia.render(linha, True, (0, 0, 0)) for linha in linhasa]
    linhasb = rB.split('\n')
    respostaB = [fontemedia.render(linha, True, (0, 0, 0)) for linha in linhasb]
  
  for linha in pergunta:
    tela.blit(linha, (var.pos_x, var.pos_y))
    var.pos_y += 30
  for linha in respostaA:
    tela.blit(linha, (var.pos_x2, var.pos_y2))
    var.pos_y2 += 30
    A_rect = linha.get_rect()
    A_rect.topleft = (10, 150)
  for linha in respostaB:
    tela.blit(linha, (var.pos_x3, var.pos_y3))
    var.pos_y3 += 30
    B_rect = linha.get_rect()
    B_rect.topleft = (10, 250)

  var.pos_y = 50
  var.pos_y2 = 150
  var.pos_y3 = 250

  mouse_x, mouse_y = pygame.mouse.get_pos()
  mouse_pressed = pygame.mouse.get_pressed()[0]

  if A_rect.collidepoint(mouse_x, mouse_y) and mouse_pressed and not var.mouse_button_pressed:
    if not var.questao_atualizada:
      var.questao_atualizada = True
    if var.parte == 1:
      if var.questaoAtual == 0:
        conferir('errado')
      elif var.questaoAtual == 1:
        conferir('errado')
    elif var.parte == 2:
      if var.resposta == 'automacao':
        if var.questaoAtual == 0:
          conferir('certo')
        if var.questaoAtual == 3:
          conferir('certo')
        if var.questaoAtual == 6:
          conferir('errado')
      elif var.resposta == 'quimica':
        if var.questaoAtual == 1:
          conferir('certo')
        if var.questaoAtual == 4:
          conferir('errado')
        if var.questaoAtual == 7:
          conferir('certo')
      else:
        if var.questaoAtual == 2:
          conferir('errado')
        if var.questaoAtual == 5:
          conferir('errado')
        if var.questaoAtual == 8:
          conferir('certo')
    var.mouse_button_pressed = True
  if B_rect.collidepoint(mouse_x, mouse_y) and mouse_pressed and not var.mouse_button_pressed:
    if not var.questao_atualizada:
      var.questao_atualizada = True
    if var.parte == 1:
      if var.questaoAtual == 0:
        conferir('certo')
      elif var.questaoAtual == 1:
        conferir('certo')
    elif var.parte == 2:
      if var.resposta == 'automacao':
        if var.questaoAtual == 0:
          conferir('errado')
        if var.questaoAtual == 3:
          conferir('errado')
        if var.questaoAtual == 6:
          conferir('certo')
      elif var.resposta == 'quimica':
        if var.questaoAtual == 1:
          conferir('errado')
        if var.questaoAtual == 4:
          conferir('certo')
        if var.questaoAtual == 7:
          conferir('errado')
      else:
        if var.questaoAtual == 2:
          conferir('certo')
        if var.questaoAtual == 5:
          conferir('certo')
        if var.questaoAtual == 8:
          conferir('errado')
    var.mouse_button_pressed = True
  var.mouse_button_pressed = mouse_pressed

def fase3():
  if var.resposta != 'quimica':
    tela.blit(fundo2, (0, 0))
    var.caixas.draw(tela)
    mouse_pos = pygame.mouse.get_pos()
    for caixa in var.caixas:
      if caixa.colidir_com_mouse(mouse_pos):
        caixa.colidir_com_mouse(mouse_pos)
