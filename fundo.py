import pygame
pygame.init()
from cobra import movimento_cobra


sizeX = 600
sizeY = 800
mov_x = 0
mov_y = 0
pos_inix = 120
pos_iniy = 120
angulo = 0


relogio = pygame.time.Clock()
FPS = 45

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

    mov_x, mov_y, angulo, cobra_rotacionada = movimento_cobra(mov_x, mov_y, angulo)
    
    pos_inix += mov_x
    pos_iniy += mov_y

    if pos_iniy < 0:
        pos_iniy = 600
    elif pos_iniy > 600:
        pos_iniy = 0
    if pos_inix < 0:
        pos_inix = 800
    elif pos_inix > 800:
        pos_inix = 0

    screen.blit(cobra_rotacionada, (pos_inix,pos_iniy))
    
        
    pygame.display.flip()

    relogio.tick(FPS)



pygame.quit()