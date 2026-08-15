import pygame
pygame.init()

sizeX = 720
sizeY = 1080


relogio = pygame.time.Clock()
FPS = 30

screen = pygame.display.set_mode((sizeY, sizeX))

fundo = pygame.image.load("imagens/fundo_grama/fundo.jpg").convert()
fundo_redimencionado = pygame.transform.scale(fundo, (sizeY, sizeX))

pygame.display.set_caption("Cobrinha")



running = True 
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(fundo_redimencionado, (0, 0))
    pygame.display.flip()

    relogio.tick(FPS)


pygame.quit()