import pygame
from pygame.locals import *

LARGURA = 500
ALTURA = 700
VELOCIDADE = 10
GRAVIDADE = 1

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load('passarocima.png').convert_alpha(),
                       pygame.image.load('passaromeio.png').convert_alpha(),
                       pygame.image.load('passarobaixo.png').convert_alpha()]
        
        self.velocidade = VELOCIDADE
        self.atualizaImg = 0
        self.image = pygame.image.load('passaromeio.png').convert_alpha()
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


class base(pygame.sprite.Sprite):
    def __init__(self, largura, altura):
        self.image = pygame.image.load('base.png')
        self.image = pygame.transform.scale(self.image(largura,altura))

        self.rect = self.image.get_rect()

