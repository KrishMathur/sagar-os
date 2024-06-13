import pygame
from time import sleep



def close_os(wallpaper_str,color):
    import homepage
    from pygame import mixer    
    import os_settings
    import sys 

    pygame.init()
    info = pygame.display.Info() 
    window = pygame.display.set_mode((1500, 1000 ))

    pygame.display.set_caption('Power OFF')

    close_window = pygame.image.load("graphics/close_white.png") #LOAD CLOSE WINDOW BUTTON
    close_window = pygame.transform.scale(close_window,(50,50)) # SCALE IT SMALLER 

    off = pygame.image.load("graphics/close_sq/off.png")
    on = pygame.image.load("graphics/close_sq/power off.png")
    sleep_state = "ON"




    run = True
    while run:
        
        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == pygame.QUIT:
                            exit()
            
            mousex,mousey = pygame.mouse.get_pos() #GET MOUSE POSITION


            window.blit(on,(0,0)) #LOADS ON SCREEn
            window.blit(close_window,(1480 - close_window.get_width(),20)) #LOADS CLOSE BUTTON
            pygame.display.flip()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                sleep_state = "OFF"
                   
                if (1480 - close_window.get_width() <= mousex <= 1480 and 
                20 <= mousey <= 20 + close_window.get_height()):
                    exit = mixer.Sound("graphics/exit.mp3")
                    exit.play()
                    os_settings.os_setting(wallpaper_str,color)
                    break
                    
            
            if sleep_state == "OFF":
                  window.blit(off,(0,0))
                  pygame.display.flip()
                  sleep(1)
                  sys.exit()
