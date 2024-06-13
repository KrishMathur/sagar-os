import pygame 
from time import sleep 



def os_home(wallpaper_str,color):
    global run
    import turn_off
    import os_settings
    import sagar_explorer
    import spotify
    from pygame import mixer 

    import random
    from random import randint

    pygame.init()
    window = pygame.display.set_mode((1500, 1000 ))

    #--------------------------------------------------------  LAODING THE BACKROUND FOR THE OS
    wallpaper = pygame.image.load(wallpaper_str)
    wallpaper = pygame.transform.scale(wallpaper,(1500,1000))
    #--------------------------------------------------------
    pygame.display.set_caption('Homepage')

    #--------------------------------------------------------LOAD APP ICONS
    power    = pygame.image.load("graphics/APP ICONS/power.png")
    power    = pygame.transform.scale(power,(50,50))

    settings = pygame.image.load("graphics/APP ICONS/settings.png")
    settings = pygame.transform.scale(settings,(50,50))

    search   = pygame.image.load("graphics/APP ICONS/search.png")
    search   = pygame.transform.scale(search,(50,50))

    music = pygame.image.load("graphics/APP ICONS/music.png")
    music = pygame.transform.scale(music,(50,50))
    #-----------------------------------------------------------------------------------BATTERY LEVELS
    power_full = pygame.image.load("graphics/battery/battery_full.png")
    power_full   = pygame.transform.scale(power_full,(50,50))

    power_75 = pygame.image.load("graphics/battery/battery_75.png")
    power_75 = pygame.transform.scale(power_75,(50,50))

    power_50 = pygame.image.load("graphics/battery/battery_50.png")
    power_50 = pygame.transform.scale(power_50,(50,50))

    power_0 = pygame.image.load("graphics/battery/batery_0.png")
    power_0 = pygame.transform.scale(power_0,(50,50))

    battery_level = random.randint(1,4)
    #---------------------------------------------------------------------------------


    #--------------------------------------------------------LOADS THE TASK BAR COLOR
    taskbar_rect = pygame.Rect(20, 930, 1460, 40)

    taskbar_surface = pygame.Surface((taskbar_rect.width, taskbar_rect.height), pygame.SRCALPHA)
    taskbar_surface.fill(color)
    #--------------------------------------------------------

    run = True
    while run:
        
        
        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == pygame.QUIT:
                            exit()


            if event.type == pygame.MOUSEBUTTONDOWN : #DETECTS MOUSE PRESS
                mousex,mousey = pygame.mouse.get_pos()
               
                if (power_x <= mousex <= power_x+power.get_width() and #BUTTON DETECTION FOR POWER BUTTON
                    power_y <= mousey <= power_y + power.get_height()):
                      click = mixer.Sound("graphics/APP ICONS/home_click.mp3")
                      click.play()
                      turn_off.close_os(wallpaper_str,color)
                      run = False
                if (settings_x <= mousex <= settings_x + settings.get_width() and #BUTTON DETECTION FOR SETTINGS BUTTON
                    settings_y <= mousey <= settings_y + settings.get_height()):
                      click = mixer.Sound("graphics/APP ICONS/home_click.mp3")
                      click.play()
                      os_settings.os_setting(wallpaper_str,color)
                      run = False
                if (search_x <= mousex <= search_x + search.get_width() and #BUTTON DETECTION FOR SEARCH WINDOW
                    search_y <= mousey <= search_y + search.get_height()):
                      click = mixer.Sound("graphics/APP ICONS/home_click.mp3")
                      click.play()
                      sagar_explorer.search_window(wallpaper_str,color)
                if (music_x <= mousex <= music_x + music.get_width() and
                     music_y <= mousey <= music_y + music.get_height()): 
                          click = mixer.Sound("graphics/APP ICONS/home_click.mp3")
                          click.play()
                          spotify.spotify(wallpaper_str,color)
                
                      
                        
                

        window.blit(wallpaper,(0,0)) #BLITS THE BACKROUND

        window.blit(taskbar_surface, (taskbar_rect.x, taskbar_rect.y))#BLIT TASKBAR
        #-----------------------------------------------
        power_x = 1500 / 2 - power.get_width() / 2 #CALCUATE THE POSITIONS FOR THE POWER BUTTON
        power_y = 950 - power.get_height() / 2
        window.blit(power, (power_x, power_y))
        #------------------------------------------------
        settings_x = power_x - 50 - settings.get_width()  #CALC POSITIONS OF THE SETTINGS ICON
        settings_y = 950 - settings.get_height() / 2
        window.blit(settings,(settings_x,settings_y))
        #-------------------------------------------------
        search_x = power_x + 150 - search.get_width() #CALC BUTTONS FOR THE SEARCH ICON
        search_y = 950 - search.get_height() / 2
        window.blit(search,(search_x,search_y))
        #------------------------------------------------- 
        music_x = settings_x - 50 - music.get_width() #CALC BUTTONS FOR THE MUSIC ICON
        music_y = 950 - music.get_height() / 2
        window.blit(music,(music_x,music_y))
        #-------------------------------------------------


        if 1 == battery_level:
              window.blit(power_full,(1400,power_y))
        elif 2 == battery_level:
              window.blit(power_75,(1400,power_y))
        elif 3 == battery_level:
              window.blit(power_50,(1400,power_y))
        else:
              window.blit(power_0,(1400,power_y))
        #-------------------------------------------------
        pygame.display.flip() #UPDATE THE SCREEn
        #-----------------bju--------------------------------



color = (194, 38, 45,0)
os_home("graphics/WALLPAPERS/WP1.jpg",color)

