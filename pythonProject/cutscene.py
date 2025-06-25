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

#Fundo
tela1 = pygame.image.load('pythonProject/cutscene/tela1.jpeg')
tela1 = pygame.transform.scale(tela1,(largura,altura))
tela2 = pygame.image.load('pythonProject/cutscene/tela2.jpeg')
tela2 = pygame.transform.scale(tela2,(largura,altura))
tela3 = pygame.image.load('pythonProject/cutscene/tela3.jpeg')
tela3 = pygame.transform.scale(tela3,(largura,altura))
tela4 = pygame.image.load('pythonProject/cutscene/tela4.jpeg')
tela4 = pygame.transform.scale(tela4,(largura,altura))
tela5 = pygame.image.load('pythonProject/cutscene/tela5.jpeg')
tela5 = pygame.transform.scale(tela5,(largura,altura))
tela6 = pygame.image.load('pythonProject/cutscene/tela6.jpeg')
tela6 = pygame.transform.scale(tela6,(largura,altura))


#musica
pygame.mixer.music.load('pythonProject/Efeitos Sonoros/starwars.mp3')
#pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()
pygame.mixer.music.pause()

#contador
cronometro = 0

#LAÇO PRINCIPAL
while True:
    clock.tick(fps)
    tela.fill((0,0,0,))

#Quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                import main

    cronometro += 1

    if cronometro > 900:
        pygame.mixer.music.unpause()

    if cronometro <= 600:
        tela.blit(tela1,(0,0))
    if cronometro > 600 and cronometro <= 900:
        tela.blit(tela2,(0,0))
    if cronometro > 900 and cronometro <= 1100:
        tela.blit(tela3,(0,0))
    if cronometro > 1100 and cronometro <= 1500:
        tela.blit(tela4,(0,0))
    if cronometro > 1500 and cronometro <= 1800:
        tela.blit(tela5,(0,0))
    if cronometro > 1800:
        tela.blit(tela6,(0,0))









    pygame.display.flip()