import pygame
from pygame.locals import *
from sys import exit
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

#Pato
pato = pygame.image.load('pythonProject/sprites pinguim/pato.png').convert_alpha()
pato = pygame.transform.scale(pato,(628//2,253//2))

cringuim = pygame.image.load('pythonProject/pinguim/sprite_0.png').convert_alpha()
cringuim = pygame.transform.scale(cringuim,(32*10,32*10))

fundo = pygame.image.load('pythonProject/sprites pinguim/parabensFinal.jpeg')
fundo = pygame.transform.scale(fundo,(largura,altura))

cronometro = 0
som_quack = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/quack.mp3')

pygame.mixer.music.load('pythonProject/Efeitos Sonoros/NOOT.mp3')
#pygame.mixer.music.set_volume(0.5)

#LAÇO PRINCIPAL
while True:
    clock.tick(fps)
    tela.fill((255,255,255))

#Quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                import Inicio


    cronometro += 1
    if cronometro == 180:
        som_quack.play()

    if cronometro <= 180:
        tela.blit(pato,(largura//2-150,altura//2-50))

    if cronometro >= 280:
        tela.blit(cringuim,(largura//2-180,altura//2-180))

    if cronometro == 240:
        pygame.mixer.music.play()

    if cronometro >= 520:
        tela.blit(fundo,(0,0))











    pygame.display.flip()