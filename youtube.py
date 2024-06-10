import pygame


def youtube(wallpaper_str,color):
    import sagar_explorer

    #-------------------------------------------------
    back = pygame.image.load("graphics/go back.png")
    back = pygame.transform.scale(back,(60,60))
    #-----------------------------------------------

    pygame.init()
    info = pygame.display.Info() 
    window = pygame.display.set_mode((1500, 1000 ))
    pygame.display.set_caption('Garg Tv')

    youtube_bg = pygame.image.load ("graphics/sagar tv/Game On.png")

    run = True
    while run:


        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                                exit()
                    
                mousex,mousey = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if (10 <= mousex < 10 + back.get_width() and 
                            10 <= mousey < 10 + back.get_height()):
                                sagar_explorer.search_window(wallpaper_str,color)

        #-----------------------------------blit app bg                       
        window.blit(youtube_bg,(0,0))
        #------------------------------------- Blit return button
        window.blit(back,(10,10))
        #----------------------------------- #update
        pygame.display.flip()
        #---------------------------------
        
