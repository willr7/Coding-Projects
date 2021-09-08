import pygame
import random
pygame.font.init()

WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Tic Tac Toe")

WINNER_FONT = pygame.font.SysFont('comicsans', 40, bold=False, italic=False)
CHOOSE_PLAYER_FONT = pygame.font.SysFont('comicsans', 20, bold=False, italic=False)

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

X_image = pygame.image.load('X.png')
O_image = pygame.image.load('O.png')

board_positions = [
    (range(0, 200), range(0, 200)),
    (range(200, 400), range(0, 200)),
    (range(400, 600), range(0, 200)),
    (range(0, 200), range(200, 400)),
    (range(200, 400), range(200, 400)),
    (range(400, 600), range(200, 400)),
    (range(0, 200), range(400, 600)),
    (range(200, 400), range(400, 600)),
    (range(400, 600), range(400, 600))
]

char_positions = [
    (75, 75),
    (250, 75),
    (425, 75),
    (75, 250),
    (250, 250),
    (425, 250),
    (75, 450),
    (250, 450),
    (425, 450)
]

def create_board(board):
    pygame.draw.line(WIN, BLACK, (200, 50), (200, 550), 2)
    pygame.draw.line(WIN, BLACK, (400, 50), (400, 550), 2)
    pygame.draw.line(WIN, BLACK, (50, 200), (550, 200), 2)
    pygame.draw.line(WIN, BLACK, (50, 400), (550, 400), 2)
    for i in range(9):
        if board[i] == 'X':
            WIN.blit(X_image, char_positions[i])
        elif board[i] == 'O':
            WIN.blit(O_image, char_positions[i])

def draw_move(player, position):
    if position == 0 and player == 'X':
        WIN.blit(X_image, (75, 75))

def make_move(pos, player):
    if pos[0] in range(200, 400) and pos[1] in range(200, 400):
        draw_move(player, 0)

def possibleMoves(board):
    tempList = []
    for i in range(9):
        if board[i] == ' ':
            tempList.append(i)
    return tempList

def minimax(position, maximizingPlayer, depth, alpha, beta):
    childBoard = position.copy()

    if checkwin(position) == 1: 
        return 10 - depth
    if checkwin(position) == -1: 
        return -10 + depth
    if len(possibleMoves(position)) == 0: 
        return 0
    
    if maximizingPlayer:
        bestEval = -1000
        for i in (possibleMoves(position)):
            childBoard[i] = 'X'
            eval = minimax(childBoard, False, depth + 1, alpha, beta)
            childBoard = position.copy()
            bestEval = max(eval, bestEval)
            alpha = max(alpha, bestEval)
            if beta <= alpha:
                break
        return bestEval
    else:
        bestEval = 1000
        for i in (possibleMoves(position)):
            childBoard[i] = 'O'
            eval = minimax(childBoard, True, depth + 1, alpha, beta)
            childBoard = position.copy()
            bestEval = min(bestEval, eval)
            beta = min(beta, bestEval)
            if beta <= alpha:
                break
        return bestEval

def findBestMove(position, player):
    maxEval = -100
    minEval = 100
    alpha = -100
    beta = 100
    bestMoves = []
    childPosition = position.copy()

    if player == 'X':
        maximizingPlayer = True
    elif player == 'O':
        maximizingPlayer = False

    if maximizingPlayer:
        for i in (possibleMoves(position)):
            childPosition[i] = 'X'
            eval = minimax(childPosition, 0, False, alpha, beta)
            childPosition = position.copy()
            if eval > maxEval:
                maxEval = eval
                bestMove = i
        for i in possibleMoves(position):
            childPosition = position.copy()
            childPosition[i] = 'X'
            eval = minimax(childPosition, 0, False, alpha, beta)
            if eval == maxEval:
                bestMoves.append(i)
        return bestMoves[random.randrange(len(bestMoves))]
    else:
        for i in (possibleMoves(position)):
            childPosition[i] = 'O'
            eval = minimax(childPosition, 1, True, alpha, beta)
            childPosition = position.copy()
            if eval < minEval:
                minEval = eval
                bestMove = i
        for i in possibleMoves(position):
            childPosition = position.copy()
            childPosition[i] = 'O'
            eval = minimax(childPosition, 1, True, alpha, beta)
            if eval == minEval:
                bestMoves.append(i)
        return bestMoves[random.randrange(len(bestMoves))] 

