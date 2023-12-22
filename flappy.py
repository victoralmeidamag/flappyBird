import pygame
from pygame.locals import *
from bird import Bird

LARGURA = 500
ALTURA = 700


pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))

BACKGROUND = pygame.image.load('background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND,(LARGURA, ALTURA))

grupoPassaro = pygame.sprite.Group()
passaro = Bird()
grupoPassaro.add(passaro)

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
        if evento.type == KEYDOWN:
            if evento.key == K_SPACE:
                passaro.saltar()
    tela.blit(BACKGROUND, (0, 0))
    grupoPassaro.update()
    grupoPassaro.draw(tela)  
    pygame.display.update()

