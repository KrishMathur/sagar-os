import pygame
def game_theory_album(wallpaper_str,color):
    from pygame import mixer
    import sagar_artist
    pygame.init()
    mixer.init()
    window = pygame.display.set_mode((1500, 1000 ))
    pygame.display.set_caption('Sagar')

    #--------------------------------------LOAD THE BACKGROUND
    bg = pygame.image.load("graphics/spotify/sagar_artist/game_theory/game_theory.png")

    back = pygame.image.load("graphics/go back.png")
    back = pygame.transform.scale(back, (60, 60))
    #--------------------------------------
    #--------------------------------------load the songs
    a_theory = pygame.image.load("graphics/spotify/sagar_artist/game_theory/a_theory.png")
    bucket_clutch = pygame.image.load("graphics/spotify/sagar_artist/game_theory/bucket_clutch.png")
    double_clutch = pygame.image.load("graphics/spotify/sagar_artist/game_theory/double_clutch.png")
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
                    sagar_artist.sagar_artist(wallpaper_str,color)
                #------------------------------------------
                #--------------------------------------------------------------------------------------------------MUSIC BUTTONS
                if (750 - 200 <= mousex <= 750 - 200 + a_theory.get_width() and  #A_THEORY BUTTON
                    450 <= mousey <= 450 + a_theory.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    mixer.music.load("graphics/spotify/sagar_artist/game_theory/a_theory.MP3")
                    mixer.music.play()
                    

                if (750 - 200 <= mousex <= 750 - 200 + bucket_clutch.get_width() and  #BUCKET_CLUTCH BUTTON
                    550 <= mousey <= 550 + bucket_clutch.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    mixer.music.load("graphics/spotify/sagar_artist/game_theory/bucket_clutch.MP3")
                    mixer.music.play()
                    
                if (750 - 200 <= mousex <= 750 - 200 + double_clutch.get_width() and  # 
                    650 <= mousey <= 650 + double_clutch.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    mixer.music.load("graphics/spotify/sagar_artist/game_theory/double_clutch.MP3")
                    mixer.music.play()
                #--------------------------------------------------------------------------------------------------




        #--------------------------------------DISPLAY THE BACKGROUND
        window.blit(bg, (0,0))

        window.blit(play,(750 - 100,900))
        window.blit(pause,(750+ 100,900))

        window.blit(back, (10, 10))
        #--------------------------------------
        window.blit(a_theory, (750-200, 450))
        window.blit(bucket_clutch, (750-200, 550))
        window.blit(double_clutch, (750-200, 650))
        #--------------------------------------
        pygame.display.flip()


