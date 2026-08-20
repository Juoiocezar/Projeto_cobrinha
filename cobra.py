import pygame

vel_x = 0
vel_y = 0




def movimento_cobra(mov_x, mov_y, angulo):
    global vel_x, vel_y

    cobra = pygame.image.load("imagens/cobra/kbç_cobra.png").convert_alpha()
    cobra_red = pygame.transform.scale(cobra,(50, 50))
    cobra_rotacionada = pygame.transform.rotate(cobra_red, angulo)

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_a]:
        vel_x = -5
        vel_y = 0
        angulo = 90
        cobra_rotacionada = pygame.transform.rotate(cobra_red, angulo)
    if teclas[pygame.K_d]:
        vel_x = 5
        vel_y = 0
        angulo = -90
        cobra_rotacionada = pygame.transform.rotate(cobra_red, angulo)
    if teclas[pygame.K_w]:
        vel_x = 0
        vel_y = -5
        angulo = 0
        cobra_rotacionada = pygame.transform.rotate(cobra_red, angulo)
    if teclas[pygame.K_s]:
        vel_x = 0
        vel_y = 5
        angulo = 180
        cobra_rotacionada = pygame.transform.rotate(cobra_red, angulo)

    mov_x = vel_x
    mov_y = vel_y

    
    

    return mov_x, mov_y, angulo, cobra_rotacionada

   
    
    

    

