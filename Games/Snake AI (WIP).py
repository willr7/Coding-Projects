import pygame
import math
import random

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Snake game")

snake_body = []

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.color = WHITE
        self.x = row * width
        self.y = col * width
        self.direction = ''
        self.old_direction = ''
        self.order = 0

    def make_barrier(self):
        self.color = BLACK
    
    def make_snake(self):
        self.color = GREEN
    
    def make_food(self):
        self.color = ORANGE

    def make_empty(self):
        self.color = WHITE
    
    def make_head(self):
        self.is_head = True

    def is_barrier(self):
        return self.color == BLACK

    def is_snake(self):
        return self.color == GREEN
    
    def is_food(self):
        return self.color == ORANGE



def make_grid(rows, width):
    temp_list = []

    gap = width // rows

    for i in range(rows):
        temp_list.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
                node.make_barrier()
            temp_list[i].append(node)
    
    return temp_list

def draw(grid):
    for row in grid:
        for node in row:
            pygame.draw.rect(WIN, node.color, (node.x, node.y, node.width, node.width))



GRID = make_grid(50, 800)

def random_point_generator(color):
    temp_list = []
    make_head = True

    for row in GRID:
        for node in row:
            if not node.is_barrier() and not node.is_snake() and not node.is_food():
                temp_list.append(node)
    rand = random.randrange(len(temp_list))
    
    for row in GRID:
        for node in row:
            if node.is_snake():
                make_head = False

    temp_list[rand].color = color

    if make_head:
        temp_list[rand].order = 1
        snake_body.append(temp_list[rand])
    


def move_snake():
    for node in snake_body:
        if node.direction == pygame.K_LEFT:
            if GRID[(node.row - 1)][node.col].is_barrier():
                quit()
            elif GRID[(node.row - 1)][node.col].is_food():
                GRID[(node.row - 1)][node.col].make_snake()
                snake_body[node.order - 1] = GRID[(node.row - 1)][node.col]
                snake_body[-1].direction = snake_body[-2].old_direction
                snake_body[-1].order = len(snake_body)
                GRID[(node.row - 1)][node.col].order = node.order
            elif node.old_direction == pygame.K_RIGHT:
                break
            else:
                node.make_empty()
                GRID[(node.row - 1)][node.col].make_snake()
                snake_body[node.order - 1] = GRID[(node.row - 1)][node.col]
                GRID[(node.row - 1)][node.col].order = node.order
                node.order = 0

        elif node.direction == pygame.K_RIGHT:
            if GRID[(node.row + 1)][node.col].is_barrier():
                quit()
            elif GRID[(node.row + 1)][node.col].is_food():
                GRID[(node.row + 1)][node.col].make_snake()
                snake_body.append(GRID[(snake_body[-1].row - 1)][snake_body[-1].col])
                snake_body[node.order - 1] = GRID[(node.row + 1)][node.col]
                snake_body[-1].direction = snake_body[-2].old_direction
                snake_body[-1].order = len(snake_body)
                GRID[(node.row + 1)][node.col].order = node.order
            elif node.old_direction == pygame.K_LEFT:
                break
            else:
                node.make_empty()
                GRID[(node.row + 1)][node.col].make_snake()
                snake_body[node.order - 1] = GRID[(node.row + 1)][node.col]
                GRID[(node.row + 1)][node.col].order = node.order
                node.order = 0

        elif node.direction == pygame.K_DOWN:
            if GRID[node.row][(node.col + 1)].is_barrier():
                quit()
            elif GRID[node.row][(node.col + 1)].is_food():
                GRID[node.row][(node.col + 1)].make_snake()
                snake_body.append(GRID[snake_body[-1].row][snake_body[-1].col + 1])
                snake_body[node.order - 1] = GRID[node.row][node.col + 1]
                snake_body[-1].direction = snake_body[-2].old_direction
                snake_body[-1].order = len(snake_body)
                GRID[node.row][(node.col + 1)].order = node.order
                node.order = 0
            elif node.old_direction == pygame.K_UP:
                break
            else:
                node.make_empty()
                GRID[node.row][(node.col + 1)].make_snake()
                snake_body[node.order - 1] = GRID[node.row][node.col + 1]
                GRID[node.row][(node.col + 1)].order = node.order
                node.order = 0

        elif node.direction == pygame.K_UP:
            if GRID[node.row][(node.col - 1)].is_barrier():
                quit()
            elif GRID[node.row][(node.col - 1)].is_food():
                GRID[node.row][(node.col - 1)].make_snake()
                snake_body.append(GRID[snake_body[-1].row][snake_body[-1].col - 1])
                snake_body[node.order - 1] = GRID[node.row][node.col + 1]
                snake_body[-1].direction = snake_body[-2].old_direction
                snake_body[-1].order = len(snake_body)
                GRID[node.row][(node.col - 1)].order = node.order
                node.order = 0
            elif node.old_direction == pygame.K_DOWN:
                break
            else:
                node.make_empty()
                GRID[node.row][(node.col - 1)].make_snake()
                snake_body[node.order - 1] = GRID[node.row][node.col - 1]
                GRID[node.row][(node.col - 1)].order = node.order
                node.order = 0

random_point_generator(GREEN)
random_point_generator(ORANGE)

direction = ''

while 1:

    new_food = True

    pygame.time.Clock().tick(10)
    
    
    snake_body.sort(key=lambda x: x.order)

    keys_pressed = pygame.key.get_pressed()
    
    if keys_pressed[pygame.K_LEFT]:
        direction = pygame.K_LEFT
    elif keys_pressed[pygame.K_RIGHT]:
        direction = pygame.K_RIGHT
    elif keys_pressed[pygame.K_DOWN]:
        direction = pygame.K_DOWN
    elif keys_pressed[pygame.K_UP]:
        direction = pygame.K_UP
    
    snake_body[0].direction = direction

    for node in snake_body:
        node.old_direction = node.direction

    if len(snake_body) > 1:
        for i in range(1, len(snake_body)):
            snake_body[i].direction = snake_body[i - 1].old_direction

    move_snake()

    for row in GRID:
        for node in row:
            if node.is_food():
                new_food = False
    
    if new_food:
        random_point_generator(ORANGE)

    WIN.fill(WHITE)
    draw(GRID)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()