import pygame 

def spotify():
    from pygame import mixer 
    pygame.init()
    mixer.init()
    window = pygame.display.set_mode((1500, 1000 ))
    pygame.display.set_caption('Sagar Music')

    #----------------------LOAD THE BACKGROUND
    bg = pygame.image.load("graphics/spotify/bg.png")
    #----------------------LOAD ARTISTS 
    sagar = pygame.image.load("graphics/spotify/sagar.png")
    arijit = pygame.image.load("graphics/spotify/arijit.png")
    shah = pygame.image.load("graphics/spotify/shah.png")
    #----------------------LOAD ALBUMS
    hadi_reckon = pygame.image.load("graphics/spotify/HADI_album1.png")
    pyar_hai_meri_zindagi = pygame.image.load("graphics/spotify/shah_album1.png")
    chill_hits = pygame.image.load("graphics/spotify/arijit_album1.png")
    #----------------------CLOSE WINDOW BUTTON
    close_window = pygame.image.load("graphics/close_white.png") #LOAD CLOSE WINDOW BUTTON
    close_window = pygame.transform.scale(close_window,(50,50)) # SCALE IT SMALLER 
    #----------------------PLAY/PAUSE BUTTON
    play = pygame.image.load("graphics/spotify/play.png")
    play = pygame.transform.scale(play,(50,50))

    pause = pygame.image.load("graphics/spotify/pause.png")
    pause = pygame.transform.scale(pause,(50,50))
    #----------------------

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex,mousey = pygame.mouse.get_pos()
                if (1480 - close_window.get_width() <= mousex <= 1480 and  #CLOSE WINDOW BUTTON
                    20 <= mousey <= 20 + close_window.get_height()):
                    exit = mixer.Sound("graphics/exit.mp3")
                    exit.play()
                    print("EXITING")
                #--------------------------------------------------------------------------PLAY/PAUSE BUTTON
                if (750 - 100 <= mousex <= 750 - 100 + play.get_width() and  #PLAY BUTTON
                    900 <= mousey <= 900 + play.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    print("PLAYING")
                if (750 + 100 <= mousex <= 750 + 100 + pause.get_width() and  #PAUSE BUTTON
                    900 <= mousey <= 900 + pause.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    print("PAUSING")
                #--------------------------------------------------------------------------ARTISTS
                if (180 <= mousex <= 180 + sagar.get_width() and  #SAGAR ARTIST
                    500 <= mousey <= 500 + sagar.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    print("SAGAR")
                if (180 <= mousex <= 180 + arijit.get_width() and  #ARIJIT ARTIST
                    600 <= mousey <= 600 + arijit.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    print("ARIJIT")
                if (180 <= mousex <= 180 + shah.get_width() and  #SHAH ARTIST
                    700 <= mousey <= 700 + shah.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    print("SHAH")
                #--------------------------------------------------------------------------ALBUMS
                if (960 <= mousex <= 960 + hadi_reckon.get_width() and  #HADI RECKON ALBUM
                    500 <= mousey <= 500 + hadi_reckon.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    print("HADI RECKON")
                if (960 <= mousex <= 960 + pyar_hai_meri_zindagi.get_width() and  #SHAH ALBUM
                    600 <= mousey <= 600 + pyar_hai_meri_zindagi.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    print("SHAH ALBUM")
                if (960 <= mousex <= 960 + chill_hits.get_width() and  #ARIJIT ALBUM
                    700 <= mousey <= 700 + chill_hits.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    print("ARIJIT ALBUM")
                #-------------------------------------------------------------------------------
        
        #--------------------------------------------------------------------------------------blit everything
        window.blit(bg,(0,0))
        #----------------------------------------- ARTISTS
        window.blit(sagar,(180,500)) #sagar the artist
        window.blit(arijit,(180,600)) #arijit the artist
        window.blit(shah,(180,700)) #shah the artist
        #-----------------------------------------ALBUMS
        window.blit(hadi_reckon,(960,500)) #HADI RECKON ALBUM
        window.blit(pyar_hai_meri_zindagi,(960,600)) #SHAH ALBUM
        window.blit(chill_hits,(960,700)) #ARIJIT ALBUM
        #-----------------------------------------
        window.blit(close_window,(1480 - close_window.get_width(),20))#CLOSE BUTTON
        #---------------------BLIT THE PLAY/PAUSE BUTTONS
        window.blit(play,(750 - 100,900))
        window.blit(pause,(750+ 100,900))
        #---------------------------------------------------------------------------------------------

        pygame.display.flip()

spotify()