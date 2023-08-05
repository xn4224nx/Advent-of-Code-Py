"""
--- Day 4: Giant Squid ---

The submarine has a bingo subsystem to help passengers (currently, you and the
giant squid) pass the time. It automatically generates a random order in which
to draw numbers and a random set of boards (your puzzle input).

The winning board is the first to get a row or column.

The score of the winning board can now be calculated. Start by finding the sum
of all unmarked numbers on that board; in this case, the sum is 188. Then,
multiply that sum by the number that was just called when the board won, 24, to
get the final score, 188 * 24 = 4512.

Part 1:
    To guarantee victory against the giant squid, figure out which board will
    win first. What will your final score be if you choose that board?

"""

import numpy as np


class BingoGame:

    def __init__(self, data_path: str):

        # Load the data about the initial game setup
        self.raw_data = open(data_path, "r").read().splitlines()

        # Parse the numbers to be called
        self.call_numbers = np.array([int(x) for x in self.raw_data[0].split(",")])

        # Storage of the player data
        self.player_data = []

        # Determine the number of boards
        self.players = len(self.raw_data)//6

        # Parse the bingo data
        for i in range(self.players):

            start_idx = 6 * i + 2
            final_idx = 6 * i + 7

            # Extract the players board data
            board = self.raw_data[start_idx:final_idx]

            # Convert to a 2d numpy array
            board = np.array([[int(x) for x in line.split()] for line in board])

            # Store the data
            self.player_data.append({
                "board": board,
                "score": np.full(
                          shape=(5, 5),
                          fill_value=False,
                          dtype=np.bool_)
            })

    def call_number(self, call_number: int):
        """
        Run a round of bingo.
        """

        # Iterate over every player
        for i in range(self.players):

            # Change every instance of the called number to True in score
            mask = self.player_data[i]["board"] == call_number
            print(mask)

            self.player_data[i]["score"][
                self.player_data[i]["score"] != mask] = True


if __name__ == "__main__":

    # Sample Game
    sample = BingoGame("./data/sample.txt")

    sample.call_number(7)

    print(sample.call_numbers)


