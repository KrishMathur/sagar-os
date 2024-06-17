import pygame
from time import sleep

def task_colorr(wallpaper_str,color):

    import homepage
    import os_settings
    from pygame import mixer
    #----------------------------------------------LOAD WINDOW 
    pygame.init()
    mixer.init()
    window = pygame.display.set_mode((1500, 1000 ))
    #----------------------------------------------
    pygame.display.set_caption('Taskbar Color')
    #-------------------------------------------------------------------------------------------- #LOAD SETTINGS BG
    task_color_bg = pygame.image.load("graphics/taskbar_color_choose/SAGAR OS TASKBAR COLOR.png")   
    #--------------------------------------------------------------------------------------------

    #--------------------------------------------------COLORS


    yellow      = (181, 155, 59,255)
    green       = (53, 122, 56,255)
    red         = (255, 0, 0,255)
    transparent = (194, 38, 45,0)
    
    #--------------------------------------------------
    green_b = pygame.image.load("graphics/taskbar_color_choose/green.png")
    red_b = pygame.image.load("graphics/taskbar_color_choose/REd.png")
    yellow_b = pygame.image.load("graphics/taskbar_color_choose/yellow.png")
    transparent_b = pygame.image.load("graphics/taskbar_color_choose/transparent.png")

    close_window = pygame.image.load("graphics/close_white.png") #LOAD CLOSE WINDOW BUTTON
    close_window = pygame.transform.scale(close_window,(50,50)) # SCALE IT SMALLER 
    #--------------------------------------------------

    

    run = True
    while run:

        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == pygame.QUIT:
                            exit()
            mousex,mousey = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #--------------------------------------------------------------------------BUTTONS 
                if (400 <= mousex <= 400 + yellow_b.get_width() and       #YELLOW BUTTON      
                   400 <= mousey <= 400 + yellow_b.get_height()):
                   click = mixer.Sound("graphics/SETTINGSAPP/confirm.mp3")
                   click.play()
                   color = yellow
                   homepage.os_home(wallpaper_str,color)
                   


                if (900 <= mousex <= 900 + red_b.get_width() and #RED BUTTON
                    400 <= mousey <= 400 + red_b.get_height()):
                      click = mixer.Sound("graphics/SETTINGSAPP/confirm.mp3")
                      click.play()
                      color = red
                      homepage.os_home(wallpaper_str,color)
                
                if (400 <= mousex <= 400 + green_b.get_width()and #GREEN BUTTON
                    650 <= mousey <= 650 + green_b.get_height()):
                      click = mixer.Sound("graphics/SETTINGSAPP/confirm.mp3")
                      click.play()
                      color = green
                      homepage.os_home(wallpaper_str,color)
                
                if (900 <= mousex <= 900 + transparent_b.get_width() and       #TRANSPARENT BUTTON      
                   650 <= mousey <= 650 + transparent_b.get_height()):
                    click = mixer.Sound("graphics/SETTINGSAPP/confirm.mp3")
                    click.play()
                    color = transparent
                    homepage.os_home(wallpaper_str,color)
 
                if (1480 - close_window.get_width() <= mousex <= 1480 and  #CLOSE WINDOW BUTTON
                    20 <= mousey <= 20 + close_window.get_height()):
                    exit = mixer.Sound("graphics/exit.mp3")
                    exit.play()
                    os_settings.os_setting(wallpaper_str,color)

                #--------------------------------------------------------------------------
            #--------------------------------------------
            window.blit(task_color_bg,(0,0))
            #--------------------------------------------
            window.blit(yellow_b,(400,400))
            window.blit(red_b,(900,400))

            window.blit(green_b,(400,650))
            window.blit(transparent_b,(900,650))

            window.blit(close_window,(1480 - close_window.get_width(),20))
            #-------------------------------------------
            pygame.display.flip()





