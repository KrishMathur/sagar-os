import pygame
import sys
def ping_pong_menu(wallpaper_str,color):
    from pygame import mixer
    pygame.init()
    mixer.init()
    SCREENx , SCREENy = 1500,1000
    window = pygame.display.set_mode((SCREENx,SCREENy)) 
    pygame.display.set_caption('PONG MENU')

    #-------------------------
    bg = pygame.image.load("graphics/pong/PONG.png")

    back = pygame.image.load("graphics/go back.png")
    back = pygame.transform.scale(back,(60,60))
    #-------------------------
    WHITE = (255,255,255)
    font = pygame.font.SysFont("Times New Roman", 40)
    RED = (255, 0, 0)
    YELLOW = (255,255,0)

    #-------------------------TEXT
    instructions = "INSTRUCTIONS"
    instructions_text = font.render(str(instructions),True,WHITE)
    instructions_rect = instructions_text.get_rect(topleft=(1000, 800))

    menu = "MENU"
    menu_text = font.render(str(menu),True,WHITE)
    menu_rect = menu_text.get_rect(topleft=(1000, 600))
    #-------------------------

    import pong_easy
    import sagar_explorer
    import pong_diff
    import pong_inst
  
    


    if not mixer.music.get_busy():
        menu_music = mixer.music.load("graphics/pong/menu_music.MP3")
        mixer.music.play(-1)

    run = True
    while run:

        mousex,mousey = pygame.mouse.get_pos()
        window.blit(bg,(0,0))

        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                            exit()
            
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if (10 <= mousex < 10 + back.get_width() and 
                        10 <= mousey < 10 + back.get_height()):
                            mixer.music.stop()
                            sagar_explorer.search_window(wallpaper_str,color)
             

                    if instructions_rect.collidepoint(pygame.mouse.get_pos()):
                        pong_inst.pong_inst(wallpaper_str,color)
   
                        
                        
                    if menu_rect.collidepoint(pygame.mouse.get_pos()):
                        pong_diff.pong_diff_sel(wallpaper_str,color)
       
        

        
        #--------------------------------------------------------------
        window.blit(bg,(0,0))
        if (1000 <= mousex <= 1000 + instructions_rect.width and
            800 <= mousey <= 800 + instructions_rect.height):
              pygame.draw.rect(window, YELLOW, instructions_rect)  #BLIT THE RED
              window.blit(instructions_text,(1000,800))
        else:
              pygame.draw.rect(window,RED, instructions_rect)  #BLIT THE RED
              window.blit(instructions_text,(1000,800))



        if (1000 <= mousex <= 1000 + menu_rect.width and
            600 <= mousey <= 600 + menu_rect.height):
              pygame.draw.rect(window, YELLOW, menu_rect)
              window.blit(menu_text,(1000,600))

        else:
            pygame.draw.rect(window,RED, menu_rect)
            window.blit(menu_text,(1000,600))
        
        window.blit(back,(10,10))#blit the return button
        
        #-----------------------------------------------------------------
        pygame.display.flip()


#color = (194, 38, 45,0)
#ping_pong_menu("graphics/WALLPAPERS/WP1.jpg",color)