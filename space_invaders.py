import pygame
import random

def space_invade(wallpaper_str,color):
    pygame.init()
    from pygame import mixer 
    from time import sleep 
    import math  
    import sagar_explorer

    window = pygame.display.set_mode((1500, 1000))
    pygame.display.set_caption("Space Invaders")

    # Load the background
    back = pygame.image.load("graphics/space_invaders/space_back.jpg")
    back = pygame.transform.scale(back, (1500, 1000))
    back_music = mixer.music.load("graphics/space_invaders/background.wav")
    mixer.music.play(-1)

    go_back = pygame.image.load("graphics/go back.png")
    go_back = pygame.transform.scale(go_back,(60,60))

    # Load the player
    player = pygame.image.load("graphics/space_invaders/player_ship.png")
    player = pygame.transform.scale(player, (200, 200))
    playery = 800
    playerx = 650
    player_speed = 40
    left = False
    right = False

    # Load the player bullet
    player_bullet = pygame.image.load("graphics/space_invaders/player_bullet.png")
    player_bullet = pygame.transform.scale(player_bullet, (50, 50))
    player_bullet = pygame.transform.rotate(player_bullet, 90)
    player_bulletx = playerx
    player_bullety = playery
    b_stat = "ready"
    



    # Load the enemy
    enemy = pygame.image.load("graphics/space_invaders/enemy_ship.png")
    enemy = pygame.transform.scale(enemy, (100,100))
    

    enemy_speed = []
    enemyx = []
    enemyy = []
    amount_of_enemies = 6

    #text
    font = pygame.font.Font("freesansbold.ttf", 32)
    score = 0
    game_over = font.render("GAME OVER", True, (255,0, 0))

    for i in range (amount_of_enemies):
        enemyx.append(random.randint(0, 1350))
        enemyy.append(random.randint(0, 100))
        enemy_speed.append(random.randint(1, 10))
    enemy_direction = [1,1,1,1,1,1] 

    time = pygame.time.Clock()

    def draw_enemies():
        for i in range(len(enemyx)):
            window.blit(enemy, (enemyx[i], enemyy[i]))
            

    def move_enemies():
        for i in range(len(enemyx)):
            enemyx[i] += enemy_speed[i] * enemy_direction[i]
            if enemyx[i] <= 0 or enemyx[i] >= 1350:
                enemy_direction[i] *= -1
                enemyy[i] += 50

    def hit_bottom():
        for i in range (len(enemyx)):
            if 1000 < enemyy[i] < 1050:
                return True
            else:
                return False
            
    def hit_bullet(enemyX, enemyY, bulletX, bulletY):
        for i in range (len(enemyx)):
            if enemyy[i] <= bulletY <= enemyy[i] + 150 and enemyx[i] <= bulletX <= enemyx[i] + 150:
                return True
            else:
                return False

    while True:
        hit_bullet(enemyx[i], enemyy[i], player_bulletx, player_bullety)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_RIGHT:
                    right = True
                if event.key == pygame.K_SPACE and b_stat == "ready":
                    b_stat = "fire"
                    player_bulletx = playerx
                    player_bullety = playery
                    bullet_sound = mixer.Sound("graphics/space_invaders/laser.wav")
                    bullet_sound.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex,mousey = pygame.mouse.get_pos()
                if (10 <= mousex < 10 + back.get_width() and 
                        10 <= mousey < 10 + back.get_height()):
                            mixer.music.stop()
                            sagar_explorer.search_window(wallpaper_str,color)
                


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False

                    

        if left and playerx > 0:
            playerx -= player_speed
        if right and playerx < 1300:
            playerx += player_speed

        if b_stat == "fire":
            player_bullety -= 20
            pygame.display.flip()
            

        if player_bullety == 0:
            b_stat = "ready"
            player_bullety = 1500
        
        if hit_bullet(enemyx[i], enemyy[i], player_bulletx, player_bullety):
            score += 1
            enemyx[i] = random.randint(0, 1350)
            enemyy[i] = random.randint(0, 100)
            enemy_speed[i] = random.randint(1, 10)
            enemy_direction[i] = 1
            player_bullety = 1500
            mixer.Sound("graphics/space_invaders/explosion.wav").play()

        
        
        
        for i in range(len(enemyx)):
            if enemyy[i] > 1000:
                window.blit(game_over, (650, 500))
                pygame.display.flip()
                sleep(2)
                sagar_explorer.search_window(wallpaper_str,color)
                mixer.music.stop()

        
        
        

        window.blit(back, (0, 0))
        window.blit(player_bullet, (player_bulletx + 75, player_bullety))
        window.blit(player, (playerx, playery))
        score_display = font.render("Score: " + str(score), True, (255, 255, 255))
        window.blit(score_display, (1500 - score_display.get_width(), 10))
        window.blit(go_back, (10, 10))
        

        move_enemies()
        draw_enemies()
        hit_bottom()
        hit_bullet(enemyx[i], enemyy[i], player_bulletx, player_bullety)
       
        
        time.tick(120)

        
        


