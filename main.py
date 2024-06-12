import pygame
from moviepy.editor import VideoFileClip
from time import sleep
from pygame import mixer



pygame.init()
mixer.init()
info = pygame.display.Info() 
screen_width, screen_height = info.current_w, info.current_h
window = pygame.display.set_mode((1500, 1000 ))
pygame.display.set_caption('Sagar Os')

#-------------------------------------------------------- LOAD ON OFF PICTURES 
turn_on = pygame.image.load('graphics/open_sq/power on.png')
on  = pygame.image.load('graphics/open_sq/on 2.png')
#--------------------------------------------------------



run = True
sleep_state = "OFF"
while run:
    
    for event in pygame.event.get():

        pygame.display.flip()
        if event.type == pygame.QUIT:
                    exit()
        

        #----------------------------------------------CHECKS FOR MOUSE INPUT
        if event.type == pygame.MOUSEBUTTONDOWN:
                sleep_state = "ON"
        #-----------------------------------------------
        #----------------------------------------------- CHANGES ON OFF BUTTON BASED ON MOUSE INPUT AND GOES TO THE HOMEPAGE OF SAGAR OS
        if sleep_state == "OFF":
            window.blit(turn_on, (0,0))
            pygame.display.flip()
            
        
        if sleep_state == "ON":
              window.blit(on,(0,0))  
              pygame.display.flip()
              sleep(1)
              sleep_state = "LOADING"


        if sleep_state == "LOADING":
            loading_sagar_os = VideoFileClip('graphics/open_sq/SAGAR-OS_LOADSCRN.mp4')
            loading_sagar_os.preview()
            sleep_state = "RUNNING" 
            pygame.display.flip()
    
        if sleep_state == "RUNNING": 
            opensound = mixer.Sound('graphics/home_load.mp3')
            opensound.play()
            import homepage
            homepage.os_home()
            pygame.display.flip()
            run = False
         #-----------------------------------------------
        
        
        








