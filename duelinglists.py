#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Again, your lists should be random numbers
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = 5,7,2,9,1,1,3,8,6,9
#Player Two = 3,8,5,5,8,1,4,7,4,7
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random

player1 = []
player2 = []
player_1_score = 0
player_2_score = 0
ties = 0

for i in range(10):
    player1.append(random.randint(1,50))
    player2.append(random.randint(1,50))
print(f'Player 1 = {player1} \nPlayer 2 = {player2}')

i = 1
while i < (len(player1)):
    if player1[i] > player2[i]:
        player_1_score = player_1_score + 1
        print(f"Player 1 Won at index {i} with a score of {player1[i]} which is {player1[i]-player2[i]} points larger than player 2's score of {player2[i]}")
        i = i + 1
    elif player1[i] == player2[i]:
        print(f'Both players tied at index {i} with a score of {player1[i]}')
        ties = ties + 1
        i = i + 1
    else:
        player_2_score = player_2_score + 1
        print(f"Player 2 Won at index {i} with a score of {player2[i]} which is {player2[i]-player1[i]} points larger than player 1's score of {player1[i]}")
        i = i + 1

#ignor 0
player1_low = min(player1[1:])
player1_high = max(player1[1:])
player2_low = min(player2[1:])
player2_high = max(player2[1:])

print(f"Player 1's lowest number was {player1_low} at index {player1.index(player1_low,1 )}\nPlayer 2's lowest number was {player2_low} at index {player2.index(player2_low, 1)}")
print(f"Player 1's highest number was {player1_high} at index {player1.index(player1_high, 1)}\nPlayer 2's highest number was {player2_high} at index {player2.index(player2_high, 1)}")
print(f'Player 1 won {player_1_score} times \nPlayer 2 won {player_2_score} times')
if ties != 0:
    print(f"Players tied {ties} times")