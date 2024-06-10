import pygame 
from time import sleep 



def os_setting(wallpaper_str,color):

    import pc_about
    import homepage
    import turn_off
    import background_choose
    import task_color

    pygame.init()
    window = pygame.display.set_mode((1500, 1000 ))
    #----------------------------------------------------------------- LOADING BUTTON IMAGES
    on_off = pygame.image.load("graphics/SETTINGSAPP/POWER.png")
    about_pc = pygame.image.load("graphics/SETTINGSAPP/ABOUT PC.png")
    taskbar_color = pygame.image.load("graphics/SETTINGSAPP/TASKBAR_COLOR.png")
    wallpaperchooser = pygame.image.load("graphics/SETTINGSAPP/WALLPAPER.png")
    #-----------------------------------------------------------------
    pygame.display.set_caption('Settings')
    #-----------------------------------------------------------------
    settingsapp = pygame.image.load("graphics/SETTINGSAPP/SAGAR OS SETTINGS.png") #LOAD SETTINGS BACKROUND

    close_window = pygame.image.load("graphics/close_white.png") #LOAD CLOSE WINDOW BUTTON
    close_window = pygame.transform.scale(close_window,(50,50)) # SCALE IT SMALLER 
    #-----------------------------------------------------------------

    run = True
    while run:
        
        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == pygame.QUIT:
                            exit()

            mousex,mousey = pygame.mouse.get_pos() #GET MOUSE POSITION

            #-------------------------------------------------BLIT SETTINGS APP BG
            window.blit(settingsapp,(0,0))
            #-------------------------------------------------BLIT BUTTONS
            window.blit(on_off,(200,400))
            window.blit(taskbar_color,(1300 - taskbar_color.get_width(),400))
            window.blit(wallpaperchooser,(200,600))
            window.blit(about_pc, (1300 - about_pc.get_width(),600))

            window.blit(close_window,(1480 - close_window.get_width(),20))
            pygame.display.flip()
            #-------------------------------------------------
            if event.type == pygame.MOUSEBUTTONDOWN:

                if (1480 - close_window.get_width() <= mousex <= 1480 and  #CLOSE WINDOW BUTTON
                    20 <= mousey <= 20 + close_window.get_height()):
                    homepage.os_home(wallpaper_str,color)
                    

  
                if (200 <= mousex <= 200 + on_off.get_width() and  # POWER BUTTON CLICKED
                    400 <= mousey <= 400 + on_off.get_height()):
                    turn_off.close_os(wallpaper_str,color)


                if (1300 - taskbar_color.get_width() <= mousex <= 1300 and  #TASKBAR CLICKED 
                    400 <= mousey <= 400 + taskbar_color.get_height()):
                    task_color.task_colorr(wallpaper_str,color)

                if (200 <= mousex <= 200 + wallpaperchooser.get_width() and # WALLPAPER CLICKED
                    600 <= mousey <= 600 + wallpaperchooser.get_height()):
                    background_choose.bg_chooser( "graphics/WALLPAPERS/WP1.jpg",color)

            
                if (1300 - about_pc.get_width() <= mousex <= 1300 and # ABOUT PC CLICKED
                    600 <= mousey <= 600 + about_pc.get_height()):
                        pc_about.about_pc_window(wallpaper_str,color)

            


