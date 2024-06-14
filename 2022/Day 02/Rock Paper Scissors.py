# -*- coding: utf-8 -*-
"""
Calculate The Rock Paper Scissors Game

Created on Fri Dec  2 22:58:02 2022

@author: FAKENAME

What would your total score be if everything
goes exactly according to your strategy guide?

The scores are calculated as follows:

    1 for Rock
    2 for Paper
    3 for Scissors

    0 if you lost
    3 if the round was a draw
    6 if you won

"""

won = 6
draw = 3
lost = 0

scores = []

# Matrix to store how the games go
result_matr = [[draw, won, lost], [lost, draw, won], [won, lost, draw]]

# Read the file into memory
with open("input.txt") as file:

    # Read the line in one at a time
    for line in file:

        match_score = 0

        # Parse the Commands. Convert the letters to numbers
        opp_move = ord(line[0]) - ord('A')
        my_move = ord(line[2]) - ord('X')

        # Work out what the result of the match
        result = result_matr[opp_move][my_move]

        # Save the score
        scores.append(result + my_move + 1)

print(f"My total score is {sum(scores)}")