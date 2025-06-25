import pygame
from pygame.locals import *
from sys import exit
import random
pygame.init()
pygame.mixer.init()

#Eixos da Tela
largura=1280
altura=720

#Eixos HitBox
xHitBox, yHitBox = 55, altura/2+33

#Valores da Vida
yVida1,yVida2,yVida3,yVida4,yVida5 = 50,50,50,50,50

#Valor Vida
vidaJogador=5

#Vidas Imagem
grupo1 = pygame.sprite.Group()
linux1 = pygame.sprite.Sprite(grupo1)
linux1.image = pygame.image.load('pythonProject/sprites pinguim/linuxguim.png')
linux1.image = pygame.transform.scale(linux1.image,(60,60))
linux1.rect = linux1.image.get_rect()
linux1.rect.center = largura - 40, yVida3
linux1Vivo = True

grupo2 = pygame.sprite.Group()
linux2 = pygame.sprite.Sprite(grupo2)
linux2.image = pygame.image.load('pythonProject/sprites pinguim/linuxguim.png')
linux2.image = pygame.transform.scale(linux2.image,(60,60))
linux2.rect = linux2.image.get_rect()
linux2.rect.center = largura - 120, yVida2

linux2Vivo = True

grupo3 = pygame.sprite.Group()
linux3 = pygame.sprite.Sprite(grupo3)
linux3.image = pygame.image.load('pythonProject/sprites pinguim/linuxguim.png')
linux3.image = pygame.transform.scale(linux3.image,(60,60))
linux3.rect = linux3.image.get_rect()
linux3.rect.center = largura - 200, yVida1
linux3Vivo = True

grupo4 = pygame.sprite.Group()
linux4 = pygame.sprite.Sprite(grupo4)
linux4.image = pygame.image.load('pythonProject/sprites pinguim/linuxguim.png')
linux4.image = pygame.transform.scale(linux4.image,(60,60))
linux4.rect = linux4.image.get_rect()
linux4.rect.center = largura - 280, yVida1
linux4Vivo = True

grupo5 = pygame.sprite.Group()
linux5 = pygame.sprite.Sprite(grupo5)
linux5.image = pygame.image.load('pythonProject/sprites pinguim/linuxguim.png')
linux5.image = pygame.transform.scale(linux5.image,(60,60))
linux5.rect = linux5.image.get_rect()
linux5.rect.center = largura - 360, yVida1
linux5Vivo = True

#Cores Placas
corBaseEsquerda = (255,0,0)
corBaseDireita = (255,0,0)
corTopoEsquerda = (255,0,0)
corTopoDireita = (255,0,0)
corMeio = (255,0,0)

#Contador Placas
contadorBaseEsquerda = 0
contadorBaseDireita = 0
contadorTopoEsquerda = 0
contadorTopoDireita = 0
contadorMeio = 0
cronometro = 900

#Inicialização
tela=pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Masmorras&Pinguins')
clock=pygame.time.Clock()

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

#Tela de Parabéns
parabens = pygame.image.load('pythonProject/sprites pinguim/parabens1.jpeg')
parabens = pygame.transform.scale(parabens,(largura,altura))
parabensTela = True

#Musica de Fundo
pygame.mixer.music.load('pythonProject/Efeitos Sonoros/Jungle8bit.mp3')
pygame.mixer.music.play(-1,35)
#pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.pause()

#Som Vitória Fase 1
som_vitoria=pygame.mixer.Sound('pythonProject/Efeitos Sonoros/champions_8bit.mp3')
#som_vitoria.set_volume(0.5)
som_vitoria.play()

#Sons
som_bonk = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/bonk.mp3')

som_twitter = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/twitter.mp3')

som_kritter = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/kritter.mp3')

som_moai = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/moai.mp3')
#som_moai.set_volume(0.01)

som_derrota = pygame.mixer.Sound('pythonProject/Efeitos Sonoros/hello darkness 8 bit.mp3')
#som_derrota.set_volume(0.25)

#Variaveis Jogador
velocidade = 5

#fps
fps=10

#Fundo
fundo = pygame.image.load('pythonProject/sprites pinguim/floresta.jpg')
fundo = pygame.transform.scale(fundo,(largura,altura))


#Sprite Sheet
spriteSheet = pygame.image.load('pythonProject/pinguim/spritesheet pinguim.png').convert_alpha()
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
        self.rect.topleft = (10,altura/2-20)

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
        self.rect.x -=6

