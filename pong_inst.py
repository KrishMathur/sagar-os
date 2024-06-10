import pygame 

def pong_inst(wallpaper_str,color):    
    import pong_menu
    bg = pygame.image.load("graphics/pong/PONG (1).png")

    back = pygame.image.load("graphics/go back.png")
    back = pygame.transform.scale(back,(60,60))

    pygame.init()
    window = pygame.display.set_mode((1500, 1000 ))
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                                exit()
                mousex,mousey = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (10 <= mousex < 10 + back.get_width() and 
                            10 <= mousey < 10 + back.get_height()):
                                pong_menu.ping_pong_menu(wallpaper_str,color)

        window.blit(bg,(0,0))
        window.blit(back,(10,10))#blit the return button
        pygame.display.flip()
