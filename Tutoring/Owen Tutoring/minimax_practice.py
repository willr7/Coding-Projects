def minimax(position, maximizingPlayer, depth):
    childBoard = position.copy()

    if checkwin(position) == 1: 
        return 10
    if checkwin(position) == -1: 
        return -10
    if len(possibleMoves(position)) == 0: 
        return 0
    
    if maximizingPlayer:
        bestEval = -1000
        for i in (possibleMoves(position)):
            childBoard[i] = 'X'
            eval = minimax(childBoard, False, depth + 1, alpha, beta)
            childBoard = position.copy()
            bestEval = max(eval, bestEval)
        return bestEval
    else:
        bestEval = 1000
        for i in (possibleMoves(position)):
            childBoard[i] = 'O'
            eval = minimax(childBoard, True, depth + 1, alpha, beta)
            childBoard = position.copy()
            bestEval = min(bestEval, eval)
        return bestEval

def findBestMove(position, player):
    maxEval = -100
    minEval = 100
    childPosition = position.copy()

    if player == 'X':
        maximizingPlayer = True
    elif player == 'O':
        maximizingPlayer = False

    if maximizingPlayer:
        for i in (possibleMoves(position)):
            childPosition[i] = 'X'
            eval = minimax(childPosition, 0, False)
            childPosition = position.copy()
            if eval > maxEval:
                maxEval = eval
                bestMove = i
        return bestMove
    else:
        for i in (possibleMoves(position)):
            childPosition[i] = 'O'
            eval = minimax(childPosition, 1, True)
            childPosition = position.copy()
            if eval < minEval:
                minEval = eval
                bestMove = i    
        return bestMove   