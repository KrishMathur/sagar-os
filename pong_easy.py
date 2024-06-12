import pygame
from pygame import mixer
from time import sleep
import pong_menu

def ping_pong(wallpaper_str, color):
    pygame.init()
    mixer.init()

    SCREENx, SCREENy = 1500, 1000
    window = pygame.display.set_mode((SCREENx, SCREENy)) 
    pygame.display.set_caption('PONG')

    back = pygame.image.load("graphics/go back.png")
    back = pygame.transform.scale(back, (60, 60))

    #-------------------------------------------------------- make game pieces 
    ball = pygame.Rect(SCREENx // 2 - 10, SCREENy // 2 - 10, 20, 20)
    player1 = pygame.Rect(40, SCREENy // 2 - 50, 10, 100)
    player2 = pygame.Rect(1460, SCREENy // 2 - 50, 10, 100)
    center_line = pygame.Rect(SCREENx // 2 - 1, 0, 2, SCREENy)
    #------------------------------------------------------
    ballspeedx, ballspeedy = 5, 5
    #------------------------------------------------------MOVEMENT VARIABLES 
    player2_up = False
    player2_down = False

    player1_up = False
    player1_down = False
    #------------------------------------------------------ SET COLORS 
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    #-------------------------------------------------------PLAYER SCORES
    player1_score = 0
    player2_score = 0

    font = pygame.font.Font(None, 74)
    #-------------------------------------------------------
    clock = pygame.time.Clock() #SET the framerate thing
    #-------------------------------------------------------MUSIC ON OFF 
    music_off = pygame.image.load("graphics/pong/music_off.png")
    music_toggle = True
    music_playing = False

    # Start music immediately
    pygame.mixer.music.load("graphics/pong/Game_music.MP3")
    pygame.mixer.music.play(-1)
    music_playing = True
    #-------------------------------------------------------

    clock = pygame.time.Clock()
    gamestart = mixer.Sound('graphics/pong/Gamestart.mp3')
    gamestart.play()
    run = True
    while run:
        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if (10 <= mousex < 10 + back.get_width() and 
                    10 <= mousey < 10 + back.get_height()):
                    pygame.mixer.music.pause()
                    music_playing = False 
                    pong_menu.ping_pong_menu(wallpaper_str, color)
                    

            #----------------------------------------MOVEMENT VARIABLES GO
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player2_up = True
                if event.key == pygame.K_DOWN:
                    player2_down = True

                if event.key == pygame.K_w:
                    player1_up = True
                if event.key == pygame.K_s:
                    player1_down = True
                #-------------------------------------------MUSIC 
                if event.key == pygame.K_m:
                    music_toggle = not music_toggle
                    if music_toggle and not music_playing:
                        pygame.mixer.music.unpause()
                        music_playing = True
                    elif not music_toggle and music_playing:
                        pygame.mixer.music.pause()
                        music_playing = False
            #--------------------------------------------MOVEMENT VARIABLES STOP
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player2_up = False
                if event.key == pygame.K_DOWN:
                    player2_down = False

                if event.key == pygame.K_w:
                    player1_up = False
                if event.key == pygame.K_s:
                    player1_down = False
              
            #--------------------------------------------
        #--------------------------PLAYER PADDLE MOVEMENT
        if player1_down:
            player1.y += 10
        if player1_up:
            player1.y -= 10

        if player2_down:
            player2.y += 10
        if player2_up:
            player2.y -= 10
        #--------------------------#out of bounds 
        if player1.top < 0:
            player1.top = 0
        if player1.bottom > 1000:
            player1.bottom = 1000
        if player2.top < 0:
            player2.top = 0
        if player2.bottom > 1000:
            player2.bottom = 1000

        if ball.top <= 0 or ball.bottom >= SCREENy:
            ballspeedy = -ballspeedy
        #---------------------------------------HIT SIDES AND UPDATE SCORE

        if ball.right >= 1500:  # player one score
            ballspeedx = -ballspeedx
            ball.x, ball.y = SCREENx // 2 - 10, SCREENy // 2 - 10
            player1_score += 1

        if ball.left <= 0:  # player 2 score 
            ballspeedx = -ballspeedx
            ball.x, ball.y = SCREENx // 2 - 10, SCREENy // 2 - 10
            player2_score += 1

        #--------------------------BALL HIT PADDLE
        if ball.colliderect(player1) or ball.colliderect(player2):
            ballspeedx = -ballspeedx 
            hit = mixer.Sound('graphics/pong/left.MP3')
            hit.play()
        #--------------------------BALL MOVEMENT 
        ball.x += ballspeedx
        ball.y += ballspeedy
        #--------------------------
        #------------------------------------------DRAW GAME STUFF
        window.fill(BLACK)#reset the screen

        pygame.draw.rect(window, WHITE, player1)
        pygame.draw.rect(window, WHITE, player2)
        pygame.draw.ellipse(window, WHITE, ball)
        pygame.draw.rect(window, WHITE, center_line)

        player1_text = font.render(str(player1_score), True, WHITE)
        window.blit(player1_text, (1500 // 4, 20))
        player2_text = font.render(str(player2_score), True, WHITE)
        window.blit(player2_text, (1500 * 3 // 4, 20))

        window.blit(back, (10, 10))#blit the return button

        if not music_playing: #IF THE MUOC IS PAYING OR NOT
            music_pic = pygame.image.load("graphics/pong/music_off.png")
            music_pic = pygame.transform.scale(music_pic, (20, 20))
            window.blit(music_pic, (1450, 20))
        pygame.display.flip()
        #--------------------------------------------
        clock.tick(120)

        #-----------------------------------------------WINNING
        gameover = mixer.Sound('graphics/pong/gameover.MP3')
        win_1 = pygame.image.load("graphics/pong/1.png") 
        win_2 = pygame.image.load("graphics/pong/2.png") 
        if player1_score == 10:
            pygame.mixer.music.pause()
            window.blit(win_1, (0, 0))
            gameover.play()
            pygame.display.flip()
            sleep(2)
            pong_menu.ping_pong_menu(wallpaper_str, color)

        if player2_score == 10:
            pygame.mixer.music.pause()
            window.blit(win_2, (0, 0))
            gameover.play()
            pygame.display.flip()
            sleep(2)
            pong_menu.ping_pong_menu(wallpaper_str, color)
            
