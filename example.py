#Given a player_turn list that gives the turn of players in a round-robin game system as ['player1','player2','player3'].
#Write a python program using collections. deque module to simulate the game rounds. Keep rotating the players using the rotate methods until
#5 rounds are complete and print the data after each round. Suppose initial rotation will be conducted clockwise.

from collections import deque
def myCode(player_turn):
    data_after_each_round=deque(player_turn)
    for i in range(5):
        data_after_each_round.rotate(-1)  # Rotate the deque to the left (clockwise)
        print("Round", i+1, ":",  list(data_after_each_round))

player_turn=['player1','player2','player3']
myCode(player_turn) 