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

#Eixos do inimigo Vermelho
xRet_Verm=largura/2-60 #retângulo vermelho
yRet_Verm=altura/2-50 #retângulo vermelho

#Eixos do inimigo Verde
xRet_Verd=largura/2-60 #retângulo verde
yRet_Verd=altura/2-50 #retângulo verde

#Eixos do Jogador
xJogador=largura/2
yJogador=altura-50

#Valores da Vida
yVida1,yVida2,yVida3=50,50,50

#Valor Vida
vidaJogador=3

#Pontos
pontos=0

#musica de fundo
pygame.mixer.music.load('pythonProject/Efeitos Sonoros/Top Gear Remix.mp3')
pygame.mixer.music.play(-1,3,0)
#pygame.mixer.music.set_volume(0.25)


#efeitos
som_batida=pygame.mixer.Sound('pythonProject/Efeitos Sonoros/8-bit-kit-explosion-3_G_minor.wav')
#som_batida.set_volume(0.15)
som_ponto=pygame.mixer.Sound('pythonProject/Efeitos Sonoros/smw_coin.wav')
som_derrota=pygame.mixer.Sound('pythonProject/Efeitos Sonoros/hello darkness 8 bit.mp3')
#som_derrota.set_volume(0.25)


#Sprites
xPinguim = xJogador
yPinguim = yJogador
class Pinguim(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('pythonProject/pinguim/sprite_0.png'))
        self.sprites.append(pygame.image.load('pythonProject/pinguim/sprite_1.png'))
        self.sprites.append(pygame.image.load('pythonProject/pinguim/sprite_2.png'))
        self.sprites.append(pygame.image.load('pythonProject/pinguim/sprite_3.png'))
        self.sprites.append(pygame.image.load('pythonProject/pinguim/sprite_4.png'))
        self.sprites.append(pygame.image.load('pythonProject/pinguim/sprite_5.png'))

        self.atual = 0

        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image,(135,120))

        self.rect = self.image.get_rect()
        self.rect.center = xJogador, yJogador-10

        self.animacaoFrente = False
        self.animacaoCostas = False

    def andarBaixo(self):
        self.animacaoFrente = True
    def andarCima(self):
        self.animacaoCostas = True


    def update(self):
        if self.animacaoFrente == True:
            self.atual += 0.3
        if self.atual >= 3:
            self.atual = 0
            self.animacaoFrente = False
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (135, 120))

    def update(self):
        if self.animacaoCostas == True:
            self.atual += 0.3
        if self.atual >= 6:
            self.atual = 3
            self.animacaoCostas = False
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (135, 120))


allSprites = pygame.sprite.Group()
player = Pinguim()
allSprites.add(player)

#Funções Game Over
gameover=False
def derrota (gameover):
    global fps,pontos,yVida1,yVida2,yVida3,yJogador,xRet_Verd,xRet_Verm,vidaJogador,linux1Vivo,linux2Vivo,linux3Vivo
    fps = 600
    pygame.mixer.music.stop()
    som_derrota.play()
    pontos = -1
    yVida1 = -50
    tela.fill((0,0,0))
    tela.blit(texto_derrota, (retTextoDerrota))
    tela.blit(texto_ESC, (0, 50))
    yJogador = altura - 50
    player.rect.y = yJogador - 65
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            fps = 60
            pygame.mixer.music.play(-1, 3, 0)
            pygame.mixer.music.set_volume(0.25)
            som_derrota.stop()
            som_derrota.set_volume(0.25)
            vidaJogador = 3
            yVida1,yVida2,yVida3 = 50,50,50
            linux1Vivo,linux2Vivo,linux3Vivo = True,True,True
            pontos = 0

#Gelo
grupoCubo1 = pygame.sprite.Group()
cubo1 = pygame.sprite.Sprite(grupoCubo1)
cubo1.image = pygame.image.load('pythonProject/sprites pinguim/cubo_gelo.png')
cubo1.image = pygame.transform.scale(cubo1.image,(120,100))
cubo1.rect = cubo1.image.get_rect()
cubo1.rect.topleft = xRet_Verd, yRet_Verd

grupoCubo2 = pygame.sprite.Group()
cubo2 = pygame.sprite.Sprite(grupoCubo2)
cubo2.image = pygame.image.load('pythonProject/sprites pinguim/cubo_gelo.png')
cubo2.image = pygame.transform.scale(cubo1.image,(120,100))
cubo2.rect = cubo1.image.get_rect()
cubo2.rect.topleft = xRet_Verd, yRet_Verd


