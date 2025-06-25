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
fundo = pygame.image.load('pythonProject/sprites pinguim/telaInicial4.jpeg')
fundo = pygame.transform.scale(fundo,(largura,altura))

#musica
pygame.mixer.music.load('pythonProject/Efeitos Sonoros/DragonForce.mp3')
pygame.mixer.music.play(-1,19)
#pygame.mixer.music.set_volume(0.05)

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
            pygame.mixer.music.stop()
            import cutscene



    tela.blit(fundo,(0,0))





    pygame.display.flip()