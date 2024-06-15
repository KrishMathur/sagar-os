import pygame 

def srk_artist(wallpaper_str, color):
    from pygame import mixer
    import spotify 
    import srk_chennai
    import srk_zindagi
    import srk_tum_meri

    pygame.init()
    mixer.init()
    window = pygame.display.set_mode((1500, 1000 ))
    pygame.display.set_caption('Sagar')

    #--------------------------------------LOAD THE BACKGROUND
    bg = pygame.image.load("graphics/spotify/srk_artist/srk.png")

    back = pygame.image.load("graphics/go back.png")
    back = pygame.transform.scale(back, (60, 60))
    #--------------------------------------
    chennai = pygame.image.load("graphics/spotify/srk_artist/CHENNAI EXPRESS/11.png")
    zindagi = pygame.image.load("graphics/spotify/srk_artist/ZINDAGI/9.png")
    tum_meri = pygame.image.load("graphics/spotify/srk_artist/TUM MERI/10.png")
    #--------------------------------------TOP SONGS   
    kashmir = pygame.image.load("graphics/spotify/srk_artist/CHENNAI EXPRESS/44.png")
    dil = pygame.image.load("graphics/spotify/srk_artist/TUM MERI/42.png")
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
                if (110 <= mousex <= 110 + chennai.get_width() and
                    450 <= mousey <= 450 + chennai.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    srk_chennai.srk_chennai_album(wallpaper_str,color)
                if (110 <= mousex <= 110 + zindagi.get_width() and
                    550 <= mousey <= 550 + zindagi.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    srk_zindagi.srk_zindagi_album(wallpaper_str,color)
                    
                    
                
                if (110 <= mousex <= 110 + tum_meri.get_width() and
                    650 <= mousey <= 650 + tum_meri.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    srk_tum_meri.srk_tum_meri_album(wallpaper_str,color)
                 
                    
                #---------------------------------------------------------------------------------TOP SONGS
                if (890 <= mousex <= 890 + kashmir.get_width() and
                    450 <= mousey <= 450 + kashmir.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    

                if (890 <= mousex <= 890 + dil.get_width() and 
                    550 <= mousey <= 550 + dil.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    
                
                if (890 <= mousex <= 890 + manwa.get_width() and
                    650 <= mousey <= 650 + manwa.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    
                  
                #---------------------------------------------------------------------------------

                
        #--------------------------------------DISPLAY THE BACKGROUND
        window.blit(bg, (0,0))
        window.blit(back, (10, 10))

        window.blit(play,(750 - 100,900)) #PLAY BUTTON
        window.blit(pause,(750+ 100,900))
        #--------------------------------------DISPLAY ALBUMS
        window.blit(chennai, (110, 450))
        window.blit(zindagi, (110, 550))
        window.blit(tum_meri, (110, 650))
        #--------------------------------------DISPLAY TOP SONGS
        window.blit(kashmir, (890, 450))
        window.blit(dil, (890, 550))
        window.blit(manwa, (890, 650))
        #--------------------------------------
        pygame.display.flip()


color = (0, 0, 0)
#sagar_artist("graphics/WALLPAPERS/WP1.jpg", color)

