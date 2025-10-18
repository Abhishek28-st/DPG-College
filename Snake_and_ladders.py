# Simple Snake and Ladders game implementation in Python
import random

def roll_dice():
    return random.randint(1, 6) 
def move_player(position, roll):
    position += roll
    if position > 100:
        position = 100 - (position - 100)  # Bounce back if overshoot
    return position
def check_snakes_and_ladders(position):
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    
    if position in snakes:
        print(f"Oops! Bitten by a snake at {position}. Going down to {snakes[position]}.")
        return snakes[position]
    elif position in ladders:
        print(f"Yay! Climbed a ladder at {position}. Going up to {ladders[position]}.")
        return ladders[position]
    return position
def play_game():
    player1_pos = 0
    player2_pos = 0
    turn = 0  # 0 for player1, 1 for player2
    
    while player1_pos < 100 and player2_pos < 100:
        if turn == 0:
            input("Player 1's turn. Press Enter to roll the dice...")
            roll = roll_dice()
            print(f"Player 1 rolled a {roll}.")
            player1_pos = move_player(player1_pos, roll)
            player1_pos = check_snakes_and_ladders(player1_pos)
            print(f"Player 1 is now at position {player1_pos}.\n")
            if player1_pos == 100:
                print("Player 1 wins!")
                break
            turn = 1
        else:
            input("Player 2's turn. Press Enter to roll the dice...")
            roll = roll_dice()
            print(f"Player 2 rolled a {roll}.")
            player2_pos = move_player(player2_pos, roll)
            player2_pos = check_snakes_and_ladders(player2_pos)
            print(f"Player 2 is now at position {player2_pos}.\n")
            if player2_pos == 100:
                print("Player 2 wins!")
                break
            turn = 0
if __name__ == "__main__":
    play_game() 
    


    

