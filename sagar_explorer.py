import pygame
from time import sleep

def search_window(wallpaper_str,color):
    import sys 
    import homepage
    import Eliott
    import youtube
    import pong_menu
    import searches
    global searchable

    from pygame import mixer


    pygame.init()
    window = pygame.display.set_mode((1500, 1000 ))
    pygame.display.set_caption('Sagar Explorer')


#--------------------------------------------------------------------------SETS THE FONT AND THEZ
    base_font = pygame.font.SysFont("Times New Roman", 32)
    search_text = ''

    cursor_visible = True
    cursor_flash_timer = 0
#---------------------------------------------------------------------------
    #---------------------------------
    browser_back = pygame.image.load("graphics/sagar_browser/browser_back_1.jpeg") #WALLPAPER
    browser_back = pygame.transform.scale(browser_back,(1500,1000))
    #---------------------------------
    close_window = pygame.image.load("graphics/close_white.png") #LOAD CLOSE WINDOW BUTTON
    close_window = pygame.transform.scale(close_window,(50,50)) # SCALE IT SMALLER 
    #---------------------------------
    browse_logo = pygame.image.load("graphics/sagar_browser/logo.png")
    #---------------------------------
    enter = pygame.image.load("graphics/sagar_browser/enter.png")
    enter = pygame.transform.scale(enter,(53,53))
    #---------------------------------
    acceptable_search = pygame.image.load("graphics/sagar_browser/Searches_list.png")
    #---------------------------------
    searchable = False
    #--------------------------------


    


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                            exit()
            #------------------------------------------------
            if searchable == True: #IF CLICKED ON SEARCH BAR 
                if event.type == pygame.KEYDOWN:
                        
                        #---------------------------------------------------------------#ENTER 
                        if event.key == pygame.K_RETURN:
                            if search_text == "ell" or search_text == "eliott" or search_text == "Eliott":
                                  Eliott.eliott(wallpaper_str,color)
                            if search_text == "TV" or search_text == "Gargtv" or search_text == "Youtube":
                                 youtube.youtube(wallpaper_str,color)
                            if search_text == "pong" or search_text == "Pong" or search_text == "Ping-Pong":
                                pygame.mixer.music.stop()
                                pong_menu.ping_pong_menu(wallpaper_str,color)
                        #-------------------------------------------------------------HANDLES THE INPUT FOR TYPING
                        if event.key == pygame.K_BACKSPACE:
                            search_text = search_text[:-1] #delete one from prhase
                        elif len(search_text) < 40 and event.key != pygame.K_RETURN:
                            search_text += event.unicode # ADD THE KEYSTROKES TO THE VARIBALE
                            #----------------------------------------------------------


            #--------------------------------------------------
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex,mousey = pygame.mouse.get_pos()

                if (1480 - close_window.get_width() <= mousex <= 1480 and  #CLOSE WINDOW BUTTON
                    20 <= mousey <= 20 + close_window.get_height()):
                    exit = mixer.Sound("graphics/exit.mp3")
                    exit.play()
                    homepage.os_home(wallpaper_str,color)
                
                if (760 - acceptable_search.get_width() / 2 <= mousex <= 760 + acceptable_search.get_width() / 2 and 
                    650 <= mousey <= 630 + acceptable_search.get_height()): #ACCEPTABLE SEARCHES
                    click = mixer.Sound("graphics/SETTINGSAPP/button_click.mp3")
                    click.play()
                    searches.searches(wallpaper_str, color)
                     

                if (460 <= mousex <= 460 + 560 and 
                    600 <= mousey <= 600 + 60):
                     searchable = True
                else:
                     searchable = False

                #---------------------------------------------------------------------------SEARCH ENTER BUTTON
                if (1020 <= mousex <= 1020 + enter.get_width() and 
                    600 <= mousey <= 600 + enter.get_height() and search_text == "ell" or search_text == "eliott" or search_text == "Eliott"):
                     Eliott.eliott(wallpaper_str,color)

                if (1020 <= mousex <= 1020 + enter.get_width() and 
                    600 <= mousey <= 600 + enter.get_height() and search_text == "TV" or search_text == "Gargtv" or search_text == "Youtube"):
                    youtube.youtube(wallpaper_str,color)
                
                if (1020 <= mousex <= 1020 + enter.get_width() and 
                    600 <= mousey <= 600 + enter.get_height() and search_text == "pong" or search_text == "Pong" or search_text == "Ping-Pong"):
                    pong_menu.ping_pong_menu(wallpaper_str,color)
                     
        
            #-----------------------------------------------------------------------------------

        if pygame.time.get_ticks() - cursor_flash_timer > 500:  # Flash the cursor every 500 milliseconds
            cursor_visible = not cursor_visible
            cursor_flash_timer = pygame.time.get_ticks()
        #------------------------------------------------------------------------      #MAKE THE SEARCH BAR

        search_rect_color = (135, 8, 18)
        search_bar = (460,600,560,60)
        pygame.draw.rect(window,search_rect_color,search_bar , border_radius=180)

        #----------------------------------------------------
        #---------------------------------------------------------------

        search_text_surface = base_font.render(search_text,True,(255,255,255))        #SHOW THE TEXT
        window.blit(search_text_surface,(480,610))

        #------------------------------------------------------

        search_here = "Search stuff here"                                                     #SHOW THE SEARCH BAR PLACEHOLDER
        search_here_surface = base_font.render(search_here,True,(192,192,192))
        if search_text == '':
            window.blit(search_here_surface,(480,610))

        #------------------------------------------------------

        sagar_browser = "SMART SAGAR BROSWER"
        sagar_browser_surface = base_font.render(sagar_browser,True,(255,255,255))

        window.blit(sagar_browser_surface,(550,550))

        #------------------------------------------------------

        window.blit(close_window,(1480 - close_window.get_width(),20)) #blit close window button
        window.blit(browse_logo,(500,10))                                #blit logo
        window.blit(enter,(1020,600))                                    #blit enter button
        window.blit(acceptable_search,(760 - acceptable_search.get_width() / 2, 650)) #accept search
        #-------------------------------------------------------
        if searchable == True:  #IF CLICKED ON SEARCH BAR SHOW CURSOR
            if cursor_visible: #IF CURSOR VISIBLE
                cursor_surface = base_font.render("|", True, (255, 255, 255))
                window.blit(cursor_surface, (480 + search_text_surface.get_width(), 610))

        pygame.display.flip()

        #-------------------------------------------------------
        window.blit(browser_back,(0,0))#BLIT THE BACKROUND
        #--------------------------------------------------------------------------
        

color = (194, 38, 45,0)
#search_window("graphics/WALLPAPERS/WP1.jpg",color)
