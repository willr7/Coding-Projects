# for i in range(100):
#     print(i)

# for i in range(100):
#     if i % 3 == 0:
#         print(i)
    
# crewmates = ['Red', 'Black', 'Blue', 'Orange']

# for crewmate in crewmates:
#     print(crewmate)

# for crewmate in crewmates:
#     if 'a' in crewmate and 'l' in crewmate:
#         print(crewmate + " is ithe imposter")














    
# def recur_fibo(n):
#     if n <= 1:
#         return n
    
#     return (recur_fibo(n - 1) + recur_fibo(n - 2))

# for i in range(5):
#     print(recur_fibo(i))

# def recur_fact(n):
#     if n <= 1:
#         return 1
#     else:
#         return recur_fact(n - 1) * n

# print(recur_fact(5))

# def possibleMoves(position):
#     return []

# def checkwin(position):
#     return 1

# def minimax(depth, maximizingPlayer, position):
#     childPosition = position

#     if checkwin(position) == 1: 
#         return 1
#     if checkwin(position) == -1: 
#         return -1
#     if len(possibleMoves(position)) == 0: 
#         return 0
    
#     if maximizingPlayer:
#         bestEval = -1000
#         for i in possibleMoves(position):
#             childPosition[i] = 'X'
#             eval = minimax(depth + 1, False, childPosition)
#             bestEval = max(eval, bestEval)
#         return bestEval
#     else:
#         bestEval = 1000
#         for i in possibleMoves(position):
#             childPosition[i] = 'O'
#             eval = minimax(depth + 1, True)
#             bestEval = min(eval, bestEval)
#         return bestEval