import pygame 

def sagar_artist(wallpaper_str, color):
    from pygame import mixer
    import spotify 
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
    #--------------------------------------

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                
                if (10 <= mousex < 10 + back.get_width() and 
                    10 <= mousey < 10 + back.get_height()):
                    click = mixer.Sound("graphics/spotify/button_click.mp3")
                    click.play()
                    spotify.spotify(wallpaper_str, color)
        
        #--------------------------------------DISPLAY THE BACKGROUND
        window.blit(bg, (0,0))
        window.blit(back, (10, 10))
        #--------------------------------------DISPLAY ALBUMS
        window.blit(hadi_reckon, (110, 450))
        window.blit(game_theory, (110, 550))
        window.blit(harvey, (110, 650))
        #--------------------------------------
        pygame.display.flip()


color = (0, 0, 0)
#sagar_artist("graphics/WALLPAPERS/WP1.jpg", color)