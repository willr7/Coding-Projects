# Pi approximation
import pygame
import random
import math

WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pi approximation")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

def pixel(surface, color, pos):
    pygame.draw.circle(surface, color, pos, 2)
    pygame.display.update()



WIN.fill(WHITE)

def clear(win):
    win.fill(WHITE)
    pygame.draw.arc(win, BLACK, (150, 50, 300, 300), 10, 20, 1)
    pygame.display.update()

def approximate_pi(num, win):

    points = 0
    in_circle = 0

    for i in range(num):
        x = random.randint(150, 450)
        y = random.randint(50, 350)
        radius = math.sqrt((x - 300) ** 2 + (y - 200) ** 2)

        if radius <= 150: 
            pixel(WIN, RED, [x, y])
            in_circle += 1
        else:
            pixel(WIN, BLACK, [x, y])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()

        pygame.init()

        font = pygame.font.Font('freesansbold.ttf', 24)

        points += 1

        counter = font.render('{} out of {} points generated'.format(points, num), True, BLACK, WHITE)

        counterRect = counter.get_rect()

        counterRect.center = (WIDTH // 2, 500)

        pygame.draw.rect(win, WHITE, (0, 400, WIDTH, 200))
        win.blit(counter, counterRect)
        
        pi = in_circle/points * 4     
    
        displayPi = font.render("This algorithm has approximated pi to {}".format(round(pi, 4)), True, BLACK, WHITE)

        displayPi_rect = displayPi.get_rect()

        displayPi_rect.center = (WIDTH // 2, 450)

        win.blit(displayPi, displayPi_rect)

        pygame.display.update()

    

pygame.draw.arc(WIN, BLACK, (150, 50, 300, 300), 10, 20, 1)

approximate_pi(1000, WIN)

while 1:
    pygame.display.update()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                clear(WIN)
                approximate_pi(1000, WIN)
            
            if event.key == pygame.K_1:
                clear(WIN)
                approximate_pi(1000, WIN)
            
            if event.key == pygame.K_2:
                clear(WIN)
                approximate_pi(2000, WIN)

            if event.key == pygame.K_3:
                clear(WIN)
                approximate_pi(3000, WIN)
            
            if event.key == pygame.K_4:
                clear(WIN)
                approximate_pi(4000, WIN)

            if event.key == pygame.K_5:
                clear(WIN)
                approximate_pi(5000, WIN)
            
            if event.key == pygame.K_6:
                clear(WIN)
                approximate_pi(6000, WIN)
            
            if event.key == pygame.K_7:
                clear(WIN)
                approximate_pi(7000, WIN)

            if event.key == pygame.K_8:
                clear(WIN)
                approximate_pi(8000, WIN)

            if event.key == pygame.K_9:
                clear(WIN)
                approximate_pi(9000, WIN)

            if event.key == pygame.K_0:
                clear(WIN)
                approximate_pi(10000, WIN)