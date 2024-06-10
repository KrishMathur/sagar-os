import pygame 

def searches(wallpaper_str,color):
    import sagar_explorer
    pygame.init()
    window = pygame.display.set_mode((1500, 1000 ))

    #----------------------------------------------images 
    bg = pygame.image.load("graphics/searches.png")
    back = pygame.image.load("graphics/go back.png")
    back = pygame.transform.scale(back,(60,60))
    #---------------------------------------------
    while True:
        mousex,mousey = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                            exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                   if (10 <= mousex < 10 + back.get_width() and 
                        10 <= mousey < 10 + back.get_height()):
                            sagar_explorer.search_window(wallpaper_str,color)
        window.blit(bg,(0,0))
        window.blit(back,(10,10))#blit the return button
        pygame.display.flip()
            