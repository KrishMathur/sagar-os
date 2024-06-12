import pygame 

def sagar_artist():
    from pygame import mixer 
    pygame.init()
    mixer.init()
    window = pygame.display.set_mode((1500, 1000 ))
    pygame.display.set_caption('Sagar')

    #--------------------------------------LOAD THE BACKGROUND
    bg = pygame.image.load("graphics/spotify/sagar_artist/sg.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        #--------------------------------------DISPLAY THE BACKGROUND
        window.blit(bg, (0,0))
        #--------------------------------------
        pygame.display.flip()
sagar_artist()