import pygame

WIDTH = 600
HEIGHT = 600
WIN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Checkers")

GRID = []

for i in range(8):
    for j in range(8):
        GRID.append([range(j * WIDTH // 8, (j + 1) * WIDTH // 8), range(i * WIDTH // 8, (i + 1) * WIDTH // 8)])


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

class Checker():
    def __init__(self, col, row, width, color):
        self.row = row
        self.col = col
        self.width = width
        self.color = color
        self.crowned = False
        self.x = row * width
        self.y = col * width
        self.held = False
        self.old_position = [self.x, self.y]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.width)
    
    def make_crowned(self):
        self.crowned = True
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x + 5, self.y + 5, self.width - 10, self.width - 10))
    
    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.width)
    
    def legal_moves(self, pieces):
        if self.color == RED:
            temp = [[self.old_position[0] // self.width - 1, self.old_position[1] // self.width - 1], [self.old_position[0] // self.width + 1, self.old_position[1] // self.width - 1]]
            for piece in pieces:
                if temp[0][0] == piece.old_position[0] // self.width and temp[0][-1] == piece.old_position[1] // self.width and piece.color == RED:
                    temp.remove(temp[0])
                if temp[-1][0] == piece.old_position[0] // self.width and temp[-1][-1] == piece.old_position[1] // self.width and piece.color == RED:
                    temp.remove(temp[-1])
                if temp[0][0] == piece.old_position[0] // self.width and temp[0][-1] == piece.old_position[1] // self.width and piece.color == BLACK:
                    if temp[0][0] > 0 and temp[0][-1] > 0:
                        temp[0][0] -= 1
                        temp[0][-1] -= 1
                if temp[-1][0] == piece.old_position[0] // self.width and temp[-1][-1] == piece.old_position[1] // self.width and piece.color == BLACK:
                    if temp[-1][0] > 0 and temp[-1][1] < 7:
                        temp[-1][0] -= 1
                        temp[-1][1] += 1
                        return temp

                if len(temp) == 0:
                    return temp
            pygame.draw.rect(WIN, GREEN, (temp[0][0] * self.width, temp[0][1] * self.width, self.width, self.width))
            pygame.draw.rect(WIN, GREEN, (temp[-1][0] * self.width, temp[-1][1] * self.width, self.width, self.width))
            return temp
        elif self.color == BLACK:
            temp = [[self.old_position[0] // self.width - 1, self.old_position[1] // self.width + 1], [self.old_position[0] // self.width + 1, self.old_position[1] // self.width + 1]]
            for piece in pieces:
                if temp[0][0] == piece.old_position[0] // self.width and temp[0][-1] == piece.old_position[1] // self.width and piece.color == BLACK:
                    temp.remove(temp[0])
                elif temp[-1][0] == piece.old_position[0] // self.width and temp[-1][-1] == piece.old_position[1] // self.width and piece.color == BLACK:
                    temp.remove(temp[1])
                if len(temp) == 0:
                    break
            return temp

    def update_rows_cols(self):
        self.row = (self.x + self.width // 2) // self.width
        self.col = (self.y + self.width // 2) // self.width

def make_grid(win):
    for i in range(0, WIDTH + 1, WIDTH // 8):
        pygame.draw.line(win, BLACK, (i, 0), (i, HEIGHT), 5)
        pygame.draw.line(win, BLACK, (0, i), (WIDTH, i), 5)
    
def make_pieces():
    pieces = []

    for i in range(3):
        for j in range(4):
            if i % 2:
                piece = Checker(i, (j * 2 + 1), WIDTH // 8, BLACK)
            else:
                piece = Checker(i, (j * 2), WIDTH // 8, BLACK)
            pieces.append(piece)
        
    for i in range(3):
        for j in range(4):
            if not i % 2:
                piece = Checker(i + 5, (j * 2 + 1), WIDTH // 8, RED)
            else:
                piece = Checker(i + 5, (j * 2), WIDTH // 8, RED)
            pieces.append(piece)
        
    return pieces
                
    

pieces = make_pieces()
check_square = False
holding_piece = False

run = True

while run:
    WIN.fill(WHITE)
    make_grid(WIN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if pygame.mouse.get_pressed()[0]:
            pieces.sort(key=lambda x: x.held, reverse=True)
            for piece in pieces:
                if piece.rect.collidepoint(pygame.mouse.get_pos()) and not holding_piece:
                    piece.x = pygame.mouse.get_pos()[0] - piece.width // 2
                    piece.y = pygame.mouse.get_pos()[1] - piece.width // 2
                    current_piece = piece
                    check_square = True
                    holding_piece = True
                    piece.held = True
            holding_piece = False
        if not pygame.mouse.get_pressed()[0] and check_square:
            for piece in pieces:
                piece.held = False
            holding_piece = False
            for node in GRID:
                if pygame.mouse.get_pos()[0] in node[0] and pygame.mouse.get_pos()[1] in node[1]:
                    if [current_piece.row, current_piece.col] in current_piece.legal_moves(pieces):
                        current_piece.x = node[0][0]
                        current_piece.y = node[1][0]
                        current_piece.old_position = [current_piece.x, current_piece.y]
                        check_square = False
                    else:
                        current_piece.x, current_piece.y = current_piece.old_position

    pieces.sort(key=lambda x: x.held, reverse=False)
    for piece in pieces:
        piece.update_rect()
        piece.update_rows_cols()
        piece.draw(WIN)
    pygame.display.update()
            