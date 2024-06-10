import pygame

#------------------------------------------------
ell = pygame.image.load("graphics/elloit.png")
ell = pygame.transform.scale(ell,(1000,1000))
#-------------------------------------------------
back = pygame.image.load("graphics/go back.png")
back = pygame.transform.scale(back,(60,60))
#-----------------------------------------------


pygame.init()
info = pygame.display.Info() 
screen_width, screen_height = info.current_w, info.current_h
window = pygame.display.set_mode((1500, 1000 ))
pygame.display.set_caption('Eliott')

def eliott(wallpaper_str,color):
    import sagar_explorer
    while True: 

        for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                                exit()
                    
                mousex,mousey = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if (10 <= mousex < 10 + back.get_width() and 
                            10 <= mousey < 10 + back.get_height()):
                                sagar_explorer.search_window(wallpaper_str,color)
                                
                        


        window.fill((0,0,1))
        window.blit(ell,(0,0))

        window.blit(back,(10,10))
        pygame.display.flip()

