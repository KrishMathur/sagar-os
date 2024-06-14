import pygame

def harvey_reginald(wallpaper_str,color):
    from pygame import mixer
    import sagar_artist
    pygame.init()
    mixer.init()
    window = pygame.display.set_mode((1500, 1000 ))
    pygame.display.set_caption('Sagar')

    #--------------------------------------LOAD THE BACKGROUND
    bg = pygame.image.load("graphics/spotify/sagar_artist/harvey_specter/harvey.png")

    back = pygame.image.load("graphics/go back_black.png")
    back = pygame.transform.scale(back, (60, 60))
    #--------------------------------------
    #--------------------------------------load the songs
    hrs = pygame.image.load("graphics/spotify/sagar_artist/harvey_specter/HRS.png")
    life_is_like_this = pygame.image.load("graphics/spotify/sagar_artist/harvey_specter/life is like thi.png")
    ps = pygame.image.load("graphics/spotify/sagar_artist/harvey_specter/PS.png")
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
                if (750 - 200 <= mousex <= 750 - 200 + hrs.get_width() and  #greenback
                    450 <= mousey <= 450 + hrs.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    pygame.mixer.music.load("graphics/spotify/sagar_artist/harvey_specter/greenback.MP3")
                    pygame.mixer.music.play()
                    
                    

                if (750 - 200 <= mousex <= 750 - 200 + life_is_like_this.get_width() and  
                    550 <= mousey <= 550 + life_is_like_this.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    pygame.mixer.music.load("graphics/spotify/sagar_artist/harvey_specter/life.MP3")
                    pygame.mixer.music.play()
                    
                    
                if (750 - 200 <= mousex <= 750 - 200 + ps.get_width() and  # 
                    650 <= mousey <= 650 + ps.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    pygame.mixer.music.load("graphics/spotify/sagar_artist/harvey_specter/pearson.MP3")
                    pygame.mixer.music.play()
                    
                #--------------------------------------------------------------------------------------------------




        #--------------------------------------DISPLAY THE BACKGROUND
        window.blit(bg, (0,0))

        window.blit(play,(750 - 100,900))
        window.blit(pause,(750+ 100,900))

        window.blit(back, (10, 10))
        #--------------------------------------
        window.blit(hrs, (750-200, 450))
        window.blit(life_is_like_this, (750-200, 550))
        window.blit(ps, (750-200, 650))
        #--------------------------------------
        pygame.display.flip()


