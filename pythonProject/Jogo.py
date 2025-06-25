import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
pygame.mixer.init()


# Eixos da Tela
largura = 1280
altura = 720


# FPS
fps = 60


# Eixos Cobra
xCobra = randint(280,1000)
yCobra = randint(20,700)


# Eixos Fruta
xFruta = randint(50, largura - 50)
yFruta = randint(50, altura - 50)

# Inicialização
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Cobrinha')
clock = pygame.time.Clock()

#Fontes
fonteGameOver=pygame.font.SysFont('gabriola', 128, True, False)
fonteEsc=pygame.font.SysFont('gabriola', 48, True, False)
# Função de Crescimento
def crescimento(listaCorpo):
    for x_y in listaCorpo:
        pygame.draw.rect(tela, (0, 155, 0), (x_y[0], x_y[1], 15,15))
listaCorpo = []
tamanhoInicial = 20

# Movimentação
xControle = 1
yControle = 0

#Função Derrota
gameover=False
def derrota(gameover):
    global xCobra,yCobra
    xCobra+=0
    yCobra+=0
    tela.blit(texto_derrota, (largura / 4, 310))
    tela.blit(texto_ESC, (0, 50))

#Função reinicio
def reiniciar():
    global tamanhoInicial,xCobra,yCobra,xFruta,yFruta,listaCabeça,listaCorpo,gameover
    tamanhoInicial = 20
    xCobra = randint(280, 1000)
    yCobra = randint(280, 1000)
    xFruta = randint(5, largura - 5)
    yFruta = randint(10, altura - 10)
    listaCabeça=[]
    listaCorpo=[]
    gameover=False

#Musica
pygame.mixer.music.load('pythonProject/Efeitos Sonoros/atumalaca.mp3')
pygame.mixer.music.play(-1)


#LAÇO PRINCIPAL
while True:
    clock.tick(fps)
    tela.fill((200, 150, 0,))
# Quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        # movimentação
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                if xControle==0:
                    xControle = 5
                    yControle = 0
            if event.key == K_LEFT:
                if xControle==0:
                    xControle = -5
                    yControle = 0

            if event.key == K_UP:
                if yControle==0:
                    xControle = 0
                    yControle = -5

            if event.key == K_DOWN:
                if yControle==0:
                    xControle = 0
                    yControle = 5

    xCobra=xCobra+xControle
    yCobra=yCobra+yControle
# Mensagem
    mensagem_derrota = 'GAME OVER'
    mensagem_ESC = 'Aperte ESC Para Reiniciar'
# Textos
    texto_derrota = fonteGameOver.render(mensagem_derrota, True, (255, 0, 0))
    texto_ESC = fonteEsc.render(mensagem_ESC, True, (255, 255, 255))
    retTexto_derrota = texto_derrota.get_rect()

# Personagens
    cobra = pygame.draw.rect(tela, (0, 155, 0), (xCobra, yCobra, 15,15))
    fruta = pygame.draw.rect(tela, (255, 0, 0), (xFruta, yFruta, 15, 15))
    if cobra.colliderect(fruta):
        xFruta = randint(5, largura - 5)
        yFruta = randint(10, altura - 10)
        tamanhoInicial += 5
# Crescimento da Cobra
    listaCabeça = []
    listaCabeça.append(xCobra)
    listaCabeça.append(yCobra)
       # listaCorpo=[]
    listaCorpo.append(listaCabeça)
    if listaCorpo.count(listaCabeça) > 1:
        gameover=True
    if len(listaCorpo) > tamanhoInicial:
        del listaCorpo[0]
    crescimento(listaCorpo)
#Teleporte
    if yCobra<0:
        yCobra=altura
    if yCobra>altura:
        yCobra=0
    if xCobra<0:
        xCobra=largura
    if xCobra>largura:
        xCobra=0
#Derrota
    if listaCorpo.count(listaCabeça) > 1:
        gameover=True
        tela.fill((0,0,0))
        while gameover:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        reiniciar()
            retTexto_derrota.center = (largura / 2, altura / 2)
            tela.blit(texto_derrota, retTexto_derrota)
            tela.blit(texto_ESC, (0, 50))

            pygame.display.update()


        derrota(gameover)


    pygame.display.update()
