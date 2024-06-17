"""
AUTHOR: Krish Mathur
DESCRIP: THIS IS AN MOCK UP OS CALLED SAGAR OS TO CARRY OUT FUNCTIONS LIKE SETTINGSS, MUSIC, SEARCH, AND GAMES
DATE: 10/10/2021
"""
import pygame 
from pygame import mixer
from time import sleep 




pygame.init()
mixer.init()
info = pygame.display.Info() 
screen_width, screen_height = info.current_w, info.current_h
window = pygame.display.set_mode((1500, 1000 ))
pygame.display.set_caption('Sagar Os')

#-------------------------------------------------------- LOAD ON OFF PICTURES 
turn_on = pygame.image.load('graphics/open_sq/power on.png')
on  = pygame.image.load('graphics/open_sq/on 2.png')
#--------------------------------------------------------RECT PROPETIRS 
rec_width = 0
#--------------------------------------------------------
sagar = pygame.image.load('graphics/open_sq/sagar.png')
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
            pygame.mixer.music.load('graphics/open_sq/loading_screen.MP3')
            pygame.mixer.music.play()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()

                if rec_width == 1400:
                    sleep_state = "RUNNING"
                    mixer.music.stop()
                    opensound = mixer.Sound('graphics/home_load.mp3')
                    opensound.play()
                    import homepage
                    
                    
                    

                rec_width += 10
                sleep(0.1)
                window.fill((0, 0, 0))
                pygame.draw.rect(window, (255, 255, 255), (50, 850, rec_width, 50))
                window.blit(sagar, (750 - sagar.get_width() // 2 , 300))
                pygame.display.flip()






