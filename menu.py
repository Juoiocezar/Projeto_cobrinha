import pygame
pygame.init()

size = width, height = 1080, 720

screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Cobrinha")

cobra = pygame.image.load("cobra.png").convert()
cobra_redimencionada = pygame.transform.scale(cobra, (100, 100))

running = True 

posicaoX = 360
posicaoY = 740

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    screen.blit(cobra_redimencionada, (posicaoX, posicaoY))

    if posicaoX == 720:
        posicaoX = 1
    else:
        posicaoX +=1

    if posicaoY == 1080:
            posicaoY = 1
    else:
        posicaoY +=1

    pygame.display.flip()


pygame.quit()