#Vidas Imagem
grupo1 = pygame.sprite.Group()
linux1 = pygame.sprite.Sprite(grupo1)
linux1.image = pygame.image.load('pythonProject/sprites pinguim/linuxguim.png')
linux1.image = pygame.transform.scale(linux1.image,(60,60))
linux1.rect = linux1.image.get_rect()
linux1.rect.center = largura - 200, yVida3
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
linux3.rect.center = largura - 40, yVida1
linux3Vivo = True


#Fundo Imagem
fundo = pygame.image.load('pythonProject/sprites pinguim/floresta_nevada.png').convert()
fundo = pygame.transform.scale(fundo,(largura,altura))

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
    jogador = pygame.draw.circle(tela, [255, 0, 0], (xJogador, yJogador), (50))  # Jogador

#Fundo Tela
    if vidaJogador>0:
     tela.blit(fundo,(0,0))

# Fontes
    fonte_padrao = pygame.font.SysFont('gabriola', 72, True, False)
    fonteEsc = pygame.font.SysFont('gabriola', 48, True, False)
    fonteGameOver = pygame.font.SysFont('gabriola', 72, True, False)

# mensagens
    marcador = f'Pontos: {pontos}'
    mensagem_derrota = 'OS PINGUIS MORRERAM! SEU CRINGE!!!'
    mensagem_ESC = 'Aperte ESC Para Reiniciar'

# textos
    texto_marcador = fonte_padrao.render(marcador, False, (0,0,0))
    texto_ESC = fonteEsc.render(mensagem_ESC, True, (255, 255, 255))
    texto_derrota = fonteGameOver.render(mensagem_derrota, True, (255, 0, 0))

# Retangulos de Texto
    retTextoDerrota = texto_derrota.get_rect()
    retTextoDerrota.center = (largura / 2, altura / 2)

# Inimigos
    grupoCubo1.draw(tela)
    grupoCubo2.draw(tela)

# Vidas
    if linux1Vivo == True:
        grupo1.draw(tela)
    if linux2Vivo == True:
        grupo2.draw(tela)
    if linux3Vivo == True:
        grupo3.draw(tela)

#Movimento Jogador
    if pontos <3:
        if pygame.key.get_pressed()[K_UP]:
            yJogador -= 12
            player.rect.y -=12
            player.andarCima()
        if pygame.key.get_pressed()[K_DOWN]:
            yJogador += 12
            player.rect.y += 12
            player.andarBaixo()
    if pontos>=3 and pontos<5:
        if pygame.key.get_pressed()[K_UP]:
            yJogador -= 24
            player.rect.y -= 24
            player.andarCima()
        if pygame.key.get_pressed()[K_DOWN]:
            yJogador += 24
            player.rect.y += 24
            player.andarBaixo()
    if pontos>=5 and pontos<=7:
        if pygame.key.get_pressed()[K_UP]:
            yJogador -= 32
            player.rect.y -= 32
            player.andarCima()
        if pygame.key.get_pressed()[K_DOWN]:
            yJogador += 32
            player.rect.y += 32
            player.andarBaixo()

#MOVIMENTAÇÃO inimigos
    if cubo2.rect.topleft[0] >= largura:
        #xRet_Verm = 0
        cubo2.rect.x = 0
    cubo2.rect.x += 16
    if cubo1.rect.topright[0] < 0:
        cubo1.rect.x = largura
    cubo1.rect.x -= 8

#Progresso Jogador
    if yJogador<0:
        som_ponto.play()
        yJogador=altura
        pontos+=1 #Pontuando
    if yJogador>altura-50:
        yJogador = altura-50
        player.rect.y = yJogador-65

#COLISÕES
    if jogador.colliderect(cubo1):
        som_batida.play()
        yJogador = altura-50
        vidaJogador-=1
        player.rect.y = yJogador - 65

    if jogador.colliderect(cubo2):
        som_batida.play()
        yJogador = altura-50
        vidaJogador-=1
        player.rect.y = yJogador - 65
#progressão
    #Vermelho
    if pontos>=3:
        cubo2.rect.x += 24

    elif pontos>=5:
        cubo2.rect.x += 32
    elif pontos>=7:
        cubo2.rect.x += 80
    #verde
    if pontos>=3:
        cubo1.rect.x -= 16
    elif pontos>=5:
        cubo1.rect.x -= 24
    elif pontos>=7:
        cubo1.rect.x -= 72

#Vitória
    if pontos<8 and pontos>=0:
        tela.blit(texto_marcador, (0, 0))
    if pontos==8:
        pygame.mixer.music.stop()
        import Fase_2
 # Game Over
    if vidaJogador==2:
        linux1Vivo = False
    if vidaJogador==1:
        linux2Vivo = False
    if vidaJogador==0:
        linux3Vivo = False
        gameover=True
        derrota(gameover)

#Desenhando o Pinguim
    allSprites.draw(tela)
    allSprites.update()

    pygame.display.flip()
