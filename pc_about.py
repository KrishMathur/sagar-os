import pygame




def about_pc_window(wallpaper_str,color):
    import os_settings
    from pygame import mixer

    pygame.init()
    window = pygame.display.set_mode((1500, 1000 ))

    pygame.display.set_caption('About PC')

    about_pc_pic = pygame.image.load("graphics/SETTINGSAPP/4.png")
    about_pc_pic = pygame.transform.scale(about_pc_pic,(1500,1000))

    close_window = pygame.image.load("graphics/close_white.png") #LOAD CLOSE WINDOW BUTTON
    close_window = pygame.transform.scale(close_window,(50,50)) # SCALE IT SMALLER 

    


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                            exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex,mousey = pygame.mouse.get_pos()
                if (1480 - close_window.get_width() <= mousex <= 1480 and  #CLOSE WINDOW BUTTON
                    20 <= mousey <= 20 + close_window.get_height()):
                    exit = mixer.Sound("graphics/exit.mp3")
                    exit.play()
                    os_settings.os_setting(wallpaper_str,color)

        window.blit(about_pc_pic,(-1,0))
        window.blit(close_window,(1480 - close_window.get_width(),20))
        pygame.display.flip()

