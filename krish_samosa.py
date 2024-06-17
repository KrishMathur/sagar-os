import pygame
def krish_samosa_album(wallpaper_str,color):
    from pygame import mixer
    import krish_artist
    pygame.init()
    mixer.init()
    window = pygame.display.set_mode((1500, 1000 ))
    pygame.display.set_caption('Sagar')

    #--------------------------------------LOAD THE BACKGROUND
    bg = pygame.image.load("graphics/spotify/krish/SAMOSA/SAMOSA 2.png")

    back = pygame.image.load("graphics/go back.png")
    back = pygame.transform.scale(back, (60, 60))
    #--------------------------------------
    #--------------------------------------load the songs
    kesariya = pygame.image.load("graphics/spotify/krish/SAMOSA/34.png")
    jab_tak = pygame.image.load("graphics/spotify/krish/SAMOSA/35.png")
    badal = pygame.image.load("graphics/spotify/krish/SAMOSA/badal.png")
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
                    krish_artist.krish_artist (wallpaper_str,color)
                #------------------------------------------
                #--------------------------------------------------------------------------------------------------MUSIC BUTTONS
                if (750 - 200 <= mousex <= 750 - 200 + kesariya.get_width() and  #FEEL IT BUTTON
                    450 <= mousey <= 450 + kesariya.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    pygame.mixer_music.load("graphics/spotify/krish/SAMOSA/kesariya.MP3")
                    pygame.mixer_music.play()

                if (750 - 200 <= mousex <= 750 - 200 + jab_tak.get_width() and  #LIFE BUTTON
                    550 <= mousey <= 550 + jab_tak.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    pygame.mixer_music.load("graphics/spotify/krish/SAMOSA/jab_tak.MP3")
                    pygame.mixer_music.play()
              

                   
                if (750 - 200 <= mousex <= 750 - 200 + badal.get_width() and  #LOSE BUTTON
                    650 <= mousey <= 650 + badal.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    pygame.mixer_music.load("graphics/spotify/krish/SAMOSA/badal.MP3")
                    pygame.mixer_music.play()
                #--------------------------------------------------------------------------------------------------




        #--------------------------------------DISPLAY THE BACKGROUND
        window.blit(bg, (0,0))

        window.blit(play,(750 - 100,900))
        window.blit(pause,(750+ 100,900))

        window.blit(back, (10, 10))
        #--------------------------------------
        window.blit(kesariya, (750-200, 450))
        window.blit(jab_tak, (750-200, 550))
        window.blit(badal, (750-200, 650))
        #--------------------------------------
        pygame.display.flip()

