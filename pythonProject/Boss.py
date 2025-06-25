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
fps=5

#Contador
inicio = False
contadorCutScene = 0

#Contador Antenas
contadorAntea1 = 0
contadorAntea2 = 0
contadorAntea3 = 0

#Tela de Parabéns
parabens = pygame.image.load('pythonProject/sprites pinguim/parabéns3.jpeg')
parabens = pygame.transform.scale(parabens,(largura,altura))
parabensTela = True

#Som Vitória Fase 3
som_vitoria = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/burning_love.mp3')
#som_vitoria.set_volume(0.5)
som_vitoria.play()

#Musica de Fundo
pygame.mixer.music.load('pythonProject/Efeitos Sonoros/bossmusic.mp3')
pygame.mixer.music.play(-1,10)
#pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.pause()

#Efeitos Sonoros
som_tiro = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/shooting.mp3')
#som_tiro.set_volume(0.1)

som_ativação = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/smw_coin.wav')

som_bonk = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/bonk.mp3')

som_batida = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/smw_thunder.wav')

som_zap = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/zap.mp3')

som_abertura = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/smw_midway_gate.wav')

som_derrota = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/hello darkness 8 bit.mp3')

som_batidaGelo=pygame.mixer.Sound('pythonProject/Efeitos Sonoros/8-bit-kit-explosion-3_G_minor.wav')
#som_batidaGelo.set_volume(0.1)

som_twitter = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/twitter.mp3')

som_kritter = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/kritter.mp3')

som_moai = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/moai.mp3')
#som_moai.set_volume(0.001)

som_quack = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/quack.mp3')

#Tela Fundo
fundo = pygame.image.load('pythonProject/sprites pinguim/mesapoker.jpg')
fundo = pygame.transform.scale(fundo,(largura,altura))

#Vida
vidaJogador = 10

#Valores da Vida
yVida = 50

#Velocidade
velocidade = 5
#Dash
direcao = 0

#Bala
velocidadeBala = 28
danoBala = 1

#Eixos HitBox
xHitBox, yHitBox = largura//2, altura - 35

#Vida Pato
vidaPato = 50

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
linux9Vivo = True

grupo10 = pygame.sprite.Group()
linux10 = pygame.sprite.Sprite(grupo10)
linux10.image = pygame.image.load('pythonProject/sprites pinguim/linuxguim.png')
linux10.image = pygame.transform.scale(linux10.image,(60,60))
linux10.rect = linux10.image.get_rect()
linux10.rect.center = largura - 760, yVida
linux10Vivo = True

