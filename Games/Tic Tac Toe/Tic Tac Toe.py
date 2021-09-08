import random

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def createBoard(board):
        print("  {}  |   {}   |  {}  ".format(board[0], board[1], board[2]))
        print("_____|_______|_____")
        print("  {}  |   {}   |  {}  ".format(board[3], board[4], board[5]))
        print("_____|_______|_____")
        print("  {}  |   {}   |  {}  ".format(board[6], board[7], board[8]))
        print("     |       |     ")

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
    childPosition = position.copy()
    bestMoves = []

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
            childPosition[i] = 'X'
            eval = minimax(childPosition, 0, False, alpha, beta)
            childPosition = position.copy()
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
            childPosition[i] = 'X'
            eval = minimax(childPosition, 1, True, alpha, beta)
            childPosition = position.copy()
            if eval == minEval:
                bestMoves.append(i)
        return bestMoves[random.randrange(len(bestMoves))]



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

restart = 'y'
round = 0

while restart == 'y':

    print("Who will go first? \n")
    print("1 ---> Player goes first")
    first = int(input("2 ---> AI goes first\n"))












    while round < 9:
        createBoard(board)
        if round % 2 == 0:
            if first == 1:
                playerMove = int(input("What is your move? \n"))
                while not playerMove in possibleMoves(board):
                    playerMove = int(input("Invalid move. Try again \n"))
                board[playerMove] = 'X'
            else:
                computerMove = findBestMove(board, 'X')
                board[computerMove] = 'X'
                print("AI move: {}".format(computerMove))
        elif round % 2 == 1:
            if first == 2:
                playerMove = int(input("What is your move? \n"))
                while not playerMove in possibleMoves(board):
                    playerMove = int(input("Invalid move. Try again \n"))
                board[playerMove] = 'O'
            else:
                computerMove = findBestMove(board, 'O')
                board[computerMove] = 'O'
                print("AI move: {}".format(computerMove))
        
        round = round + 1

        if checkwin(board) == 1:
            createBoard(board)
            print("Player X won!\n")
            break
        if checkwin(board) == -1:
            createBoard(board)
            print("Player O won!\n")
            break
        if round == 9:
            createBoard(board)
            print("Tie! \n")
    
    round = 0
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    restart = input("Do you want to play again? (y/n) \n")