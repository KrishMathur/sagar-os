import pygame 

def krish_artist(wallpaper_str, color):
    from pygame import mixer
    import spotify 

    pygame.init()
    mixer.init()
    window = pygame.display.set_mode((1500, 1000 ))
    pygame.display.set_caption('Sagar')

    #--------------------------------------LOAD THE BACKGROUND
    bg = pygame.image.load("graphics/spotify/krish/krish_bg.png")

    back = pygame.image.load("graphics/go back.png")
    back = pygame.transform.scale(back, (60, 60))
    #--------------------------------------
    chill = pygame.image.load("graphics/spotify/krish/CHILL.png")
    money = pygame.image.load("graphics/spotify/krish/MONEY.png")
    samosa = pygame.image.load("graphics/spotify/krish/SAMOSA.png")
    #--------------------------------------TOP SONGS   
    lose_control = pygame.image.load("graphics/spotify/krish/CHILL/LOSE CONTRL.png")
    tom_ford = pygame.image.load("graphics/spotify/krish/MONEY/TOO SWEET.png")
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
                #--------------------------------------------------------------------play and pause button
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
                #--------------------------------------------------------------------GO BACK BUTTON
                if (10 <= mousex < 10 + back.get_width() and 
                    10 <= mousey < 10 + back.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    spotify.spotify(wallpaper_str, color)
                #----------------------------------------------------------------------------------ALBUMS
                if (110 <= mousex <= 110 + chill.get_width() and
                    450 <= mousey <= 450 + chill.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    

                if (110 <= mousex <= 110 + money.get_width() and
                    550 <= mousey <= 550 + money.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    
                
                if (110 <= mousex <= 110 + samosa.get_width() and
                    650 <= mousey <= 650 + samosa.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    
                #---------------------------------------------------------------------------------TOP SONGS
                if (890 <= mousex <= 890 + lose_control.get_width() and
                    450 <= mousey <= 450 + lose_control.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                   

                if (890 <= mousex <= 890 + tom_ford.get_width() and 
                    550 <= mousey <= 550 + tom_ford.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    
                
                if (890 <= mousex <= 890 + badal.get_width() and
                    650 <= mousey <= 650 + badal.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                  
                #---------------------------------------------------------------------------------

                
        #--------------------------------------DISPLAY THE BACKGROUND
        window.blit(bg, (0,0))
        window.blit(back, (10, 10))

        window.blit(play,(750 - 100,900)) #PLAY BUTTON
        window.blit(pause,(750+ 100,900))
        #--------------------------------------DISPLAY ALBUMS
        window.blit(chill, (110, 450))
        window.blit(money, (110, 550))
        window.blit(samosa, (110, 650))
        #--------------------------------------DISPLAY TOP SONGS
        window.blit(lose_control, (890, 450))
        window.blit(tom_ford, (890, 550))
        window.blit(badal, (890, 650))
        #--------------------------------------
        pygame.display.flip()


color = (0, 0, 0)
#sagar_artist("graphics/WALLPAPERS/WP1.jpg", color)

