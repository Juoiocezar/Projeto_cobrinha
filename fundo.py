import pygame
from cobra import movimento_cobra
pygame.init()

sizeX = 600
sizeY = 800
mov_x = 0
mov_y = 0
pos_inix = 120
pos_iniy = 120


relogio = pygame.time.Clock()
FPS = 25

screen = pygame.display.set_mode((sizeY, sizeX))

fundo = pygame.image.load("imagens/fundo_grama/fundo.jpg").convert()
fundo_redimencionado = pygame.transform.scale(fundo, (sizeY, sizeX))

cobra = pygame.image.load("imagens/cobra/kbç_cobra.png").convert()
cobra_red = pygame.transform.scale(cobra,(50, 50))

pygame.display.set_caption("Cobrinha")



running = True 
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(fundo_redimencionado, (0, 0))

    mov_x, mov_y = movimento_cobra(mov_x, mov_y)
    pos_inix += mov_x
    pos_iniy += mov_y
    screen.blit(cobra_red, (pos_inix,pos_iniy))
    print(f"{mov_x}{mov_y}")
        
    pygame.display.flip()

    relogio.tick(FPS)


pygame.quit()