import pygame 
from time import sleep 


color = (100,100,100,255)
def bg_chooser(wallpaper_str,color):

    global wp1,wallpaper,run
    import os_settings
    import homepage

    pygame.init()
    window = pygame.display.set_mode((1500, 1000 )) 
    pygame.display.set_caption('Change Wallpaper')
    #-------------------------------------------------------------------LOAD APP BACKGORUND 
    wallpaper_bg = pygame.image.load('graphics/bg_choser/SAGAR OS WP_SET.png')
    #-------------------------------------------------------------------LOAD ALL THE BACKGROUNDS
    wp1 = pygame.image.load("graphics/WALLPAPERS/WP1.jpg")
    wp1_b = pygame.transform.scale(wp1,(300,200))
    

    wp2 = pygame.image.load("graphics/WALLPAPERS/WP2.jpg")
    wp2_b = pygame.transform.scale(wp2,(300,200))

    wp3 = pygame.image.load("graphics/WALLPAPERS/WP3.jpg")
    wp3_b = pygame.transform.scale(wp3,(300,200))

    wp4 = pygame.image.load("graphics/WALLPAPERS/WP4.jpg")
    wp4_b = pygame.transform.scale(wp4,(300,200))

    wp5 = pygame.image.load("graphics/WALLPAPERS/WP5.jpg")
    wp5_b = pygame.transform.scale(wp5,(300,200))

    wp6 = pygame.image.load("graphics/WALLPAPERS/wp6.jpg")
    wp6_b = pygame.transform.scale(wp6,(300,200))
    #-------------------------------------------------------------------#SET THE WALLPAPER VARIABLE
    wallpaper = wp1
    #-------------------------------------------------------------------
    close_window = pygame.image.load("graphics/close_white.png") #LOAD CLOSE WINDOW BUTTON
    close_window = pygame.transform.scale(close_window,(50,50)) # SCALE IT SMALLER 
    #-------------------------------------------------------------------

    run = True
    while run:
        wallpaper = wp1
        
        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == pygame.QUIT:
                            exit()

            mousex,mousey = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #---------------------------------------------------------------------------------------------------------------BUTON CLICKS FOR THE WALLLPAPER
                if 200 <= mousex <= 200 + wp1_b.get_width() and 400 <= mousey <= 400 + wp1_b.get_height():
                    wallpaper_str = "graphics/WALLPAPERS/WP1.jpg"
                    homepage.os_home(wallpaper_str,color)
                    
                    
                if 600 <= mousex <= 600 + wp2_b.get_width() and 400 <= mousey <= 400 + wp2_b.get_height():
                    wallpaper_str = "graphics/WALLPAPERS/WP2.jpg"
                    homepage.os_home(wallpaper_str,color)
                
                if 1000 <= mousex <= 1000 + wp3_b.get_width() and 400 <= mousey <= 400 + wp3_b.get_height():
                    wallpaper_str =  "graphics/WALLPAPERS/WP3.jpg"
                    homepage.os_home(wallpaper_str,color)
                
                if 200 <= mousex <= 200 + wp4_b.get_width() and 700 <= mousey <= 700 + wp4_b.get_height():
                    wallpaper_str =  "graphics/WALLPAPERS/WP4.jpg"
                    homepage.os_home(wallpaper_str,color)
                    
                if 600 <= mousex <= 600 + wp5_b.get_width() and 700 <= mousey <= 700 + wp5_b.get_height():
                    wallpaper_str =  "graphics/WALLPAPERS/WP5.jpg"
                    homepage.os_home(wallpaper_str,color)
                
                if 1000 <= mousex <= 1000 + wp6_b.get_width() and 700 <= mousey <= 700 + wp6_b.get_height():
                    wallpaper_str =  "graphics/WALLPAPERS/WP6.jpg"
                    homepage.os_home(wallpaper_str,color)
                #----------------------------------------------------------------------------------------------------------------#BUTTON CLICK FOR CLOSE WINDOW
                if (1480 - close_window.get_width() <= mousex <= 1480 and  #CLOSE WINDOW BUTTON
                    20 <= mousey <= 20 + close_window.get_height()):
                    os_settings.os_setting(wallpaper_str,color)
                #----------------------------------------------------------------------------------------------------------------    



            #------------------------------------------BLIT THE APP BACKGROUND
            window.blit(wallpaper_bg,(0,0))
            #------------------------------------------ BLIT BACKGROUNDS
            window.blit(wp1_b,(200,400))
            window.blit(wp2_b,(600,400))
            window.blit(wp3_b,(1000,400))

            window.blit(wp4_b,(200,700))
            window.blit(wp5_b,(600,700))
            window.blit(wp6_b,(1000,700))
            #------------------------------------------BLIT CLOSE WINDOW
            window.blit(close_window,(1480 - close_window.get_width(),20))
            #------------------------------------------
            pygame.display.flip()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     