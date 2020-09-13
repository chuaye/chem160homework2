from random import choices
ntrials=15000
player1wins=0
for i in range(ntrials):
# Player 2: Roll dice 2 times, continue if both dice rolls are equal, list
    player2=[]  # Outcomes for player2
    player2=choices(range(1,7),k=2)  # k is the number of rolls
    if player2[0]==player2[1]: # continue if both dice rolls are the same
        continue
# Player1:Roll dice 3 times, sort rolls from high to low, highest 2 chosen, list
    player1=[]  # Outcomes for player1
    player1=choices(range(1,7),k=3) # k is the number of rolls
    player1.sort(reverse=True)  # Sorting list in reverse order from highest to lowest
    if player1[0]+player1[1] > player2[0]+player2[1]:  # 2 highest rolls of player1 vs player 2 comparison
        player1wins=player1wins+1
ratio=player1wins/ntrials
print(ratio)
#This game is unfair, Player1 usually wins. The winning probably is about 1-2% higher than 50%.