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

#Tela de Parabéns
parabens = pygame.image.load('pythonProject/sprites pinguim/parabens2.jpg')
parabens = pygame.transform.scale(parabens,(largura,altura))
parabensTela = True

#Som Vitória Fase 2
som_vitoria=pygame.mixer.Sound('pythonProject/Efeitos Sonoros/BackInBlack')
#som_vitoria.set_volume(0.5)
som_vitoria.play()

#Musica de Fundo
pygame.mixer.music.load('pythonProject/Efeitos Sonoros/kiss.mp3')
pygame.mixer.music.play(-1,0)
#pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.pause()

#Efeitos sonoros
som_tiro = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/shooting.mp3')
#som_tiro.set_volume(0.1)
som_ativação = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/smw_coin.wav')
som_bonk = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/bonk.mp3')

som_batida = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/smw_thunder.wav')

som_zap = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/zap.mp3')

som_abertura = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/smw_midway_gate.wav')

som_guarda = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/8-bit-kit-explosion-3_G_minor.wav')
#som_guarda.set_volume(0.05)

som_derrota = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/hello darkness 8 bit.mp3')

#Tela Fundo
fundo = pygame.image.load('pythonProject/sprites pinguim/las venturas.jpg')
fundo = pygame.transform.scale(fundo,(largura,altura))

#Eixos HitBox
xHitBox, yHitBox = largura - 50, altura - 75

#Vida
vidaJogador = 8

#Valores da Vida
yVida = 50

#Velocidade
velocidade = 5
#Dash
direcao = 0

#Velocidade Bala
velocidadeBala = 22

#Cores Atenas
corAntena1= (255,0,0)
corAntena2= (255,0,0)
corAntena3= (255,0,0)

#Contador Antenas
contadorAntea1 = 0
contadorAntea2 = 0
contadorAntea3 = 0
#yCampodeForça
yCampoDeForça = 494
yCDF = 430

#Sprite Sheet
spriteSheet = pygame.image.load('pythonProject/pinguim/spritesheet pinguim.png').convert_alpha()
spriteCarro = pygame.image.load('pythonProject/sprites pinguim/carrin.png').convert_alpha()
spriteSheetGlobo = pygame.image.load('pythonProject/sprites pinguim/spritesheet_globo.png').convert_alpha()

