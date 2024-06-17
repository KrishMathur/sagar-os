import pygame
def srk_tum_meri_album(wallpaper_str,color):
    from pygame import mixer
    import srk_artist
    pygame.init()
    mixer.init()
    window = pygame.display.set_mode((1500, 1000 ))
    pygame.display.set_caption('Sagar')

    #--------------------------------------LOAD THE BACKGROUND
    bg = pygame.image.load("graphics/spotify/srk_artist/TUM MERI/1.png")

    back = pygame.image.load("graphics/go back.png")
    back = pygame.transform.scale(back, (60, 60))
    #--------------------------------------
    #--------------------------------------load the songs
    tumse = pygame.image.load("graphics/spotify/srk_artist/TUM MERI/40.png")
    rab_diktha = pygame.image.load("graphics/spotify/srk_artist/TUM MERI/41.png")
    paagal = pygame.image.load("graphics/spotify/srk_artist/TUM MERI/42.png")
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
                if (750 - 200 <= mousex <= 750 - 200 + tumse.get_width() and  #FEEL IT BUTTON
                    450 <= mousey <= 450 + tumse.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    mixer.music.load("graphics/spotify/srk_artist/TUM MERI/tumse.mp3")
                    mixer.music.play()

                if (750 - 200 <= mousex <= 750 - 200 + rab_diktha.get_width() and  #LIFE BUTTON
                    550 <= mousey <= 550 + rab_diktha.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    mixer.music.load("graphics/spotify/srk_artist/TUM MERI/diktha.mp3")
                    mixer.music.play()
                   
              

                    print("PONDER BUTTON PRESSED")
                if (750 - 200 <= mousex <= 750 - 200 + paagal.get_width() and  #LOSE BUTTON
                    650 <= mousey <= 650 + paagal.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    mixer.music.load("graphics/spotify/srk_artist/TUM MERI/pagal.mp3")
                    mixer.music.play()
                    
                #--------------------------------------------------------------------------------------------------




        #--------------------------------------DISPLAY THE BACKGROUND
        window.blit(bg, (0,0))

        window.blit(play,(750 - 100,900))
        window.blit(pause,(750+ 100,900))

        window.blit(back, (10, 10))
        #--------------------------------------
        window.blit(tumse, (750-200, 450))
        window.blit(rab_diktha, (750-200, 550))
        window.blit(paagal, (750-200, 650))
        #--------------------------------------
        pygame.display.flip()