allSprites = pygame.sprite.Group()
cringuim = Pinguim()
allSprites.add(cringuim)

twitter = Passaros()
allSprites.add(twitter)

twitter2 = Passaros()
allSprites.add(twitter2)

twitter3 = Passaros()
allSprites.add(twitter3)

#Moai
grupoMoai = pygame.sprite.Group()
moai = pygame.sprite.Sprite(grupoMoai)
moai.image = pygame.image.load('pythonProject/sprites pinguim/moai.png')
moai.image = pygame.transform.scale(moai.image,(120,120))
moai.rect = moai.image.get_rect()
moai.rect.topleft = largura-120, altura//2-80-50
moaiVivo = True

#Arvore
tree = pygame.sprite.Sprite()
tree.image = pygame.image.load('pythonProject/sprites pinguim/tree.png')
tree.image = pygame.transform.scale(tree.image,(200,200))
tree.rect = tree.image.get_rect()
tree.rect.topleft = largura-185, altura//2-15

allSprites.add(tree)

#Macaco
grupoMacaco = pygame.sprite.Group()
macaco = pygame.sprite.Sprite(grupoMacaco)
macaco.image = pygame.image.load('pythonProject/sprites pinguim/macaco.gif')
macaco.image = pygame.transform.scale(macaco.image,(416//3,288//3))
macaco.rect = macaco.image.get_rect()
macaco.rect.topleft = 980, 450

grupoMacacoVoltando = pygame.sprite.Group()
macacoVoltando = pygame.sprite.Sprite(grupoMacacoVoltando)
macacoVoltando.image = pygame.image.load('pythonProject/sprites pinguim/macaco.gif')
macacoVoltando.image = pygame.transform.scale(macacoVoltando.image,(416//3,288//3))
macacoVoltando.rect = macacoVoltando.image.get_rect()
macacoVoltando.rect.topleft = largura, 450

#Madeiras
grupoMadeira = pygame.sprite.Group()
madeira = pygame.sprite.Sprite(grupoMadeira)
madeira.image = pygame.image.load('pythonProject/sprites pinguim/madeira.png')
madeira.image = pygame.transform.scale(madeira.image,(100,100))
madeira.rect = madeira.image.get_rect()
madeira.rect.topleft = 410,0

grupoMadeira2 = pygame.sprite.Group()
madeira2 = pygame.sprite.Sprite(grupoMadeira2)
madeira2.image = pygame.image.load('pythonProject/sprites pinguim/madeira.png')
madeira2.image = pygame.transform.scale(madeira2.image,(100,100))
madeira2.rect = madeira2.image.get_rect()
madeira2.rect.topleft = 720,0

#Função Game Over
gameOver = False
def derrota(gameOver):
    global fps,xHitBox,yHitBox,vidaJogador,yVida1,yVida2,yVida3,yVida4,yVida5,linux1Vivo,linux2Vivo,linux3Vivo,linux4Vivo,linux5Vivo,corBaseDireita,corTopoDireita,corBaseEsquerda,corTopoEsquerda,corMeio
    fps = 30
    pygame.mixer.music.stop()
    xHitBox, yHitBox = 55, altura / 2 + 33+1000
    cringuim.rect.x, cringuim.rect.y = 10, altura / 2 - 20
    som_derrota.play()
    som_derrota.set_volume(0.25)
    tela.fill((0, 0, 0,))
    tela.blit(texto_derrota, (retTextoDerrota))
    tela.blit(texto_ESC, (0, 50))
    corBaseEsquerda = (255, 0, 0)
    corBaseDireita = (255, 0, 0)
    corTopoEsquerda = (255, 0, 0)
    corTopoDireita = (255, 0, 0)
    corMeio = (255, 0, 0)
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            fps = 60
            pygame.mixer.music.play(-1, 35)
            pygame.mixer.music.set_volume(0.1)
            som_derrota.stop()
            yHitBox = altura / 2 + 33
            vidaJogador = 5
            linux1Vivo,linux2Vivo,linux3Vivo,linux4Vivo,linux5Vivo = True,True,True,True,True

#LAÇO PRINCIPAL
while True:
    clock.tick(fps)
    tela.fill((0,0,0,))

#Quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

#HitBox
    hitBox = pygame.draw.circle(tela, [255, 0, 0], (xHitBox, yHitBox), (35))

# Paredes
    limiteVerde = pygame.draw.line(tela, (0, 255, 0), (0, 275), (510, 275), (5))
    limiteAzul = pygame.draw.line(tela, (0, 0, 255), (520, 140), (1035, 140), (5))
    limiteVermelho = pygame.draw.line(tela, (255, 0, 0), (1050, 230), (largura, 230), (5))

    limiteLateralTopo1 = pygame.draw.line(tela, (255, 255, 255), (520, 270), (520, 140), (5))
    limiteLateralTopo2 = pygame.draw.line(tela, (255, 255, 255), (1033, 140), (1033, 220), (5))

    limiteLateralBase1 = pygame.draw.line(tela, (255, 255, 255), (155, 535), (155, 628), (5))
    limiteLateralBase2 = pygame.draw.line(tela, (255, 255, 255), (695, 628), (695, 558), (5))

    limiteMoai = pygame.draw.line(tela, (255, 255, 255), (largura - 120, altura // 2 - 80 - 50),
                                  (largura - 120, altura // 2), (5))
    limiteTree = pygame.draw.line(tela, (255, 255, 255), (largura - 200, altura // 2),
                                  (largura - 200, altura // 2 + 200), (5))
    limiteVerdeBase = pygame.draw.line(tela, (0, 255, 0), (0, 525), (145, 525), (5))
    limiteAzulBase = pygame.draw.line(tela, (0, 0, 255), (155, 628), (695, 628), (5))
    limiteVermelhoBase = pygame.draw.line(tela, (255, 0, 0), (705, 548), (largura, 548), (5))


#Fundo Cenário
    tela.blit(fundo, (0, 0))

#Placas
    placaBaseEsquerda = pygame.draw.rect(tela,(corBaseEsquerda),(165,560,60,60))
    placaBaseDireita = pygame.draw.rect(tela, (corBaseDireita), (625, 565, 60, 60))
    placaTopoEsquerda = pygame.draw.rect(tela, (corTopoEsquerda), (535, 160, 60, 60))
    placaTopoDireita = pygame.draw.rect(tela, (corTopoDireita), (965, 145, 60, 60))
    placaMeio = pygame.draw.rect(tela, (corMeio), (1015, 480, 60, 60))

#Moai
    if moaiVivo == True:
        grupoMoai.draw(tela)
    if corBaseEsquerda == (0,255,0) and corBaseDireita == (0,255,0) and corTopoEsquerda == (0,255,0) and corTopoDireita == (0,255,0) and corMeio == (0,255,0):
        moaiVivo = False
        som_moai.play()
        som_moai.set_volume(0.1)
    else:
        moaiVivo = True
        som_moai.stop()

#Madeira
    grupoMadeira.draw(tela)
    madeira.rect.y += 8
    if madeira.rect.y >= altura:
        madeira.rect.topleft = (410,0)

    grupoMadeira2.draw(tela)
    madeira2.rect.y += 10
    if madeira2.rect.y >= altura:
        madeira2.rect.topleft = (720, 0)

#Macaco
    if macaco.rect.topleft <= (largura,450):
        grupoMacaco.draw(tela)
        macaco.rect.x += 4
    if macaco.rect.topleft == (largura,450):
        macaco.rect.topleft = (980, 450)

    if macacoVoltando.rect.topleft >=(980,450):
        grupoMacacoVoltando.draw(tela)
        macacoVoltando.rect.x -= 4
    if macacoVoltando.rect.topleft == (980,450):
        macacoVoltando.rect.topleft = (largura, 450)

#Colisões Paredes
    if hitBox.colliderect(limiteVerde):
        cringuim.rect.y = 270
        yHitBox = 324
    if hitBox.colliderect(limiteAzul):
        cringuim.rect.y = 140
        yHitBox = 324-130
    if hitBox.colliderect(limiteVermelho):
        cringuim.rect.y = 220
        yHitBox = 324-50

    if hitBox.colliderect(limiteLateralTopo1):
        cringuim.rect.x = 520-10
        xHitBox = 520+35
    if hitBox.colliderect(limiteLateralTopo2):
        cringuim.rect.x = 1033-80
        xHitBox = 1033-35

    if hitBox.colliderect(limiteLateralBase1):
        cringuim.rect.x = 155-10
        xHitBox = 155+35
    if hitBox.colliderect(limiteLateralBase2):
        cringuim.rect.x = 695-80
        xHitBox = 695-35

    if hitBox.colliderect(limiteVerdeBase):
        cringuim.rect.y = 430
        yHitBox = 485
    if hitBox.colliderect(limiteAzulBase):
        cringuim.rect.y = 533
        yHitBox = 588
    if hitBox.colliderect(limiteVermelhoBase):
        cringuim.rect.y = 453
        yHitBox = 508

#Colisão Moai
    if moaiVivo == True:
        if hitBox.colliderect(limiteMoai):
            xHitBox = largura - 120 - 35
            cringuim.rect.x = largura - 120 - 80

# Colisão Arvore
    if hitBox.colliderect(limiteTree):
        xHitBox = largura - 235
        cringuim.rect.x = largura - 280

#Apertando Placas
    if hitBox.colliderect(placaBaseEsquerda):
        corBaseEsquerda = (0,255,0)
    if corBaseEsquerda == (0,255,0):
        contadorBaseEsquerda += 1
    if contadorBaseEsquerda == cronometro:
        corBaseEsquerda = (255, 0, 0)
        contadorBaseEsquerda = 0

    if hitBox.colliderect(placaBaseDireita):
        corBaseDireita = (0,255,0)
    if corBaseDireita == (0,255,0):
        contadorBaseDireita += 1
    if contadorBaseDireita == cronometro:
        corBaseDireita = (255, 0, 0)
        contadorBaseDireita = 0

    if hitBox.colliderect(placaTopoEsquerda):
        corTopoEsquerda = (0,255,0)
    if corTopoEsquerda == (0,255,0):
        contadorTopoEsquerda += 1
    if contadorTopoEsquerda == cronometro:
        corTopoEsquerda = (255, 0, 0)
        contadorTopoEsquerda = 0


    if hitBox.colliderect(placaTopoDireita):
        corTopoDireita = (0,255,0)
    if corTopoDireita == (0,255,0):
        contadorTopoDireita += 1
    if contadorTopoDireita == cronometro:
        corTopoDireita = (255, 0, 0)
        contadorTopoDireita = 0


    if hitBox.colliderect(placaMeio):
        corMeio = (0,255,0)
    if corMeio == (0,255,0):
        contadorMeio += 1
    if contadorMeio == cronometro:
        corMeio = (255, 0, 0)
        contadorMeio = 0

#Colisões Passaros
    if hitBox.colliderect(twitter):
        vidaJogador -= 1
        xHitBox, yHitBox = 55, altura / 2 + 33
        cringuim.rect.x, cringuim.rect.y = 10, altura/2-20
        som_twitter.play()
        twitter.rect.x = -100
    if hitBox.colliderect(twitter2):
        vidaJogador -= 1
        xHitBox, yHitBox = 55, altura / 2 + 33
        cringuim.rect.x, cringuim.rect.y = 10, altura/2-20
        som_twitter.play()
        twitter2.rect.x = -100
    if hitBox.colliderect(twitter3):
        vidaJogador -= 1
        xHitBox, yHitBox = 55, altura / 2 + 33
        cringuim.rect.x, cringuim.rect.y = 10, altura/2-20
        som_twitter.play()
        twitter3.rect.x = -100

#Colisões Macacos
    if hitBox.colliderect(macaco) or hitBox.colliderect(macacoVoltando):
        vidaJogador -= 1
        xHitBox, yHitBox = 55, altura / 2 + 33
        cringuim.rect.x, cringuim.rect.y = 10, altura / 2 - 20
        som_kritter.play()

#Colisão Madeira
    if hitBox.colliderect(madeira) or hitBox.colliderect(madeira2):
        vidaJogador -= 1
        xHitBox, yHitBox = 55, altura / 2 + 33
        cringuim.rect.x, cringuim.rect.y = 10, altura / 2 - 20
        som_bonk.play()


#Movimentção Personagem
    if pygame.key.get_pressed()[K_UP]:
        cringuim.rect.y -= velocidade
        yHitBox -= velocidade
        cringuim.andar()
    if pygame.key.get_pressed()[K_DOWN]:
        cringuim.rect.y += velocidade
        yHitBox += velocidade
        cringuim.andar()
    if pygame.key.get_pressed()[K_RIGHT]:
        cringuim.rect.x += velocidade
        xHitBox += velocidade
        cringuim.andar()
    if pygame.key.get_pressed()[K_LEFT]:
        cringuim.rect.x -= velocidade
        xHitBox -= velocidade
        cringuim.andar()

#Desenhando Player
    allSprites.draw(tela)
    allSprites.update()

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

# Game Over
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
    if xHitBox > largura+35:
        pygame.mixer.music.stop()
        som_moai.stop()
        import Fase_3

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


