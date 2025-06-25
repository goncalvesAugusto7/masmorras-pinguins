import pygame
from pygame.locals import *
from sys import exit
import random
pygame.init()
pygame.mixer.init()

#Eixos da Tela
largura=1280
altura=720

#Inicialização
tela=pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Masmorras&Pinguins')
clock=pygame.time.Clock()

#fps
fps=60

#imagem
imagem = pygame.image.load('sprites pinguim/cubo_gelo.png')
pos = [0,0]
velocidade = [0.2,0.3]

#LAÇO PRINCIPAL
while True:
    clock.tick(fps)
    tela.fill((0,0,0,))

#Quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()





# Fundo Cenário
    tela.fill((0,0,0))

    pos[0] += velocidade[0] * fps
    pos[1] += velocidade[1] * fps

    if pos[0] > tela.get_width()-imagem.get_width():
        velocidade[0] = -velocidade[0]
        pos[0] = tela.get_width() - imagem.get_width()
    elif pos[0] < 0:
        velocidade[0] = -velocidade[0]
        pos[0] = 0

    if pos[1] > tela.get_height()-imagem.get_height():
        velocidade[1] = -velocidade[1]
        pos[1] = tela.get_height() - imagem.get_height()
    elif pos[1] < 0:
        velocidade[1] = -velocidade[1]
        pos[1] = 0






    tela.blit(imagem, pos)

    pygame.display.flip()