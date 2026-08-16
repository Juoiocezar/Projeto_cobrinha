import pygame

vel_x = 0
vel_y = 0




def movimento_cobra(mov_x, mov_y):
    global vel_x, vel_y

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_a]:
        vel_x = -10
        vel_y = 0
    if teclas[pygame.K_d]:
        vel_x = 10
        vel_y = 0
    if teclas[pygame.K_w]:
        vel_x = 0
        vel_y = -10
    if teclas[pygame.K_s]:
        vel_x = 0
        vel_y = 10

    mov_x = vel_x
    mov_y = vel_y

    
    

    return mov_x, mov_y

   
    
    

    

