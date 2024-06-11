import pygame 

def spotify():
    from pygame import mixer 
    pygame.init()
    mixer.init()
    window = pygame.display.set_mode((1500, 1000 ))
    pygame.display.set_caption('Sagar Music')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                

        pygame.display.flip()