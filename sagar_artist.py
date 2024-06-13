import pygame 

def sagar_artist(wallpaper_str, color):
    from pygame import mixer
    import spotify 
    import hadis_reckoning
    import game_theoryy
    import harvey_specter
    pygame.init()
    mixer.init()
    window = pygame.display.set_mode((1500, 1000 ))
    pygame.display.set_caption('Sagar')

    #--------------------------------------LOAD THE BACKGROUND
    bg = pygame.image.load("graphics/spotify/sagar_artist/sg.png")

    back = pygame.image.load("graphics/go back.png")
    back = pygame.transform.scale(back, (60, 60))
    #--------------------------------------
    hadi_reckon = pygame.image.load("graphics/spotify/sagar_artist/hadis_reckon.png")
    game_theory = pygame.image.load("graphics/spotify/sagar_artist/game_theory.png")
    harvey = pygame.image.load("graphics/spotify/sagar_artist/harvey.png")
    #--------------------------------------TOP SONGS   
    hadis_lament = pygame.image.load("graphics/spotify/sagar_artist/hadis_reckon/lament.png")
    bucket_clutch = pygame.image.load("graphics/spotify/sagar_artist/game_theory/bucket_clutch.png")
    aura = pygame.image.load("graphics/spotify/sagar_artist/hadis_reckon/aura.png")
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
                if (110 <= mousex <= 110 + hadi_reckon.get_width() and
                    450 <= mousey <= 450 + hadi_reckon.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    hadis_reckoning.hadis_reckoning(wallpaper_str, color)

                if (110 <= mousex <= 110 + game_theory.get_width() and
                    550 <= mousey <= 550 + game_theory.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    game_theoryy.game_theory_album(wallpaper_str, color)
                
                if (110 <= mousex <= 110 + harvey.get_width() and
                    650 <= mousey <= 650 + harvey.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    harvey_specter.harvey_reginald(wallpaper_str, color)
                #---------------------------------------------------------------------------------TOP SONGS
                if (890 <= mousex <= 890 + hadis_lament.get_width() and
                    450 <= mousey <= 450 + hadis_lament.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    mixer.music.load("graphics/spotify/sagar_artist/hadis_reckon/hadis_lament.mp3")
                    mixer.music.play()

                if (890 <= mousex <= 890 + bucket_clutch.get_width() and 
                    550 <= mousey <= 550 + bucket_clutch.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    mixer.music.load("graphics/spotify/sagar_artist/game_theory/bucket_clutch.MP3")
                    mixer.music.play()
                
                if (890 <= mousex <= 890 + aura.get_width() and
                    650 <= mousey <= 650 + aura.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    mixer.music.load("graphics/spotify/sagar_artist/hadis_reckon/aura.mp3")
                    mixer.music.play()
                #---------------------------------------------------------------------------------

                
        #--------------------------------------DISPLAY THE BACKGROUND
        window.blit(bg, (0,0))
        window.blit(back, (10, 10))

        window.blit(play,(750 - 100,900)) #PLAY BUTTON
        window.blit(pause,(750+ 100,900))
        #--------------------------------------DISPLAY ALBUMS
        window.blit(hadi_reckon, (110, 450))
        window.blit(game_theory, (110, 550))
        window.blit(harvey, (110, 650))
        #--------------------------------------DISPLAY TOP SONGS
        window.blit(hadis_lament, (890, 450))
        window.blit(bucket_clutch, (890, 550))
        window.blit(aura, (890, 650))
        #--------------------------------------
        pygame.display.flip()


color = (0, 0, 0)
#sagar_artist("graphics/WALLPAPERS/WP1.jpg", color)

