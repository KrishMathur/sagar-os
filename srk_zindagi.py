
import pygame
def srk_zindagi_album(wallpaper_str,color):
    from pygame import mixer
    import srk_artist
    pygame.init()
    mixer.init()
    window = pygame.display.set_mode((1500, 1000 ))
    pygame.display.set_caption('Sagar')

    #--------------------------------------LOAD THE BACKGROUND
    bg = pygame.image.load("graphics/spotify/srk_artist/ZINDAGI/zindagi.png")

    back = pygame.image.load("graphics/go back.png")
    back = pygame.transform.scale(back, (60, 60))
    #--------------------------------------
    #--------------------------------------load the songs
    kahoon = pygame.image.load("graphics/spotify/srk_artist/ZINDAGI/37.png")
    tumhi = pygame.image.load("graphics/spotify/srk_artist/ZINDAGI/38.png")
    manwa = pygame.image.load("graphics/spotify/srk_artist/ZINDAGI/39.png")
    #--------------------------------------
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
                mousex, mousey = pygame.mouse.get_pos()
                #-------------------------------------------PLAY AND PAUSE BUTTON
                if (750 - 100 <= mousex <= 750 - 100 + play.get_width() and  #PLAY BUTTON
                    900 <= mousey <= 900 + play.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    mixer.music.unpause()
                    
                if (750 + 100 <= mousex <= 750 + 100 + pause.get_width() and  #PAUSE BUTTON
                    900 <= mousey <= 900 + pause.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    mixer.music.pause()
                
                if (10 <= mousex < 10 + back.get_width() and  #GO BACK BUTTON
                    10 <= mousey < 10 + back.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    srk_artist.srk_artist (wallpaper_str,color)
                #------------------------------------------
                #--------------------------------------------------------------------------------------------------MUSIC BUTTONS
                if (750 - 200 <= mousex <= 750 - 200 + kahoon.get_width() and  
                    450 <= mousey <= 450 + kahoon.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    mixer.music.load("graphics/spotify/srk_artist/ZINDAGI/main agar kahooon.mp3")
                    mixer.music.play()
                    

                if (750 - 200 <= mousex <= 750 - 200 + tumhi.get_width() and  
                    550 <= mousey <= 550 + tumhi.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    mixer.music.load("graphics/spotify/srk_artist/ZINDAGI/tumhi_dekho.mp3")
                    mixer.music.play()
                   
              

                    print("PONDER BUTTON PRESSED")
                if (750 - 200 <= mousex <= 750 - 200 + manwa.get_width() and  
                    650 <= mousey <= 650 + manwa.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    mixer.music.load("graphics/spotify/srk_artist/ZINDAGI/manwa_lage.mp3")
                    mixer.music.play()
                    
                #--------------------------------------------------------------------------------------------------




        #--------------------------------------DISPLAY THE BACKGROUND
        window.blit(bg, (0,0))

        window.blit(play,(750 - 100,900))
        window.blit(pause,(750+ 100,900))

        window.blit(back, (10, 10))
        #--------------------------------------
        window.blit(kahoon, (750-200, 450))
        window.blit(tumhi, (750-200, 550))
        window.blit(manwa, (750-200, 650))
        #--------------------------------------
        pygame.display.flip()