#Sprite Sheet
spriteSheet = pygame.image.load('pythonProject/pinguim/spritesheet pinguim.png').convert_alpha()
spriteCarro = pygame.image.load('pythonProject/sprites pinguim/carrin.png').convert_alpha()
spriteSheetGlobo = pygame.image.load('pythonProject/sprites pinguim/spritesheet_globo.png').convert_alpha()
spriteBird = pygame.image.load('pythonProject/sprites pinguim/passarin.png').convert_alpha()

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
        self.rect.center = (largura//2, altura-45)
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
        self.velocidade = [4,6]

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
        self.rect.x = random.randrange(400, 800, 200)

    def update(self):
        if self.rect.y > altura:
            self.rect.x = random.randrange(400, 800, 120)
            self.rect.y = 0
        self.rect.y +=8

class Passaros(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spriteBird.subsurface((0,0),(831,573))
        self.image = pygame.transform.scale(self.image,(150//4,105//4))
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(0, altura, 80)
        self.rect.x = largura - random.randrange(120, 400, 240)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura
            self.rect.y = random.randrange(altura//4, 450, 240)
        self.rect.x -=4

#Grupos Classes
allSprites = pygame.sprite.Group()
cringuimSprites = pygame.sprite.Group()

carro = Carros()
allSprites.add(carro)

globo = Globo()
allSprites.add(globo)

twitter = Passaros()
allSprites.add(twitter)

twitter2 = Passaros()
allSprites.add(twitter2)

twitter3 = Passaros()
allSprites.add(twitter3)

cringuim = Pinguim()


###Sprites

#Pato
grupoPato = pygame.sprite.Group()
pato = pygame.sprite.Sprite(grupoPato)
pato.image = pygame.image.load('pythonProject/sprites pinguim/pato.png')
pato.image = pygame.transform.scale(pato.image,(628//3,253//3))
pato.rect = pato.image.get_rect()
pato.rect.center = largura//2, -250
patoVivo = True

timerPato = 2

#Moai
grupoMoai = pygame.sprite.Group()
moai = pygame.sprite.Sprite(grupoMoai)
moai.image = pygame.image.load('pythonProject/sprites pinguim/moai.png')
moai.image = pygame.transform.scale(moai.image,(80,80))
moai.rect = moai.image.get_rect()
moai.rect.center = largura//2, altura//2-50
moaiVivo = True

#Placas
corPlaca1,corPlaca2,corPlaca3,corPlaca4,corPlaca5,corPlaca6,corPlaca7 = (255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0)
contadorPlaca1,contadorPlaca2,contadorPlaca3,contadorPlaca4,contadorPlaca5,contadorPlaca6,contadorPlaca7 = 0,0,0,0,0,0,0
cronometro = 3600

#Campo de Força
grupocdf1 = pygame.sprite.Group()
cdf1 = pygame.sprite.Sprite(grupocdf1)
cdf1.image = pygame.image.load('pythonProject/sprites pinguim/campo_de_força.png')
cdf1.image = pygame.transform.scale(cdf1.image,(32*3,32*3))
cdf1.rect = cdf1.image.get_rect()
cdf1.rect.center = (255,565)
cdf1Vivo = True

grupocdf2 = pygame.sprite.Group()
cdf2 = pygame.sprite.Sprite(grupocdf2)
cdf2.image = pygame.image.load('pythonProject/sprites pinguim/campo_de_força.png')
cdf2.image = pygame.transform.scale(cdf2.image,(32*3,32*3))
cdf2.rect = cdf2.image.get_rect()
cdf2.rect.center = (110,360)
cdf2Vivo = True

grupocdf3 = pygame.sprite.Group()
cdf3 = pygame.sprite.Sprite(grupocdf3)
cdf3.image = pygame.image.load('pythonProject/sprites pinguim/campo_de_força.png')
cdf3.image = pygame.transform.scale(cdf3.image,(32*3,32*3))
cdf3.rect = cdf3.image.get_rect()
cdf3.rect.center = (250,150)
cdf3Vivo = True

grupocdf4 = pygame.sprite.Group()
cdf4 = pygame.sprite.Sprite(grupocdf4)
cdf4.image = pygame.image.load('pythonProject/sprites pinguim/campo_de_força.png')
cdf4.image = pygame.transform.scale(cdf4.image,(32*3,32*3))
cdf4.rect = cdf4.image.get_rect()
cdf4.rect.center = (largura//2,120)
cdf4Vivo = True

grupocdf5 = pygame.sprite.Group()
cdf5 = pygame.sprite.Sprite(grupocdf5)
cdf5.image = pygame.image.load('pythonProject/sprites pinguim/campo_de_força.png')
cdf5.image = pygame.transform.scale(cdf5.image,(32*3,32*3))
cdf5.rect = cdf5.image.get_rect()
cdf5.rect.center = (1035,150)
cdf5Vivo = True

grupocdf6 = pygame.sprite.Group()
cdf6 = pygame.sprite.Sprite(grupocdf6)
cdf6.image = pygame.image.load('pythonProject/sprites pinguim/campo_de_força.png')
cdf6.image = pygame.transform.scale(cdf6.image,(32*3,32*3))
cdf6.rect = cdf6.image.get_rect()
cdf6.rect.center = (1170,360)
cdf6Vivo = True

grupocdf7 = pygame.sprite.Group()
cdf7 = pygame.sprite.Sprite(grupocdf7)
cdf7.image = pygame.image.load('pythonProject/sprites pinguim/campo_de_força.png')
cdf7.image = pygame.transform.scale(cdf7.image,(32*3,32*3))
cdf7.rect = cdf7.image.get_rect()
cdf7.rect.center = (1030,565)
cdf7Vivo = True

#Macaco
grupoMacaco = pygame.sprite.Group()
macaco = pygame.sprite.Sprite(grupoMacaco)
macaco.image = pygame.image.load('pythonProject/sprites pinguim/macaco.gif')
macaco.image = pygame.transform.scale(macaco.image,(416//3,288//3))
macaco.rect = macaco.image.get_rect()
macaco.rect.topleft = 980, 200

grupoMacacoVoltando = pygame.sprite.Group()
macacoVoltando = pygame.sprite.Sprite(grupoMacacoVoltando)
macacoVoltando.image = pygame.image.load('pythonProject/sprites pinguim/macaco.gif')
macacoVoltando.image = pygame.transform.scale(macacoVoltando.image,(416//3,288//3))
macacoVoltando.rect = macacoVoltando.image.get_rect()
macacoVoltando.rect.topleft = largura, 200

#Madeiras
grupoMadeira = pygame.sprite.Group()
madeira = pygame.sprite.Sprite(grupoMadeira)
madeira.image = pygame.image.load('pythonProject/sprites pinguim/madeira.png')
madeira.image = pygame.transform.scale(madeira.image,(100,100))
madeira.rect = madeira.image.get_rect()
madeira.rect.topleft = 0,0

grupoMadeira2 = pygame.sprite.Group()
madeira2 = pygame.sprite.Sprite(grupoMadeira2)
madeira2.image = pygame.image.load('pythonProject/sprites pinguim/madeira.png')
madeira2.image = pygame.transform.scale(madeira2.image,(100,100))
madeira2.rect = madeira2.image.get_rect()
madeira2.rect.topleft = largura-100,0

#Gelo
grupoCubo1 = pygame.sprite.Group()
cubo1 = pygame.sprite.Sprite(grupoCubo1)
cubo1.image = pygame.image.load('pythonProject/sprites pinguim/cubo_gelo.png')
cubo1.image = pygame.transform.scale(cubo1.image,(100,80))
cubo1.rect = cubo1.image.get_rect()
cubo1.rect.topleft = largura/2-60, 100

grupoCubo2 = pygame.sprite.Group()
cubo2 = pygame.sprite.Sprite(grupoCubo2)
cubo2.image = pygame.image.load('pythonProject/sprites pinguim/cubo_gelo.png')
cubo2.image = pygame.transform.scale(cubo1.image,(100,80))
cubo2.rect = cubo1.image.get_rect()
cubo2.rect.topleft = largura/2-60, altura-200

#Antenas
grupoAntena = pygame.sprite.Group()
antena = pygame.sprite.Sprite(grupoAntena)
antena.image = pygame.image.load('pythonProject/sprites pinguim/antena.png')
antena.image = pygame.transform.scale(antena.image,(1076//12,1124//12))
antena.rect = antena.image.get_rect()
antena.rect.topright = (910,290)
antenaFuncionando = True

corAntena1 = (255,0,0)

grupoAntena2 = pygame.sprite.Group()
antena2 = pygame.sprite.Sprite(grupoAntena2)
antena2.image = pygame.image.load('pythonProject/sprites pinguim/antena.png')
antena2.image = pygame.transform.scale(antena2.image,(1076//12,1124//12))
antena2.rect = antena2.image.get_rect()
antena2.rect.topright = (460,290)
antenaFuncionando2 = True

corAntena2 = (255,0,0)

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
bolaEnergia2.rect.topright = (440,310)

#Bala
grupoBala = pygame.sprite.Group()
bala = pygame.sprite.Sprite(grupoBala)
bala.image = pygame.image.load('pythonProject/sprites pinguim/bala.png')
bala.image = pygame.transform.scale(bala.image,(64//3,64//3))
bala.rect = bala.image.get_rect()
bala.rect.center = xHitBox,yHitBox
atirando = False

#Sprites Desenho
allSprites.add(bala)

cringuim = Pinguim()
cringuimSprites.add(cringuim)

allSprites.add(antena)
allSprites.add(antena2)

allSprites.add(bolaEnergia)
allSprites.add(bolaEnergia2)

#Fontes
fonteEsc = pygame.font.SysFont('gabriola', 48, True, False)
fonteDesistencia = pygame.font.SysFont('arial', 36, True, False)
fonteGameOver = pygame.font.SysFont('gabriola', 72, True, False)

#Mensagens
mensagem_derrota = 'CRINGE'
mensagem_ESC = 'Aperte ESC Para Reiniciar'
mensagem_desistencia = 'Ou aperte ENTER para render-se ao Pato'

#Textos
texto_ESC = fonteEsc.render(mensagem_ESC, True, (255, 255, 255))
texto_derrota = fonteGameOver.render(mensagem_derrota, True, (255, 0, 0))
texto_desistencia = fonteDesistencia.render(mensagem_desistencia, True, (255, 255, 0))

# Retangulos de Texto
retTextoDerrota = texto_derrota.get_rect()
retTextoDerrota.center = (largura / 2, altura / 2)

#Função Derrota
gameOver = False
def derrota(gameOver):
    global fps,xHitBox,yHitBox,vidaJogador,linux1Vivo,linux2Vivo,linux3Vivo,linux4Vivo,linux5Vivo,linux6Vivo,linux7Vivo,linux8Vivo,linux9Vivo,linux10Vivo,corAntena1,corAntena2,contadorAntea1,contadorAntea2,antenaFuncionando,antenaFuncionando2,corPlaca1,corPlaca2,corPlaca3,corPlaca4,corPlaca5,corPlaca6,corPlaca7,contadorPlaca1, contadorPlaca2, contadorPlaca3, contadorPlaca4, contadorPlaca5, contadorPlaca6, contadorPlaca7
    fps = 30
    pygame.mixer.music.stop()
    xHitBox, yHitBox = largura//2,-35
    cringuim.rect.center = (largura - 50, altura - 82)
    bala.rect.center = xHitBox, yHitBox
    som_derrota.play()
    som_derrota.set_volume(0.25)
    tela.fill((0, 0, 0,))
    tela.blit(texto_derrota, (retTextoDerrota))
    tela.blit(texto_ESC, (0, 50))
    tela.blit(texto_desistencia,(0,100))
    corAntena1,corAntena2 = (255,0,0),(255,0,0)
    corPlaca1,corPlaca2,corPlaca3,corPlaca4,corPlaca5,corPlaca6,corPlaca7 = (255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0),(255,0,0)
    contadorPlaca1, contadorPlaca2, contadorPlaca3, contadorPlaca4, contadorPlaca5, contadorPlaca6, contadorPlaca7 = 0, 0, 0, 0, 0, 0, 0
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            fps = 60
            pygame.mixer.music.play(-1,19)
            pygame.mixer.music.set_volume(0.1)
            som_derrota.stop()
            xHitBox, yHitBox = largura // 2, altura - 35
            cringuim.rect.center = (largura // 2, altura - 45)
            bala.rect.center = xHitBox, yHitBox
            contadorAntea1,contadorAntea2 = 0,0
            vidaJogador = 10
            linux1Vivo,linux2Vivo,linux3Vivo,linux4Vivo,linux5Vivo,linux6Vivo,linux7Vivo,linux8Vivo,linux9Vivo,linux10Vivo = True,True,True,True,True,True,True,True,True,True
            bolaEnergia.rect.topright = (880, 310)
            bolaEnergia2.rect.topright = (440, 310)
            antenaFuncionando,antenaFuncionando2 = True,True
            cdf1.rect.center,cdf2.rect.center,cdf3.rect.center,cdf4.rect.center,cdf5.rect.center,cdf6.rect.center,cdf7.rect.center =  (255,565),(110,360),(250,150),(largura//2,120),(1035,150),(1170,360),(1030,565)
    if event.type == KEYDOWN:
        if event.key == K_KP_ENTER:
            som_derrota.stop()
            import Jogo



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
    hitBoxPato = pygame.draw.rect(tela, (0, 0, 0), [largura // 2 - 110, altura // 2 - 78, 220, 100])

# Fundo Cenário
    tela.blit(fundo, (0, 0))

# Movimentção Personagem
    if contadorCutScene >= 500:
        if xHitBox == largura - 35:
            xHitBox = largura - 50
            cringuim.rect.x = largura - 100
            bala.rect.center = xHitBox, yHitBox

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
# Dash
        if xHitBox == largura - 35:
            xHitBox = largura - 50
            cringuim.rect.x = largura - 100
            bala.rect.center = xHitBox, yHitBox
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

# Atirar
    if contadorCutScene >= 500:
        if pygame.key.get_pressed()[K_e]:
            atirando = True
        if atirando == True:
            bala.rect.y -= velocidadeBala
            if bala.rect.y <= -64:
                bala.rect.center = xHitBox, yHitBox
                atirando = False
# Macaco
    if macaco.rect.topleft <= (largura, 200):
        macaco.rect.x += 4
    if macaco.rect.topleft == (largura, 200):
        macaco.rect.topleft = (980, 200)

    if macacoVoltando.rect.topleft >= (980, 200):
        macacoVoltando.rect.x -= 4
    if macacoVoltando.rect.topleft == (980, 200):
        macacoVoltando.rect.topleft = (largura, 200)

#Placas
    placa1 = pygame.draw.circle(tela,(corPlaca1),(255,565),(40))
    placa2 = pygame.draw.circle(tela, (corPlaca2), (110, 360), (40))
    placa3 = pygame.draw.circle(tela,(corPlaca3),(250,150),(40))
    placa4 = pygame.draw.circle(tela, (corPlaca4), (largura//2, 120), (40))
    placa5 = pygame.draw.circle(tela, (corPlaca5), (1035, 150), (40))
    placa6 = pygame.draw.circle(tela, (corPlaca6), (1170, 360), (40))
    placa7 = pygame.draw.circle(tela, (corPlaca7), (1030, 565), (40))

# Desenhando Classes
    grupoBala.draw(tela)
    grupoPato.draw(tela)
    if contadorCutScene <= 500:
        pato.rect.y += timerPato
        if pato.rect.y == altura // 2 - 60:
            timerPato = 0
    if contadorCutScene >= 500:
        contadorCutScene = 501

        grupocdf1.draw(tela)
        grupocdf2.draw(tela)
        grupocdf3.draw(tela)
        grupocdf4.draw(tela)
        grupocdf5.draw(tela)
        grupocdf6.draw(tela)
        grupocdf7.draw(tela)

        allSprites.draw(tela)
        allSprites.update()

        grupoMadeira.draw(tela)
        grupoMadeira2.draw(tela)
        grupoCubo2.draw(tela)
        grupoCubo1.draw(tela)
        grupoMacaco.draw(tela)
        grupoMacacoVoltando.draw(tela)

        # Antenas
        linhaAntena1 = pygame.draw.line(tela, (corAntena1), (820, 290 + 93), (820 + 89, 290 + 93), (5))
        linhaAntena2 = pygame.draw.line(tela, (corAntena2), (370, 290 + 93), (370 + 89, 290 + 93), (5))
        # Colisão Bala-Antenas
        if linhaAntena1.colliderect(bala):
            bala.rect.y = -64
            contadorAntea1 += danoBala
            som_tiro.play()
        if linhaAntena2.colliderect(bala):
            bala.rect.y = -64
            contadorAntea2 += danoBala
            som_tiro.play()

        if contadorAntea1 == 19:
            som_ativação.play()
        if contadorAntea2 == 19:
            som_ativação.play()

        if contadorAntea1 == 20:
            corAntena1 = (0, 255, 0)
            antenaFuncionando = False
            bolaEnergia.rect.y = -100
        if contadorAntea2 == 20:
            corAntena2 = (0, 255, 0)
            antenaFuncionando2 = False
            bolaEnergia2.rect.y = -100
        #Desativando Campos de Força
        if antenaFuncionando == False and antenaFuncionando2 == False:
            cdf1.rect.y,cdf2.rect.y,cdf3.rect.y,cdf4.rect.y,cdf5.rect.y,cdf6.rect.y,cdf7.rect.y = -100,-100,-100,-100,-100,-100,-100

        #Apertando Placas
        if hitBox.colliderect(placa1):
            corPlaca1 = (0,255,0)
        if corPlaca1 == (0,255,0):
            contadorPlaca1 += 1
        if contadorPlaca1 == cronometro:
            corPlaca1 = (255, 0, 0)
            contadorPlaca1 = 0

        if hitBox.colliderect(placa2):
            corPlaca2 = (0,255,0)
        if corPlaca2 == (0,255,0):
            contadorPlaca2 += 1
        if contadorPlaca2 == cronometro:
            corPlaca2 = (255, 0, 0)
            contadorPlaca2 = 0

        if hitBox.colliderect(placa3):
            corPlaca3 = (0,255,0)
        if corPlaca3 == (0,255,0):
            contadorPlaca3 += 1
        if contadorPlaca3 == cronometro:
            corPlaca3 = (255, 0, 0)
            contadorPlaca3 = 0

        if hitBox.colliderect(placa4):
            corPlaca4 = (0,255,0)
        if corPlaca4 == (0,255,0):
            contadorPlaca4 += 1
        if contadorPlaca4 == cronometro:
            corPlaca4 = (255, 0, 0)
            contadorPlaca4 = 0

        if hitBox.colliderect(placa5):
            corPlaca5 = (0,255,0)
        if corPlaca5 == (0,255,0):
            contadorPlaca5 += 1
        if contadorPlaca5 == cronometro:
            corPlaca5 = (255, 0, 0)
            contadorPlaca5 = 0

        if hitBox.colliderect(placa6):
            corPlaca6 = (0,255,0)
        if corPlaca6 == (0,255,0):
            contadorPlaca6 += 1
        if contadorPlaca6 == cronometro:
            corPlaca6 = (255, 0, 0)
            contadorPlaca6 = 0

        if hitBox.colliderect(placa7):
            corPlaca7 = (0,255,0)
        if corPlaca7 == (0,255,0):
            contadorPlaca7 += 1
        if contadorPlaca7 == cronometro:
            corPlaca7 = (255, 0, 0)
            contadorPlaca7 = 0

        #Moai
        if moaiVivo == True:
            grupoMoai.draw(tela)
        if corPlaca3 == (0, 255, 0) and corPlaca1 == (0, 255, 0) and corPlaca2 == (
        0, 255, 0) and corPlaca4 == (0, 255, 0) and corPlaca5 == (0, 255, 0) and corPlaca6 == (0, 255, 0) and corPlaca7 == (0, 255, 0):
            moaiVivo = False
            som_moai.play()
            som_moai.set_volume(0.1)
        else:
            moaiVivo = True
            som_moai.stop()



    cringuimSprites.draw(tela)
    cringuimSprites.update()

#Pato
    if vidaPato <= 0:
        patoVivo = False
    if patoVivo == True:
        allSprites.add(pato)
    if moaiVivo == False:
        if hitBoxPato.colliderect(bala):
            bala.rect.y = -100
            vidaPato -= 1
            som_quack.play()
            som_tiro.play()

# Madeira
    madeira.rect.y += 6
    if madeira.rect.y >= altura:
        madeira.rect.topleft = (0, 0)
    madeira2.rect.y += 8
    if madeira2.rect.y >= altura:
        madeira2.rect.topleft = (largura-100, 0)

# Gelos
    if cubo2.rect.topleft[0] >= largura:
        cubo2.rect.x = 0
    cubo2.rect.x += 12
    if cubo1.rect.topright[0] < 0:
        cubo1.rect.x = largura
    cubo1.rect.x -= 4

# Ataque Antenas
    if antenaFuncionando == True:
        bolaEnergia.rect.y += 10
        if bolaEnergia.rect.y > altura + 120:
            bolaEnergia.rect.y = 290

    if antenaFuncionando2 == True:
        bolaEnergia2.rect.y += 10
        if bolaEnergia2.rect.y > altura + 120:
            bolaEnergia2.rect.y = 290

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
#Contador CutScene
    if inicio == True:
        contadorCutScene += 1

#Colisão
    if hitBox.colliderect(globo) or hitBox.colliderect(bolaEnergia) or hitBox.colliderect(bolaEnergia2) or hitBox.colliderect(cubo1) or hitBox.colliderect(cubo2) or hitBox.colliderect(madeira) or hitBox.colliderect(madeira2) or hitBox.colliderect(twitter) or hitBox.colliderect(twitter2) or hitBox.colliderect(twitter3) or hitBox.colliderect(macaco) or hitBox.colliderect(macacoVoltando):
        vidaJogador -= 1
        xHitBox, yHitBox = largura//2, altura - 35
        cringuim.rect.center = (largura//2, altura - 45)
        bala.rect.center = xHitBox, yHitBox

    if hitBox.colliderect(cdf1) or hitBox.colliderect(cdf2) or hitBox.colliderect(cdf3) or hitBox.colliderect(cdf4) or hitBox.colliderect(cdf5) or hitBox.colliderect(cdf6) or hitBox.colliderect(cdf7):
        vidaJogador -= 1
        xHitBox, yHitBox = largura // 2, altura - 35
        cringuim.rect.center = (largura // 2, altura - 45)
        bala.rect.center = xHitBox, yHitBox
        som_zap.play()

    if hitBox.colliderect(globo) or hitBox.colliderect(madeira) or hitBox.colliderect(madeira2):
        som_bonk.play()
    if hitBox.colliderect(cubo1) or hitBox.colliderect(cubo2):
        som_batidaGelo.play()
    if hitBox.colliderect(bolaEnergia) or hitBox.colliderect(bolaEnergia2):
        som_zap.play()
    if hitBox.colliderect(twitter) or hitBox.colliderect(twitter2) or hitBox.colliderect(twitter3):
        som_twitter.play()
    if hitBox.colliderect(macaco) or hitBox.colliderect(macacoVoltando):
        som_kritter.play()

    if hitBox.colliderect(carro):
        vidaJogador -= 1
        xHitBox, yHitBox = largura // 2, altura - 35
        cringuim.rect.center = (largura // 2, altura - 45)
        bala.rect.center = xHitBox, yHitBox
        carro.rect.y = -50
        som_batida.play()



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
    if vidaPato == 0:
        pygame.mixer.music.stop()
        som_moai.stop()
        import Final

# Fundo Parabéns
    if parabensTela == True:
        tela.blit(parabens, (0, 0))

    if event.type == KEYDOWN:
        if event.key == K_KP_ENTER:
            parabensTela = False
            inicio = True
            som_vitoria.stop()
            pygame.mixer.music.unpause()
            fps = 60


    pygame.display.flip()