#Classe
class Pinguim(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spritesPinguim = []
        for i in range(3):
            sprite = spriteSheet.subsurface((i * 32, 0), (32, 32))
            sprite = pygame.transform.scale(sprite,(90,90))
            self.spritesPinguim.append(sprite)

        self.indexLista = 0
        self.image = self.spritesPinguim[self.indexLista]

        self.rect = self.image.get_rect()
        self.rect.center = (largura - 50, altura - 82)
        self.animar = False

    def andar(self):
        self.animar = True

    def update(self):
        if self.animar == True:
            if self.indexLista > 2:
                self.indexLista = 0
                self.animar = False
            self.indexLista += 0.25
            self.image = self.spritesPinguim[int(self.indexLista)]

class Globo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spritesGlobo = []
        for i in range(4):
            sprite = spriteSheetGlobo.subsurface((i*32, 0), (32, 32))
            sprite = pygame.transform.scale(sprite,(90,90))
            self.spritesGlobo.append(sprite)

        self.indexLista = 0
        self.image = self.spritesGlobo[self.indexLista]

        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        self.velocidade = [6,8]

    def update(self):
        if self.indexLista > 3:
            self.indexLista = 0
        self.indexLista += 0.1
        self.image = self.spritesGlobo[int(self.indexLista)]
        self.rect.x += self.velocidade[0]
        self.rect.y += self.velocidade[1]

        if self.rect.x > largura-90:
            self.velocidade[0] = -self.velocidade[0]
        elif self.rect.x < 0:
            self.velocidade[0] = -self.velocidade[0]

        if self.rect.y > altura-90:
            self.velocidade[1] = -self.velocidade[1]
        elif self.rect.y < 0:
            self.velocidade[1] = -self.velocidade[1]

class Carros(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spriteCarro.subsurface((0,0),(1333,2400))
        self.image = pygame.transform.scale(self.image,(1333//25,2400//25))
        self.rect = self.image.get_rect()
        self.rect.y = altura + random.randrange(120, 400, 240)
        self.rect.x = random.randrange(400, 800, 120)

    def update(self):
        if self.rect.y > altura:
            self.rect.x = random.randrange(400, 800, 120)
            self.rect.y = 0
        self.rect.y +=10

#Grupos Classes
allSprites = pygame.sprite.Group()

carro = Carros()
allSprites.add(carro)

globo = Globo()
allSprites.add(globo)

#Storm Trooper
grupostormTrooper = pygame.sprite.Group()
stormTrooper = pygame.sprite.Sprite(grupostormTrooper)
stormTrooper.image = pygame.image.load('pythonProject/sprites pinguim/stomtrooper.png')
stormTrooper.image = pygame.transform.scale(stormTrooper.image,(320//3,260//3))
stormTrooper.rect = stormTrooper.image.get_rect()
stormTrooper.rect.topleft = 250, 450
stormTrooperVivo = True

xTiro,yTiro = 250,550

vidaStormTrooper = 10

#Campo de Força
grupocdf = pygame.sprite.Group()
cdf = pygame.sprite.Sprite(grupocdf)
cdf.image = pygame.image.load('pythonProject/sprites pinguim/campo_de_força.png')
cdf.image = pygame.transform.scale(cdf.image,(32*4,32*4))
cdf.rect = cdf.image.get_rect()
cdf.rect.topleft = 235, yCDF
cdfVivo = True

#Bala
grupoBala = pygame.sprite.Group()
bala = pygame.sprite.Sprite(grupoBala)
bala.image = pygame.image.load('pythonProject/sprites pinguim/bala.png')
bala.image = pygame.transform.scale(bala.image,(64//3,64//3))
bala.rect = bala.image.get_rect()
bala.rect.center = xHitBox,yHitBox
atirando = False

#Antenas
grupoAntena = pygame.sprite.Group()
antena = pygame.sprite.Sprite(grupoAntena)
antena.image = pygame.image.load('pythonProject/sprites pinguim/antena.png')
antena.image = pygame.transform.scale(antena.image,(1076//12,1124//12))
antena.rect = antena.image.get_rect()
antena.rect.topright = (910,290)
antenaFuncionando = True

grupoAntena2 = pygame.sprite.Group()
antena2 = pygame.sprite.Sprite(grupoAntena2)
antena2.image = pygame.image.load('pythonProject/sprites pinguim/antena.png')
antena2.image = pygame.transform.scale(antena2.image,(1076//12,1124//12))
antena2.rect = antena2.image.get_rect()
antena2.rect.topright = (550,290)
antenaFuncionando2 = True

grupoAntena3 = pygame.sprite.Group()
antena3 = pygame.sprite.Sprite(grupoAntena3)
antena3.image = pygame.image.load('pythonProject/sprites pinguim/antena.png')
antena3.image = pygame.transform.scale(antena3.image,(1076//12,1124//12))
antena3.rect = antena3.image.get_rect()
antena3.rect.topright = (120,20)
antenaFuncionando3 = True

#Ataques Antenas
grupobolaEnergia = pygame.sprite.Group()
bolaEnergia = pygame.sprite.Sprite(grupobolaEnergia)
bolaEnergia.image = pygame.image.load('pythonProject/sprites pinguim/energy_ball.png')
bolaEnergia.image = pygame.transform.scale(bolaEnergia.image,(500//20,850//20))
bolaEnergia.rect = bolaEnergia.image.get_rect()
bolaEnergia.rect.topright = (890,310)

grupobolaEnergia2 = pygame.sprite.Group()
bolaEnergia2 = pygame.sprite.Sprite(grupobolaEnergia2)
bolaEnergia2.image = pygame.image.load('pythonProject/sprites pinguim/energy_ball.png')
bolaEnergia2.image = pygame.transform.scale(bolaEnergia2.image,(500//20,850//20))
bolaEnergia2.rect = bolaEnergia2.image.get_rect()
bolaEnergia2.rect.topright = (540,310)

grupobolaEnergia3 = pygame.sprite.Group()
bolaEnergia3 = pygame.sprite.Sprite(grupobolaEnergia3)
bolaEnergia3.image = pygame.image.load('pythonProject/sprites pinguim/energy_ball.png')
bolaEnergia3.image = pygame.transform.scale(bolaEnergia3.image,(500//15,850//15))
bolaEnergia3.rect = bolaEnergia3.image.get_rect()
bolaEnergia3.rect.topright = (90,20)

#Grpos Sprites
allSprites.add(bala)

allSprites.add(stormTrooper)
allSprites.add(cdf)

cringuim = Pinguim()
allSprites.add(cringuim)

allSprites.add(antena)
allSprites.add(antena2)
allSprites.add(antena3)

allSprites.add(bolaEnergia)
allSprites.add(bolaEnergia2)
allSprites.add(bolaEnergia3)

#Vidas Imagem
grupo1 = pygame.sprite.Group()
linux1 = pygame.sprite.Sprite(grupo1)
linux1.image = pygame.image.load('pythonProject/sprites pinguim/linuxguim.png')
linux1.image = pygame.transform.scale(linux1.image,(60,60))
linux1.rect = linux1.image.get_rect()
linux1.rect.center = largura - 40, yVida
linux1Vivo = True

grupo2 = pygame.sprite.Group()
linux2 = pygame.sprite.Sprite(grupo2)
linux2.image = pygame.image.load('pythonProject/sprites pinguim/linuxguim.png')
linux2.image = pygame.transform.scale(linux2.image,(60,60))
linux2.rect = linux2.image.get_rect()
linux2.rect.center = largura - 120, yVida

linux2Vivo = True

grupo3 = pygame.sprite.Group()
linux3 = pygame.sprite.Sprite(grupo3)
linux3.image = pygame.image.load('pythonProject/sprites pinguim/linuxguim.png')
linux3.image = pygame.transform.scale(linux3.image,(60,60))
linux3.rect = linux3.image.get_rect()
linux3.rect.center = largura - 200, yVida
linux3Vivo = True

grupo4 = pygame.sprite.Group()
linux4 = pygame.sprite.Sprite(grupo4)
linux4.image = pygame.image.load('pythonProject/sprites pinguim/linuxguim.png')
linux4.image = pygame.transform.scale(linux4.image,(60,60))
linux4.rect = linux4.image.get_rect()
linux4.rect.center = largura - 280, yVida
linux4Vivo = True

grupo5 = pygame.sprite.Group()
linux5 = pygame.sprite.Sprite(grupo5)
linux5.image = pygame.image.load('pythonProject/sprites pinguim/linuxguim.png')
linux5.image = pygame.transform.scale(linux5.image,(60,60))
linux5.rect = linux5.image.get_rect()
linux5.rect.center = largura - 360, yVida
linux5Vivo = True

grupo6 = pygame.sprite.Group()
linux6 = pygame.sprite.Sprite(grupo6)
linux6.image = pygame.image.load('pythonProject/sprites pinguim/linuxguim.png')
linux6.image = pygame.transform.scale(linux6.image,(60,60))
linux6.rect = linux6.image.get_rect()
linux6.rect.center = largura - 440, yVida
linux6Vivo = True

grupo7 = pygame.sprite.Group()
linux7 = pygame.sprite.Sprite(grupo7)
linux7.image = pygame.image.load('pythonProject/sprites pinguim/linuxguim.png')
linux7.image = pygame.transform.scale(linux7.image,(60,60))
linux7.rect = linux7.image.get_rect()
linux7.rect.center = largura - 520, yVida

linux7Vivo = True

grupo8 = pygame.sprite.Group()
linux8 = pygame.sprite.Sprite(grupo8)
linux8.image = pygame.image.load('pythonProject/sprites pinguim/linuxguim.png')
linux8.image = pygame.transform.scale(linux8.image,(60,60))
linux8.rect = linux8.image.get_rect()
linux8.rect.center = largura - 600, yVida
linux8Vivo = True

grupo9 = pygame.sprite.Group()
linux9 = pygame.sprite.Sprite(grupo9)
linux9.image = pygame.image.load('pythonProject/sprites pinguim/linuxguim.png')
linux9.image = pygame.transform.scale(linux9.image,(60,60))
linux9.rect = linux9.image.get_rect()
linux9.rect.center = largura - 680, yVida
linux9Vivo = False

grupo10 = pygame.sprite.Group()
linux10 = pygame.sprite.Sprite(grupo10)
linux10.image = pygame.image.load('pythonProject/sprites pinguim/linuxguim.png')
linux10.image = pygame.transform.scale(linux10.image,(60,60))
linux10.rect = linux10.image.get_rect()
linux10.rect.center = largura - 760, yVida
linux10Vivo = False

#Fontes
fonteEsc = pygame.font.SysFont('gabriola', 48, True, False)
fonteGameOver = pygame.font.SysFont('gabriola', 72, True, False)

#Mensagens
mensagem_derrota = 'CRINGE'
mensagem_ESC = 'Aperte ESC Para Reiniciar'

#Textos
texto_ESC = fonteEsc.render(mensagem_ESC, True, (255, 255, 255))
texto_derrota = fonteGameOver.render(mensagem_derrota, True, (255, 0, 0))

# Retangulos de Texto
retTextoDerrota = texto_derrota.get_rect()
retTextoDerrota.center = (largura / 2, altura / 2)

#Função Derrota
gameOver = False
def derrota(gameOver):
    global fps,xHitBox,yHitBox,vidaJogador,linux1Vivo,linux2Vivo,linux3Vivo,linux4Vivo,linux5Vivo,linux6Vivo,linux7Vivo,linux8Vivo,linux9Vivo,linux10Vivo,corAntena1,corAntena2,corAntena3,contadorAntea1,contadorAntea2,contadorAntea3,antenaFuncionando,antenaFuncionando2,antenaFuncionando3,stormTrooperVivo,yCampoDeForça,yCDF,xTiro,yTiro,vidaStormTrooper
    fps = 30
    pygame.mixer.music.stop()
    xHitBox, yHitBox = largura - 50, altura - 75
    cringuim.rect.center = (largura - 50, altura - 82)
    bala.rect.center = xHitBox, yHitBox
    som_derrota.play()
    som_derrota.set_volume(0.25)
    tela.fill((0, 0, 0,))
    tela.blit(texto_derrota, (retTextoDerrota))
    tela.blit(texto_ESC, (0, 50))
    corAntena1,corAntena2,corAntena3 = (255,0,0),(255,0,0),(255,0,0)
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            fps = 60
            pygame.mixer.music.play(-1,)
            pygame.mixer.music.set_volume(0.1)
            som_derrota.stop()
            contadorAntea1,contadorAntea2,contadorAntea3 = 0,0,0
            vidaJogador = 8
            linux1Vivo,linux2Vivo,linux3Vivo,linux4Vivo,linux5Vivo,linux6Vivo,linux7Vivo,linux8Vivo = True,True,True,True,True,True,True,True
            bolaEnergia.rect.topright = (880, 310)
            bolaEnergia2.rect.topright = (530, 310)
            bolaEnergia3.rect.topright = (80, 20)
            antenaFuncionando,antenaFuncionando2,antenaFuncionando3 = True,True,True
            stormTrooperVivo = True
            yCampoDeForça = 494
            cdf.rect.y = 430
            stormTrooper.rect.topleft = 250, 450
            stormTrooperVivo = True
            xTiro, yTiro = 250, 550
            vidaStormTrooper = 10


#LAÇO PRINCIPAL
while True:
    clock.tick(fps)
    tela.fill((0,0,0,))

#Quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

# HitBox
    hitBox = pygame.draw.circle(tela, [255, 0, 0], (xHitBox, yHitBox), (35))
    hitBoxStormTrooper = pygame.draw.circle(tela, (0, 0, 0), stormTrooper.rect.center, 50)

# Objetivo
    objetivo = pygame.draw.circle(tela, (255, 255, 0), (300, 420), (5))

# Campo de Força
    if antenaFuncionando == False and antenaFuncionando2 == False and antenaFuncionando3 == False:
        yCampoDeForça = -100
        cdf.rect.y = -200
    campoDeForca = pygame.draw.circle(tela, (255, 255, 255), (235 + 64, yCampoDeForça), (66))

# Paredes
    limiteBase = pygame.draw.line(tela, (0, 255, 0), (0, altura - 1), (largura, altura - 1), (1))

    limiteHoriDireita = pygame.draw.line(tela, (0, 0, 0), (0, 555), (235, 555), (1))
    limiteHoriDireita2 = pygame.draw.line(tela, (0, 0, 0), (235 + 32 * 4, 555), (445, 555), (1))
    limiteVertDireita = pygame.draw.line(tela, (0, 0, 0), (450, 550), (450, 0), (1))

    limiteMeio = pygame.draw.line(tela, (0, 0, 0), (450, 290), (910, 290), (1))

    limiteVertEsquerda = pygame.draw.line(tela, (0, 0, 0), (910, 290), (910, 475), (1))
    limiteHoriEsquerda = pygame.draw.line(tela, (0, 0, 0), (915, 480), (largura, 480), (1))

    limiteArvEsquerda = pygame.draw.line(tela, (255, 255, 255), (640, 290), (640, 530), (1))
    limiteArvDireita = pygame.draw.line(tela, (255, 255, 255), (675, 290), (675, 530), (1))

    limiteArvmeio = pygame.draw.line(tela, (255, 255, 255), (645, 535), (670, 535), (1))

    limiteLargura = pygame.draw.line(tela, (0, 255, 0), (largura, 0), (largura, altura), (1))
    limiteLargura0 = pygame.draw.line(tela, (0, 255, 0), (0, 0), (0, altura), (1))

# Fundo Cenário
    tela.blit(fundo, (0, 0))

# Atirar
    if pygame.key.get_pressed()[K_e]:
        atirando = True
    if atirando == True:
        bala.rect.y -= velocidadeBala
        if bala.rect.y <= -64:
            bala.rect.center = xHitBox, yHitBox
            atirando = False

#Tiro Storm Trooper
    tiroStormTrooper = pygame.draw.rect(tela,(255,0,0), (xTiro,yTiro,30,10))
    if yTiro<0:
        yTiro = 550
        xTiro = 250
    xTiro += 10
    yTiro -= 10

# Desenhando Classes
    allSprites.draw(tela)
    allSprites.update()

# Movimentção Personagem
    if xHitBox == largura-35:
        xHitBox = largura - 50
        cringuim.rect.x = largura - 100
        bala.rect.center = xHitBox,yHitBox
    if pygame.key.get_pressed()[K_UP]:
        cringuim.rect.y -= velocidade
        bala.rect.y -= velocidade
        yHitBox -= velocidade
        cringuim.andar()
        direcao = 8
    if pygame.key.get_pressed()[K_DOWN]:
        cringuim.rect.y += velocidade
        yHitBox += velocidade
        bala.rect.y += velocidade
        cringuim.andar()
        direcao = 2
    if pygame.key.get_pressed()[K_RIGHT]:
        cringuim.rect.x += velocidade
        bala.rect.x += velocidade
        xHitBox += velocidade
        cringuim.andar()
        direcao = 6
    if pygame.key.get_pressed()[K_LEFT]:
        cringuim.rect.x -= velocidade
        bala.rect.x -= velocidade
        xHitBox -= velocidade
        cringuim.andar()
        direcao = 4
#Dash
    if direcao == 8:
        if event.type == KEYDOWN:
            if event.key == K_TAB:
                cringuim.rect.y -= 8
                yHitBox -= 8
                bala.rect.y -= 8
    if direcao == 2:
        if event.type == KEYDOWN:
            if event.key == K_TAB:
                cringuim.rect.y += 8
                yHitBox += 8
                bala.rect.y += 8
    if direcao == 6:
        if event.type == KEYDOWN:
            if event.key == K_TAB:
                cringuim.rect.x += 8
                xHitBox += 8
                bala.rect.x += 8
    if direcao == 4:
        if event.type == KEYDOWN:
            if event.key == K_TAB:
                cringuim.rect.x -= 8
                xHitBox -= 8
                bala.rect.x -= 8

#Antenas
    linhaAntena1 = pygame.draw.line(tela, (corAntena1), (820,290+93), (820+89, 290+93), (5))
    linhaAntena2 = pygame.draw.line(tela, (corAntena2), (460, 290 + 93), (460 + 89, 290 + 93), (5))
    linhaAntena3 = pygame.draw.line(tela, (corAntena3), (30, 20 + 93), (25 + 89, 20 + 93), (5))
#Ataque Antenas
    if antenaFuncionando == True:
        bolaEnergia.rect.y += 8
        if bolaEnergia.rect.y > altura + 120:
            bolaEnergia.rect.y = 290

    if antenaFuncionando2 == True:
        bolaEnergia2.rect.y += 8
        if bolaEnergia2.rect.y > altura + 120:
            bolaEnergia2.rect.y = 290

    if antenaFuncionando3 == True:
        bolaEnergia3.rect.y += 14
        if bolaEnergia3.rect.y > altura + 120:
            bolaEnergia3.rect.y = 20

#Colisão Paredes
    if hitBox.colliderect(limiteLargura):
        xHitBox = largura - 50
        cringuim.rect.x = largura - 100
        bala.rect.x = largura - 65
    if hitBox.colliderect(limiteLargura0):
        xHitBox = 36
        cringuim.rect.x = 0
        bala.rect.x = 36
    if hitBox.colliderect(limiteBase):
        yHitBox = altura-37
        cringuim.rect.y = altura-90
        bala.rect.y = altura-45
    if hitBox.colliderect(limiteHoriDireita) or hitBox.colliderect(limiteHoriDireita2):
        yHitBox = 555+36
        cringuim.rect.y = 555-18
        bala.rect.y = 555+5
    if hitBox.colliderect(limiteHoriEsquerda):
        yHitBox = 480+36
        cringuim.rect.y = 480-18
        bala.rect.y = 480

    if hitBox.colliderect(limiteMeio):
        yHitBox = 290+36
        cringuim.rect.y = 290 - 18
        bala.rect.y = 290+15

    if hitBox.colliderect(limiteVertDireita):
        xHitBox = 450+36
        cringuim.rect.x = 450-10
        bala.rect.x = 450+20
    if hitBox.colliderect(limiteVertEsquerda):
        xHitBox = 910 - 36
        cringuim.rect.x = 910 - 81
        bala.rect.x = 910 - 45

    if hitBox.colliderect(limiteArvEsquerda):
        xHitBox = 640 - 36
        cringuim.rect.x = 640 - 81
        bala.rect.x = 640 - 45

    if hitBox.colliderect(limiteArvDireita):
        xHitBox = 675 + 36
        cringuim.rect.x = 675 - 10
        bala.rect.x = 675 + 15

    if hitBox.colliderect(limiteArvmeio):
        yHitBox = 535+36
        cringuim.rect.y = 535 - 18
        bala.rect.y = 535

#Colisão Bala-Campo de Força
    if campoDeForca.colliderect(bala):
        bala.rect.y = -64

#Colisão Bala-Antenas
    if linhaAntena1.colliderect(bala):
        bala.rect.y = -64
        contadorAntea1 += 1
        som_tiro.play()
    if linhaAntena2.colliderect(bala):
        bala.rect.y = -64
        contadorAntea2 += 1
        som_tiro.play()
    if linhaAntena3.colliderect(bala):
        bala.rect.y = -64
        contadorAntea3 += 1
        som_tiro.play()

    if contadorAntea1 == 19:
        som_ativação.play()
    if contadorAntea2 == 19:
        som_ativação.play()
    if contadorAntea3 == 19:
        som_ativação.play()

    if contadorAntea1 == 20:
        corAntena1 = (0,255,0)
        #som_ativação.play()
        antenaFuncionando = False
        bolaEnergia.rect.y = -100
    if contadorAntea2 == 20:
        corAntena2 = (0,255,0)
        #som_ativação.play()
        antenaFuncionando2 = False
        bolaEnergia2.rect.y = -100
    if contadorAntea3 == 20:
        corAntena3 = (0,255,0)
        #som_ativação.play()
        antenaFuncionando3 = False
        bolaEnergia3.rect.y = -100

#Colisão Bala-Storm Trooper
    if hitBoxStormTrooper.colliderect(bala):
        bala.rect.y = -100
        vidaStormTrooper -= 1

    if vidaStormTrooper == 0:
        stormTrooperVivo = False
        som_guarda.play()

    if stormTrooperVivo == False:
        stormTrooper.rect.center = -200,-200
        yTiro = -100

#Colisões
    if hitBox.colliderect(globo) or hitBox.colliderect(carro) or hitBox.colliderect(bolaEnergia) or hitBox.colliderect(bolaEnergia2) or hitBox.colliderect(bolaEnergia3) or hitBox.colliderect(stormTrooper):
        vidaJogador -= 1
        xHitBox, yHitBox = largura - 50, altura - 75
        cringuim.rect.center = (largura-50,altura-82)
        bala.rect.center = xHitBox, yHitBox

    if hitBox.colliderect(globo):
        som_bonk.play()
    if hitBox.colliderect(carro):
        som_batida.play()
    if hitBox.colliderect(bolaEnergia) or hitBox.colliderect(bolaEnergia2) or hitBox.colliderect(bolaEnergia3):
        som_zap.play()
    if hitBox.colliderect(stormTrooper):
        som_guarda.play()

# Vidas
    if linux1Vivo == True:
        grupo1.draw(tela)
    if linux2Vivo == True:
        grupo2.draw(tela)
    if linux3Vivo == True:
        grupo3.draw(tela)
    if linux4Vivo == True:
        grupo4.draw(tela)
    if linux5Vivo == True:
        grupo5.draw(tela)
    if linux6Vivo == True:
        grupo6.draw(tela)
    if linux7Vivo == True:
        grupo7.draw(tela)
    if linux8Vivo == True:
        grupo8.draw(tela)
    if linux9Vivo == True:
        grupo9.draw(tela)
    if linux10Vivo == True:
        grupo10.draw(tela)

# Game Over
    if vidaJogador == 9:
        linux10Vivo = False
    if vidaJogador == 8:
        linux9Vivo = False
    if vidaJogador == 7:
        linux8Vivo = False
    if vidaJogador == 6:
        linux7Vivo = False
    if vidaJogador == 5:
        linux6Vivo = False
    if vidaJogador == 4:
        linux5Vivo = False
    if vidaJogador == 3:
        linux4Vivo = False
    if vidaJogador == 2:
        linux3Vivo = False
    if vidaJogador == 1:
        linux2Vivo = False
    if vidaJogador == 0:
        linux1Vivo = False
        derrota(gameOver)

#Vitória
    if hitBox.colliderect(objetivo):
        pygame.mixer.music.stop()
        som_guarda.stop()
        import Boss

# Fundo Parabéns
    if parabensTela == True:
         tela.blit(parabens, (0, 0))
    if event.type == KEYDOWN:
        if event.key == K_KP_ENTER:
             parabensTela = False
             som_vitoria.stop()
             pygame.mixer.music.unpause()
             fps = 60

    pygame.display.flip()