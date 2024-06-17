import pygame
import random

def space_invade(wallpaper_str, color):
    pygame.init()
    from pygame import mixer 
    from time import sleep 
    import sagar_explorer

    window = pygame.display.set_mode((1500, 1000))
    pygame.display.set_caption("Space Invaders")

    # Load the background
    back = pygame.image.load("graphics/space_invaders/space_back.jpg")
    back = pygame.transform.scale(back, (1500, 1000))
    back_music = mixer.music.load("graphics/space_invaders/background.wav")
    mixer.music.play(-1)

    go_back = pygame.image.load("graphics/go back.png")
    go_back = pygame.transform.scale(go_back, (60, 60))

    # Load the player
    player = pygame.image.load("graphics/space_invaders/player_ship.png")
    player = pygame.transform.scale(player, (200, 200))
    playery = 800
    playerx = 650
    player_speed = 20
    left = False
    right = False

    # Load the player bullet
    player_bullet = pygame.image.load("graphics/space_invaders/player_bullet.png")
    player_bullet = pygame.transform.scale(player_bullet, (50, 50))
    player_bullet = pygame.transform.rotate(player_bullet, 90)
    player_bullet_rect = player_bullet.get_rect(center=(playerx + 100, playery))
    b_stat = "ready"

    # Load the enemy
    enemy = pygame.image.load("graphics/space_invaders/enemy_ship.png")
    enemy = pygame.transform.scale(enemy, (100, 100))

    enemy_rects = []
    enemy_speeds = []
    amount_of_enemies = 6

    # Text
    font = pygame.font.Font("freesansbold.ttf", 32)
    score = 0
    game_over = font.render("GAME OVER", True, (255, 0, 0))

    for i in range(amount_of_enemies):
        enemy_rect = enemy.get_rect()
        enemy_rect.x = random.randint(0, 1350)
        enemy_rect.y = random.randint(0, 100)
        enemy_rects.append(enemy_rect)
        enemy_speeds.append(random.randint(10, 40))
    enemy_directions = [1] * amount_of_enemies

    clock = pygame.time.Clock()

    def draw_enemies():
        for rect in enemy_rects:
            window.blit(enemy, rect.topleft)

    def move_enemies():
        for i, rect in enumerate(enemy_rects):
            rect.x += enemy_speeds[i] * enemy_directions[i]
            if rect.x <= 0 or rect.x >= 1350:
                enemy_directions[i] *= -1
                rect.y += 100

    def increase_enemy_speed():
        for i in range(amount_of_enemies):
            enemy_speeds[i] += 0.01

    def hit_bottom():
        for rect in enemy_rects:
            if 1000 < rect.y < 1050:
                return True
        return False

    def hit_bullet(bullet_rect):
        for rect in enemy_rects:
            if bullet_rect.colliderect(rect):
                return rect
        return None

    while True:
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
                    player_bullet_rect.center = (playerx + 100, playery)
                    bullet_sound = mixer.Sound("graphics/space_invaders/laser.wav")
                    bullet_sound.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if (10 <= mousex < 10 + go_back.get_width() and 
                        10 <= mousey < 10 + go_back.get_height()):
                    mixer.music.stop()
                    sagar_explorer.search_window(wallpaper_str, color)

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
            player_bullet_rect.y -= 20
            if player_bullet_rect.y <= 0:
                b_stat = "ready"
                player_bullet_rect.y = 1500

        hit_enemy = hit_bullet(player_bullet_rect)
        if hit_enemy:
            score += 1
            hit_enemy.x = random.randint(0, 1350)
            hit_enemy.y = random.randint(0, 100)
            index = enemy_rects.index(hit_enemy)
            enemy_speeds[index] = random.randint(10, 40)
            enemy_directions[index] = 1
            b_stat = "ready"
            player_bullet_rect.y = 1500
            mixer.Sound("graphics/space_invaders/explosion.wav").play()

        if hit_bottom():
            window.blit(game_over, (650, 500))
            pygame.display.flip()
            sleep(2)
            sagar_explorer.search_window(wallpaper_str, color)
            mixer.music.stop()

        window.blit(back, (0, 0))
        if b_stat == "fire":
            window.blit(player_bullet, player_bullet_rect.topleft)
        window.blit(player, (playerx, playery))
        score_display = font.render("Score: " + str(score), True, (255, 255, 255))
        window.blit(score_display, (1500 - score_display.get_width(), 10))
        window.blit(go_back, (10, 10))

        move_enemies()
        draw_enemies()
        increase_enemy_speed()

        pygame.display.flip()
        clock.tick(60)