# board = ["X", " ", " ", " ", "O", ]
def checkwin(board):
    # Horizontal win positions
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X': return 1
    if board[0] == 'O' and board[1] == 'O' and board[2] == 'O': return -1

    if board[3] == 'X' and board[4] == 'X' and board[5] == 'X': return 1
    if board[3] == 'O' and board[4] == 'O' and board[5] == 'O': return -1

    if board[6] == 'X' and board[7] == 'X' and board[8] == 'X': return 1
    if board[6] == 'O' and board[7] == 'O' and board[8] == 'O': return -1

    # Vertical win positions
    if board[0] == 'X' and board[3] == 'X' and board[6] == 'X': return 1
    if board[0] == 'O' and board[3] == 'O' and board[6] == 'O': return -1

    if board[1] == 'X' and board[4] == 'X' and board[7] == 'X': return 1
    if board[1] == 'O' and board[4] == 'O' and board[7] == 'O': return -1

    if board[2] == 'X' and board[5] == 'X' and board[8] == 'X': return 1
    if board[2] == 'O' and board[5] == 'O' and board[8] == 'O': return -1

    # Diagonal win positions
    if board[0] == 'X' and board[4] == 'X' and board[8] == 'X': return 1
    if board[0] == 'O' and board[4] == 'O' and board[8] == 'O': return -1

    if board[2] == 'X' and board[4] == 'X' and board[6] == 'X': return 1
    if board[2] == 'O' and board[4] == 'O' and board[6] == 'O': return -1

    return 0

def draw_choices(choice1, choice2):
    WIN.fill(WHITE)
    draw_choice1 = CHOOSE_PLAYER_FONT.render(choice1, 1, (0, 0, 0))
    draw_choice2 = CHOOSE_PLAYER_FONT.render(choice2, 1, (0, 0, 0))

    WIN.blit(draw_choice1, (WIDTH // 3 - draw_choice1.get_width() // 3, WIDTH // 2 - draw_choice1.get_height()))
    WIN.blit(draw_choice2, (2 * WIDTH // 3 - draw_choice2.get_height() // 3, WIDTH // 2 - draw_choice2.get_height()))
    pygame.display.update()

    return (pygame.Rect(WIDTH // 3 - draw_choice1.get_width() // 3, WIDTH // 2 - draw_choice1.get_height(), draw_choice1.get_width(), draw_choice1.get_height()), pygame.Rect(2 * WIDTH // 3 - draw_choice2.get_width() // 3, WIDTH // 2 - draw_choice2.get_height(), draw_choice2.get_width(), draw_choice2.get_height()))

def main():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    run = True
    computer = ''
    player = ''
    turn = 'X'

    choice1, choice2 = draw_choices("Player Goes First", "Computer Goes First")
    print(choice2.x)
    print(choice2.y)
    while computer == '':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Mouse Button Down")
                if pygame.mouse.get_pressed()[0]:
                    print("Left Click")
                    if choice1.collidepoint(pygame.mouse.get_pos()):
                        computer = 'O'
                        player = 'X'
                        print("Left Choice Clicked")
                    elif choice2.collidepoint(pygame.mouse.get_pos()):
                        computer = 'X'
                        player = 'O'
                        print("Right Choice Clicked")
    
    while run:
        WIN.fill(WHITE)
        create_board(board)
        pygame.display.update()

        if turn == computer:
            move = findBestMove(board, turn)
            board[move] = turn
            turn = player
            pygame.time.delay(200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(board_positions)):
                    if player == turn:
                        if pygame.mouse.get_pos()[0] in board_positions[i][0] and pygame.mouse.get_pos()[1] in board_positions[i][1]:
                            if i in possibleMoves(board):
                                board[i] = player
                                turn = computer
        if checkwin(board):
            if player == 'X':
                player = 'O'
            else:
                player = 'X'

            create_board(board)
            winner_text = WINNER_FONT.render("Player {} wins!".format(player), 1, (255, 0, 0))
            WIN.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, WIDTH // 2 - winner_text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(2000)
            main()
        elif not len(possibleMoves(board)):
            create_board(board)
            winner_text = WINNER_FONT.render("Draw!".format(player), 1, (255, 0, 0))
            WIN.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, WIDTH // 2 - winner_text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(2000)
            create_board(board)
            main()
    
    pygame.quit()

if __name__ == "__main__":
    main()