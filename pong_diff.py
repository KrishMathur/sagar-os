import pygame

def pong_diff_sel(wallpaper_str,color):
    import pong_menu
    
    import pong_easy
    import pong_med
    import pong_endless

    #------------------------------------
    bg = pygame.image.load("graphics/pong/PONG.png")
    back = pygame.image.load("graphics/go back.png")
    back = pygame.transform.scale(back,(60,60))
    #------------------------------------

    pygame.init()
    SCREENx , SCREENy = 1500,1000
    window = pygame.display.set_mode((SCREENx,SCREENy)) 
    pygame.display.set_caption('PONG DIFFICULTY')

    #------------------------------------FORMATTING
    WHITE = (255,255,255)
    font = pygame.font.SysFont("Times New Roman", 40)
    RED = (255, 0, 0)
    YELLOW = (255,255,0)
    #------------------------------------TEXT
    easy = "EASY"
    easy_text = font.render(str(easy),True,WHITE)
    easy_rect = easy_text.get_rect(topleft=(1000, 500))

    medium = "MEDIUM"
    medium_text = font.render(str(medium),True,WHITE)
    medium_rect = medium_text.get_rect(topleft=(1000, 600))

    hard = "ENDLESS"
    hard_text = font.render(str(hard),True,WHITE)
    hard_rect = hard_text.get_rect(topleft=(1000, 700))


    while True:
        mousex,mousey = pygame.mouse.get_pos()
        window.blit(bg,(0,0))

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                            exit()
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if (10 <= mousex < 10 + back.get_width() and 
                        10 <= mousey < 10 + back.get_height()):
                            pong_menu.ping_pong_menu(wallpaper_str,color)
                    
                    if (1000 <= mousex <= 1000 + easy_rect.width and #EASY RECT
                        500 <= mousey <= 500 + easy_rect.height):
                          pong_easy.ping_pong(wallpaper_str,color)
                    
                    if (1000 <= mousex <= 1000 + medium_rect.width and #mediun
                        600 <= mousey <= 600 + medium_rect.height):
                            pong_med.ping_pong_med(wallpaper_str,color)
                    
                    if (1000 <= mousex <= 1000 + hard_rect.width and    #hard
                        700 <= mousey <= 700 + hard_rect.height):
                          pong_endless.ping_pong_hard(wallpaper_str,color)







        #-----------------------------------------------------
        if (1000 <= mousex <= 1000 + easy_rect.width and #EASY RECT
            500 <= mousey <= 500 + easy_rect.height):
               pygame.draw.rect(window, YELLOW, easy_rect)
        else:
            pygame.draw.rect(window, RED, easy_rect)
        window.blit(easy_text,(1000,500))


        if (1000 <= mousex <= 1000 + medium_rect.width and #mediun
            600 <= mousey <= 600 + medium_rect.height):
            pygame.draw.rect(window, YELLOW, medium_rect)
        else:
            pygame.draw.rect(window, RED, medium_rect)
        window.blit(medium_text, (1000, 600))


        if (1000 <= mousex <= 1000 + hard_rect.width and    #hard
            700 <= mousey <= 700 + hard_rect.height):
            pygame.draw.rect(window, YELLOW, hard_rect)
        else:
            pygame.draw.rect(window, RED, hard_rect)
        window.blit(hard_text, (1000, 700))

        window.blit(back,(10,10))#blit the return button
        #-------------------------------------------------------
        pygame.display.flip()


