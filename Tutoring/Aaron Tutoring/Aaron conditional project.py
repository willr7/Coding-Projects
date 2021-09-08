import pygame

WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Fun game")

playerone_score = 0
playertwo_score = 0
time = 0
winner = ''

# if the time limit is reached
# if player one has a higher score then 

while 1:
    pygame.time.Clock().tick(60)
    time += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LSHIFT:
            playerone_score += 1
            print(playerone_score)
        elif event.key == pygame.K_RSHIFT:
            playertwo_score += 1
            print(playertwo_score)
        event.key = pygame.K_SPACE
    
    if time == 600:
        if playerone_score > playertwo_score:
            print("player one wins with a score of {}, player two had a score of {}".format(playerone_score, playertwo_score))
        elif playertwo_score > playerone_score:
            print("player two wins with a score of {}, player one had a score of {}".format(playertwo_score, playerone_score))
        else:
            print("its a draw")
        quit()