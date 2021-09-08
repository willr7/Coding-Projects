import pygame
from pygame import sndarray
from pygame.constants import WINDOWRESTORED
from pygame.time import Clock
import random
pygame.font.init()
import time
import math

WIDTH = 600
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("poopy")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (255, 228, 196)

door_image = pygame.image.load("door.png")

portal_img = pygame.image.load("portal.png")

health_font = pygame.font.SysFont("comicsans", 20, bold=True, italic=True)
score_font = pygame.font.SysFont("comicsans", 20, bold=False, italic=False)
end_font = pygame.font.SysFont("comicsans", 100, bold=True, italic=False)

sqr = pygame.Rect((WIDTH - 50, HEIGHT // 2 - 25, 50, 50))
Portal = pygame.Rect((WIDTH - 520, HEIGHT - 430, 50, 50))
Portal_2 = pygame.Rect((500, 490, 50, 50))

health_potion = pygame.Rect((WIDTH // 2 - 25, HEIGHT // 2 - 25, 25, 25))
water = pygame.Rect((WIDTH // 2 - 50, HEIGHT // 2 - 50, 100, 100))
large_obstacle = pygame.Rect((WIDTH // 2 - 150, HEIGHT // 2 - 150, 300, 300))
door = pygame.Rect((WIDTH // 2 - 50, 0, 100, 100))

clock = pygame.time.Clock()

bullets = []

def generate_obstacles(n, enemy_health):
    obstacles = []
    for i in range(n):
        obstacles.append([pygame.Rect(random.randrange(0, WIDTH - 15), random.randrange(0, HEIGHT - 15), 15, 15), enemy_health])
    return obstacles

def move_obstacles(objisticle, vel):
    
    if objisticle.x < sqr.x + sqr.width // 2 - 10:
        objisticle.x += vel
    if objisticle.y < sqr.y + sqr.height // 2 - 10:
        objisticle.y += vel
    if objisticle.x > sqr.x + sqr.width // 2 - 10:
        objisticle.x -= vel
    if objisticle.y > sqr.y + sqr.height // 2 - 10:
        objisticle.y -= vel
    if objisticle.y > HEIGHT - objisticle.height:
        objisticle.y = 0
        objisticle.x = random.randrange(0, WIDTH - 15)

def draw_end(text):
    draw_text = end_font.render(text, 1, RED)
    WIN.blit(draw_text, (80, 150))

    pygame.display.update()
    pygame.time.delay(2000)

def draw_score(text):
    draw_text = health_font.render(text, 1, BLACK)
    WIN.blit(draw_text, (530, 5))


def draw_health(text):
    draw_text = health_font.render(text, 1, BLACK)
    WIN.blit(draw_text, (5, 5))


def draw(win, obstacles, health, score, health_potion, health_potion_B, door, boi_image):
    pygame.draw.rect(win, YELLOW, large_obstacle)

    pygame.draw.rect(win, BLUE, water)

    for obstacle in obstacles:
        pygame.draw.rect(WIN, BROWN, obstacle[0])

    WIN.blit(door_image, (door.x, door.y))

    WIN.blit(boi_image, (sqr.x, sqr.y))

    pygame.draw.rect(win, RED, Portal_2)
    WIN.blit(portal_img, (500, 490))

    pygame.draw.rect(win, RED, Portal)
    WIN.blit(portal_img, (WIDTH - 520, HEIGHT - 430))
    if health_potion_B:
        pygame.draw.rect(win, RED, health_potion)

    for bullet in bullets:
        pygame.draw.rect(win, BLACK, bullet[0])

    draw_health("HEALTH: {}".format(health))
    draw_score("Score: {}".format(score))

    pygame.display.update()
    



def move(keys_pressed, obj, obj_2, vel):
    if keys_pressed[pygame.K_w] and not obj.y - vel < 0:
        obj.y -= vel
    if keys_pressed[pygame.K_a] and not obj.x - vel < 0:
        obj.x -= vel
    if keys_pressed[pygame.K_s] and not obj.y + vel > WIDTH - obj.height:
        obj.y += vel
    if keys_pressed[pygame.K_d] and not obj.x + vel > WIDTH - obj.width:
        obj.x += vel

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

def bullet_movement(bullets):
    for bullet in bullets:
        bullet[0].x += bullet[1]
        bullet[0].y += bullet[2]


def main():
    now = time.time()
    teleport = False
    BULLET_VEL = 10
    run = True
    teleport = True
    health = 5
    score = 0
    enemy_health = 1
    obstacles = generate_obstacles(2,  enemy_health)
    level = 1
    level_score = 5
    health_potion_B = True
    boi_face_now = 1
    boi_face_later = 1
    boi_image = pygame.image.load("player.png")
    while run:
        
        VEL = 15
        clock.tick(60)
        keys_pressed = pygame.key.get_pressed()
        OBS_VEL = 3

        if sqr.colliderect(water):
            VEL /= 1.9

        if sqr.colliderect(large_obstacle):
            VEL /= 1.5

        if sqr.colliderect(health_potion):
            if health_potion_B == True:
                health_potion.x = random.randrange(WIDTH - 10)
                health_potion.y = random.randrange(HEIGHT - 10)
                health += 1
        if health >= 5:
            health_potion_B = False
        else:
            health_potion_B = True

        if sqr.colliderect(Portal):
            if teleport:
                sqr.x, sqr.y = 500, 490
                teleport = False
                now = time.time()
                future = now + 5

        if sqr.colliderect(Portal_2):
            if teleport:
                sqr.x, sqr.y = WIDTH - 520, HEIGHT - 430
                teleport = False
                now = time.time()
                future = now + 5


        if teleport == False:
            if time.time() >= future:
                teleport = True

        for bullet in bullets:
            for obstacle in obstacles:
                if bullet[0].colliderect(obstacle[0]):
                    obstacle[1] -= 1
                    if obstacle[1] <= 0:
                        obstacle[0].x = random.randrange(WIDTH - 10)
                        obstacle[0].y = random.randrange(HEIGHT - 10)
                        score += 1
                        obstacle[1] = enemy_health
                        break
                    bullets.remove(bullet)


        move(keys_pressed, sqr, VEL, VEL)
    
        for obstacle in obstacles:
            if obstacle[0].colliderect(sqr):
                obstacle[0].x = random.randrange(WIDTH - 15)
                obstacle[0].y = random.randrange(HEIGHT - 15)
                health -= 1
                break

            if obstacle[0].colliderect(water):
                move_obstacles(obstacle[0], OBS_VEL // 1.9)

            elif obstacle[0].colliderect(large_obstacle):
                move_obstacles(obstacle[0], OBS_VEL // 1.5)
            
            else:
                move_obstacles(obstacle[0], OBS_VEL)

        for event in pygame.event.get():


            sqr_x = sqr.x + sqr.width / 2
            sqr_y = sqr.y + sqr.height / 2
            bullet_x = pygame.mouse.get_pos()[0]
            bullet_y = pygame.mouse.get_pos()[1]
            x = bullet_x - sqr_x
            y = bullet_y - sqr_y

            if abs(x) >= abs(y) and x >= 0:
                boi_face_now = 4
            elif abs(y) >= abs(x) and y >= 0:
                boi_face_now = 3
            elif abs(x) >= abs(y) and x <= 0:
               boi_face_now = 2
            elif abs(y) >= abs(x) and y <= 0:
                boi_face_now = 1

            boi_image = pygame.transform.rotate(boi_image, 90 * (boi_face_now - boi_face_later))

            boi_face_later = boi_face_now

            if event.type == pygame.QUIT:
                quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    bullet = generate_bullets_boi(sqr, pygame.mouse.get_pos(), BULLET_VEL)
                    bullets.append(bullet)

        bullet_movement(bullets)

        draw(WIN, obstacles, health, score, health_potion, health_potion_B, door, boi_image)

        if health <= 0:
            draw_end("GAME OVER")
            run = False

        if score >= level_score:
            score = 0
            level += 1
            if level == 2:
                level_score = 10
                obstacles += generate_obstacles(1, enemy_health)
                draw_end("  LEVEL 2")
                enemy_health += 1
            if level == 3:
                level_score = 15
                obstacles += generate_obstacles(2, enemy_health)
                draw_end("  LEVEL 3")
                enemy_health += 1

            if level == 4:
                obstacles += generate_obstacles(3, enemy_health)
                draw_end("  LEVEL 4")
                enemy_health += 1

            if level == 5:
                draw_end("YOU win!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                main()
            


    main()

if __name__ == "__main__":
    main()