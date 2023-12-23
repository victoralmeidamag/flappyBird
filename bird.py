import pygame, random
from pygame.locals import *

LARGURA = 500
ALTURA = 700
VELOCIDADE = 10
GRAVIDADE = 1
VELOCIDADEJOGO = 10
LARGURACHAO = 2 * LARGURA
ALTURACHAO = 100
TAMANHO_OBSTACULO = 500
LARGURA_OBSTACULO = 80
ESPACO_CANO = 200


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load('passarocima.png').convert_alpha(),
                       pygame.image.load('passaromeio.png').convert_alpha(),
                       pygame.image.load('passarobaixo.png').convert_alpha()]
        
        self.velocidade = VELOCIDADE
        self.atualizaImg = 0
        self.image = pygame.image.load('passarobaixo.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = LARGURA / 2
        self.rect[1] = ALTURA / 2

    def update(self):
        self.atualizaImg = (self.atualizaImg + 1) % 3
        self.image = self.images[self.atualizaImg]
        #ATUALIZA ALTURA
        self.velocidade += GRAVIDADE
        self.rect[1] += self.velocidade

    def saltar(self):
        self.velocidade = -VELOCIDADE


class Base(pygame.sprite.Sprite):
    
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(LARGURACHAO,ALTURACHAO))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = ALTURA - ALTURACHAO


    def update(self):
        self.rect[0] -= VELOCIDADEJOGO
    
def naTela(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

def canosAleatorios(xpos):
    tamanho = random.randint(100,300)
    cano = Obstaculos(False, xpos, tamanho)
    cano_invertido = Obstaculos(True, xpos, ALTURA - tamanho - ESPACO_CANO)
    return(cano,cano_invertido)

class Obstaculos(pygame.sprite.Sprite):
    def __init__(self, inverte, xpos, tamanhoY):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('pipe-green.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(LARGURA_OBSTACULO, TAMANHO_OBSTACULO))
        self.rect = self.image.get_rect()
        self.rect[0] = xpos

        if inverte:
            self.image = pygame.transform.flip(self.image,False, True)
            self.rect[1] = -(self.rect[3] - tamanhoY)
        else:
            self.rect[1] = ALTURA - tamanhoY

        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        self.rect[0] -= VELOCIDADEJOGO