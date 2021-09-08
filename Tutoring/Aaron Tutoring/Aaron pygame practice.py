import pygame
import random
import os
import math
import time
pygame.font.init()

WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))

clock = pygame.time.Clock()

YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

WINNER_FONT = pygame.font.SysFont('comicsans', 40, bold=False, italic=False)
LEVEL_FONT = pygame.font.SysFont('comicsans', 40, bold=False, italic=False)
HEALTH_FONT = pygame.font.SysFont('comicsans', 20)
SCORE_FONT = pygame.font.SysFont('comicsans', 20)

player = pygame.Rect((100, 100, 20, 20))

PLAYER_SPRITE = pygame.image.load('player.png')
PLAYER_POSITION = [player.x, player.y]


sand = pygame.Rect((100, 100, WIDTH - 200, WIDTH - 200))
water = pygame.Rect((200, 200, WIDTH - 400, WIDTH - 400))
door = pygame.Rect(WIDTH // 2 - 50, 0, 100, 100)

PORTAL_IMAGE = pygame.image.load('portal.png')
PORTAL1 = pygame.transform.scale(PORTAL_IMAGE, (100, 100))
PORTAL2 = pygame.transform.scale(PORTAL_IMAGE, (100, 100))

DOOR_IMAGE = pygame.image.load("Door.png")
DOOR = pygame.transform.scale(DOOR_IMAGE, (50, 50))
DOOR_LOCATION = [WIDTH // 2 - 25 // 2, 0]
door = pygame.Rect(WIDTH // 2 - 25 // 2, 0, 50, 50)

def generate_obstacles(n, health):
    obstacles = []
    for i in range(n):
        obstacles.append([pygame.Rect(random.randrange(20, WIDTH - 20), random.randrange(20, WIDTH - 20), 20, 20), health])
    return obstacles

def generate_bullet(obj, pos, vel):
    obj_x = obj.x + obj.width / 2
    obj_y = obj.y + obj.height / 2
    bullet_x = pos[0]
    bullet_y = pos[1]
    x = bullet_x - obj_x
    y = bullet_y - obj_y

    if x != 0 and y != 0:
        k = math.atan2(y, x)
        xvel = int(math.cos(k) * vel)
        yvel = int(math.sin(k) * vel)
    elif x == 0:
        xvel = vel
        yvel = 0
    else:
        xvel = 0
        yvel = vel


    bullet = pygame.Rect(obj_x - 5, obj_y - 5, 10, 10)

    return [bullet, xvel, yvel]

def generate_bullets_boi(obj, pos, vel):
    obj_x = obj.x + obj.width / 2
    obj_y = obj.y + obj.height / 2
    bullet_x = pos[0]
    bullet_y = pos[1]
    x = bullet_x - obj_x
    y = bullet_y - obj_y

    if abs(x) >= abs(y) and x >= 0:
        xvel = vel
        yvel = 0
    elif abs(y) >= abs(x) and y >= 0:
        xvel = 0
        yvel = vel
    elif abs(x) >= abs(y) and x <= 0:
        xvel = -vel
        yvel = 0
    elif abs(y) >= abs(x) and y <= 0:
        xvel = 0
        yvel = -vel
    
    bullet = pygame.Rect(obj_x - 5, obj_y - 5, 10, 10)

    return [bullet, xvel, yvel]


def move_obstacles(obstacles, vel, obj):
    for obstacle in obstacles:
        if obstacle[0].x - obj.x > 0:
            obstacle[0].x -= vel
        elif obstacle[0].x - obj.x < 0:
            obstacle[0].x += vel
        
        if obstacle[0].y - obj.y > 0:
            obstacle[0].y -= vel
        elif obstacle[0].y - obj.y < 0:
            obstacle[0].y += vel
        
        if obstacle[0].y > WIDTH:
            obstacle[0].y = 0
            obstacle[0].x = random.randrange(20, WIDTH - 20)

def move_bullets(bullets, homing_bullets, obstacles, vel):
    if not homing_bullets:
        for bullet in bullets:
            bullet[0].x += bullet[1]
            bullet[0].y += bullet[2]
    else:
        if len(obstacles):
            min = 100000
            for bullet in bullets:
                for obstacle in obstacles:
                    dx = bullet[0].x + bullet[0].width // 2 - (obstacle[0].x + obstacle[0].width)
                    dy = bullet[0].y + bullet[0].height - (obstacle[0].y + obstacle[0].height)
                    h = math.sqrt(dx ** 2 + dy ** 2)
                    if h < min:
                        min = h
                        x = dx
                        y = dy
                angle = math.atan2(y, x)
                xvel = math.cos(angle) * -vel
                yvel = math.sin(angle) * -vel
                bullet[0].x += xvel
                bullet[0].y += yvel
        else:
            for bullet in bullets:
                bullet[0].x += bullet[1]
                bullet[0].y += bullet[2]


def move_random(rect):
    rect.x, rect.y = random.randrange(20, WIDTH - 20), random.randrange(20, WIDTH - 20)

def update_pos(obj, keys_pressed, vel):
    if keys_pressed[pygame.K_w] and not obj.y - vel < 0:
        obj.y -= vel
    if keys_pressed[pygame.K_a] and not obj.x - vel < 0:
        obj.x -= vel
    if keys_pressed[pygame.K_s] and not obj.y + vel > WIDTH - obj.height:
        obj.y += vel
    if keys_pressed[pygame.K_d] and not obj.x + vel > WIDTH - obj.width:
        obj.x += vel

def draw_win(text):
    draw_text = WINNER_FONT.render(text, 1, (0, 255, 0))
    WIN.blit(draw_text, (WIDTH // 2 - draw_text.get_width() // 2, WIDTH // 2 - draw_text.get_height() // 2))

    pygame.display.update()
    pygame.time.delay(2000)

def draw_health(text):
   draw_text = HEALTH_FONT.render(text, 1, (0, 0, 0))
   WIN.blit(draw_text, (10, 10))

def draw_score(text):
    draw_text = SCORE_FONT.render(text, 1, (0, 0, 0))
    WIN.blit(draw_text, (WIDTH - draw_text.get_width() - 10, 10))


def draw(win, obstacles, goal, health, extra_health, show_health, bullets, score, powerup, PLAYER):
    pygame.draw.rect(win, (122, 144, 0), powerup)
    PLAYER_POSITION = [player.x, player.y]
    WIN.blit(PLAYER, PLAYER_POSITION)
    for obstacle in obstacles:
        pygame.draw.rect(win, (0, 255, 0), obstacle[0])
    for bullet in bullets:
        pygame.draw.rect(win, (100, 100, 0), bullet[0])
    pygame.draw.rect(win, (255, 0, 0), goal)
    if show_health:
        pygame.draw.rect(win, (0, 255, 255), extra_health)
    draw_health("Health: {}".format(health))
    draw_score("Score: {}".format(score))
    win.blit(DOOR, DOOR_LOCATION)
    pygame.display.update()

# sky_img = pygame.transform.scale(pygame.image.load(""), (WIDTH, HEIGHT))

def draw_room1(win):
    win.blit(PORTAL1, (0, WIDTH // 2 - 50))
    win.blit(PORTAL2, (WIDTH - 100, WIDTH // 2 - 50))
    pygame.draw.rect(win, YELLOW, sand)
    pygame.draw.rect(win, BLUE, water)

def draw_room2(win):
    pass

def main():
    PLAYER_FACING_CURRENT = 1
    PLAYER_FACING_NEW = 1
    PLAYER = pygame.transform.scale(PLAYER_SPRITE, (20, 20))
    VEL = 10
    OBS_VEL = 3
    HEALTH = 3
    SCORE = 0
    TIME = 0
    LEVEL = 1
    LEVEL_SCORE = 5
    ENEMY_TIMER = 4
    ENEMY_HEALTH = 1
    LOCATION = "Room 1"
    MOVE_ROOM = True
    bullets = []
    show_health = True
    teleport = True
    portal1 = pygame.Rect(0, WIDTH // 2 - 50, 100, 100)
    portal2 = pygame.Rect(WIDTH - 100, WIDTH // 2 - 50, 100, 100)
    homing_bullets = False


    goal = pygame.Rect((WIDTH - 20, WIDTH // 2 - 10, 20, 20))
    extra_health = pygame.Rect((WIDTH - 20, 0, 20, 20))
    powerup = pygame.Rect(random.randrange(0, WIDTH - 20), random.randrange(0, WIDTH - 20), 20, 20)

    obstacles = generate_obstacles(3, ENEMY_HEALTH)

    run = True

    while run:
        WIN.fill((255, 255, 255))
        clock.tick(60)

        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                bullets.append(generate_bullets_boi(player, pygame.mouse.get_pos(), 20))
            
              
            obj_x = player.x + player.width / 2
            obj_y = player.y + player.height / 2
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]
            x = mouse_x - obj_x
            y = mouse_y - obj_y
            if abs(x) >= abs(y) and x >= 0:
                PLAYER_FACING_NEW = 2
            elif abs(y) >= abs(x) and y >= 0:
                PLAYER_FACING_NEW = 3
            elif abs(x) >= abs(y) and x <= 0:
                PLAYER_FACING_NEW = 4
            elif abs(y) >= abs(x) and y <= 0:
                PLAYER_FACING_NEW = 1
            PLAYER = pygame.transform.rotate(PLAYER, 90 * (PLAYER_FACING_CURRENT - PLAYER_FACING_NEW))
            PLAYER_FACING_CURRENT = PLAYER_FACING_NEW

        move_obstacles(obstacles, OBS_VEL, player)
        move_bullets(bullets, homing_bullets, obstacles, 20)
        for bullet in bullets:
            if bullet[0].x > WIDTH - bullet[0].width or bullet[0].x < 0:
                bullets.remove(bullet)
            elif bullet[0].y > WIDTH - bullet[0].height or bullet[0].y < 0:
                bullets.remove(bullet)
        
        for obstacle in obstacles:
            if player.colliderect(obstacle[0]):
                HEALTH -= 1
                obstacles.remove(obstacle)
                if HEALTH < 5:
                    show_health = True
                if SCORE > 15:
                    show_health = False
        
        for obstacle in obstacles:
            for bullet in bullets:
                if bullet[0].colliderect(obstacle[0]):
                    obstacle[1] -= 1
                    bullets.remove(bullet)
                    if obstacle[1] <= 0:
                        obstacles.remove(obstacle)
                        break
            
        
        if player.colliderect(goal):
            move_random(goal)
            SCORE += 1
        
        if TIME % (ENEMY_TIMER * 60) == 0:
            obstacles.append([pygame.Rect(random.randrange(20, WIDTH - 20), random.randrange(20, WIDTH - 20), 20, 20), ENEMY_HEALTH])
        
        if player.colliderect(extra_health):
            HEALTH += 1
            move_random(extra_health)
            if HEALTH >= 5:
                show_health = False
                extra_health.x = 1000
        elif not show_health:
            extra_health.x = 200
        
        if LEVEL <= 1:
            powerup.x = 1000
            powerup.y = 1000
        elif powerup.x == 1000:
            powerup.x = random.randrange(0, WIDTH - powerup.width)
            powerup.y = random.randrange(0, WIDTH - powerup.width)

        if player.colliderect(powerup):
            homing_bullets = True
            now = time.time()
            show_powerup = now + 15
            end_powerup = now + 10
            powerup.x = 10000
            powerup.y = 10000
        
        if powerup.x == 10000:
            if time.time() >= show_powerup:
                powerup.x = random.randrange(0, WIDTH - powerup.width)
                powerup.y = random.randrange(0, WIDTH - powerup.width)
            if time.time() >= end_powerup:
                homing_bullets = False

        if HEALTH <= 0:
            draw_win("You lose. Your score was {}".format(SCORE))
            run = False
        
        if player.colliderect(door):
            if MOVE_ROOM:
                bullets = []
                obstacles = []
                MOVE_ROOM = False
                if LOCATION == "Room 1":
                    LOCATION = "Room 2"
                    DOOR_LOCATION[1] = WIDTH - 50
                    door.y = WIDTH - 50
                    player.x = WIDTH // 2 - player.width
                    player.y = DOOR_LOCATION[1]
                elif LOCATION == "Room 2":
                    LOCATION = "Room 1"
                    DOOR_LOCATION[1] = 0
                    door.y = 0
                    player.x = WIDTH // 2 - player.width
                    player.y = DOOR_LOCATION[1]
            
        if not player.colliderect(door) and not MOVE_ROOM:
            MOVE_ROOM = True
        
        if LOCATION == "Room 1":
            draw_room1(WIN)
            if player.colliderect(portal1):
                if teleport:
                    player.x, player.y = WIDTH - 50 - player.width // 2, WIDTH // 2 - player.height // 2
                    teleport = False
                    now = time.time()
                    future = now + 5
            
            if player.colliderect(portal2):
                if teleport:
                    player.x, player.y = 50, WIDTH // 2 - player.height // 2
                    teleport = False
                    now = time.time()
                    future = now + 5
                
            if not teleport:
                if time.time() >= future:
                    teleport = True

            if player.colliderect(water):
                update_pos(player, keys_pressed, VEL // 3)
            elif player.colliderect(sand):
                update_pos(player, keys_pressed, VEL // 2)
            else:
                update_pos(player, keys_pressed, VEL)
        elif LOCATION == "Room 2":
            draw_room2(WIN)
            update_pos(player, keys_pressed, VEL)

        draw(WIN, obstacles, goal, HEALTH, extra_health, show_health, bullets, SCORE, powerup, PLAYER)
        
        if SCORE >= LEVEL_SCORE:
            SCORE = 0
            LEVEL += 1
            if LEVEL == 2:
                LEVEL_SCORE = 10
                ENEMY_TIMER = 2
                ENEMY_HEALTH = 2
            elif LEVEL == 3:
                LEVEL_SCORE = 15
                ENEMY_HEALTH = 3
                ENEMY_TIMER = 2
            elif LEVEL == 4:
                ENEMY_HEALTH = 3
                LEVEL_SCORE = 15
                ENEMY_TIMER = 1
                OBS_VEL = 4
            else:
                draw_win("You Win!")
                main()
            level_text = LEVEL_FONT.render("LEVEL {}".format(LEVEL), 1, (0, 0, 0))
            WIN.blit(level_text, (WIDTH // 2 - level_text.get_width() // 2, WIDTH // 2 - level_text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(2000)

        TIME += 1
    
    
    main()


if __name__ == "__main__":
    main()
