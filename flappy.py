import pygame
from pygame.locals import *
from bird import Bird, Base, Obstaculos, naTela, canosAleatorios

LARGURA = 500
ALTURA = 700
LARGURACHAO = 2 * LARGURA
ALTURACHAO = 100


pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))

BACKGROUND = pygame.image.load('background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND,(LARGURA, ALTURA))

grupoPassaro = pygame.sprite.Group()
passaro = Bird()
grupoPassaro.add(passaro)
grupoChao = pygame.sprite.Group()
for i in range(2):
    chao = Base(LARGURACHAO* i)
    grupoChao.add(chao)


grupoCano = pygame.sprite.Group()
for i in range(2):
    canos = canosAleatorios(LARGURA * i + 800)
    grupoCano.add(canos[0])
    grupoCano.add(canos[1])


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

    if naTela(grupoChao.sprites()[0]):
        grupoChao.remove(grupoChao.sprites()[0]) 
        novoChao = Base(LARGURACHAO - 20)
        grupoChao.add(novoChao)

    if naTela(grupoCano.sprites()[0]):
        grupoCano.remove(grupoCano.sprites()[0])
        grupoCano.remove(grupoCano.sprites()[0])     

        canos = canosAleatorios(LARGURA * 2)
        grupoCano.add(canos[0])
        grupoCano.add(canos[1])
       
    grupoPassaro.update()
    grupoChao.update()
    grupoCano.update()


    grupoPassaro.draw(tela)
    grupoCano.draw(tela)
    grupoChao.draw(tela)


    pygame.display.update()
    
    if pygame.sprite.groupcollide(grupoPassaro, grupoChao, False, False, pygame.sprite.collide_mask) or pygame.sprite.groupcollide(grupoPassaro, grupoCano, False, False, pygame.sprite.collide_mask):
        break

