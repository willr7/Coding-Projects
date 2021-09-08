def createBoard(board):
        print("  {}  |   {}   |  {}  ".format(board[0], board[1], board[2]))
        print("_____|_______|_____")
        print("  {}  |   {}   |  {}  ".format(board[3], board[4], board[5]))
        print("_____|_______|_____")
        print("  {}  |   {}   |  {}  ".format(board[6], board[7], board[8]))
        print("     |       |     ")

def possible_moves(board):
    temp_list = []
    for i in range(9):
        if board[i] == " ":
            temp_list.append(i + 1)
    return temp_list

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

def minimax(depth, maximizingPlayer, position):
    childPosition = position.copy()

    if checkwin(position):
        return checkwin(position)
    elif not len(possible_moves(position)):
        return 0
    
    if maximizingPlayer:
        bestEval = -1000000
        for i in possible_moves(position):
            childPosition = position.copy()
            childPosition[i - 1] = 'X'
            eval = minimax(depth + 1, False, childPosition)
            bestEval = max(eval, bestEval)
        return bestEval
    else:
        bestEval = 100000
        for i in possible_moves(position):
            childPosition = position.copy()
            childPosition[i - 1] = 'O'
            eval = minimax(depth + 1, True, childPosition)
            bestEval = min(eval, bestEval)
            childPosition = position.copy()
        return bestEval

def find_best_move(position, player):
    if player == 'X':
        bestEval = -10000
        for i in possible_moves(position):
            childPosition = position.copy()
            childPosition[i - 1] = player
            eval = minimax(0, False, childPosition)
            if eval > bestEval:
                bestEval = eval
                bestMove = i - 1
    else:
        bestEval = 10000
        for i in possible_moves(position):
            childPosition = position.copy()
            childPosition[i - 1] = player
            eval = minimax(1, True, childPosition)
            if eval < bestEval:
                bestEval = eval
                bestMove = i - 1
    
    return bestMove



def main():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    round = 0
    createBoard(board)
    while checkwin(board) == 0 and round < 9:
        if round % 2 == 0:
            player = 'X'
        else:
            player = 'O'

        if player == 'X':
            move = int(input("What is your move?\n"))
            while not(move in possible_moves(board)):
                move = int(input("Invalid move. Try again\n"))

            board[move - 1] = player
        else:
            move = find_best_move(board, 'O')
            board[move] = player
            print("Computer move: {}".format(move + 1))

        createBoard(board)

        round += 1

    if checkwin(board):
        print("player {} wins!".format(player))
    else:
        print("draw!")

    restart = input("play again? y/n \n")
    while not restart in 'yn':
        restart = input("Please type y or n")
    
    if restart == 'y':
        main()

if __name__ == "__main__":
    main()