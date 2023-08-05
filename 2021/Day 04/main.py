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

        # Define the size of the bingo board
        self.board_size = 5

        # Load the data about the initial game setup
        self.raw_data = open(data_path, "r").read().splitlines()

        # Parse the numbers to be called
        self.call_numbers = np.array([int(x) for x in self.raw_data[0].split(",")])

        # Storage of the player data
        self.player_data = []

        # Determine the number of boards
        self.players = len(self.raw_data)//(self.board_size + 1)

        # Parse the bingo data
        for i in range(self.players):

            start_idx = (self.board_size + 1) * i + 2
            final_idx = (self.board_size + 1) * i + 7

            # Extract the players board data
            board = self.raw_data[start_idx:final_idx]

            # Convert to a 2d numpy array
            board = np.array([[int(x) for x in line.split()] for line in board])

            # Store the data
            self.player_data.append({
                "board": board,
                "score": np.full(
                          shape=(self.board_size, self.board_size),
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

            self.player_data[i]["score"][
                self.player_data[i]["score"] != mask] = True

    def check_for_win(self) -> list[int]:
        """
        Check all the players to see if any have won. If any have one return a
        list of the winning players.
        """

        winners = []

        # For each player in the game
        for i in range(self.players):

            # Check any rows for all True
            row_mask = np.sum(self.player_data[i]["score"], axis=1)

            if self.board_size in row_mask:
                winners.append(i)
                continue

            # Check any cols for all True
            col_mask = np.sum(self.player_data[i]["score"], axis=0)

            if self.board_size in col_mask:
                winners.append(i)
                continue

        return winners

    def calc_final_score(self, player: int) -> int:
        """
        For a winning player sum the un scored numbers.
        """

        # Filter to the non-scored numbers
        non_scored = self.player_data[player]["board"][
            self.player_data[player]["score"] == False]

        return int(np.sum(non_scored))

    def game_of_bingo(self):
        """
        Run a game of bingo.
        """

        # Iterate over each possible call in order
        for call in self.call_numbers:

            # Call the number
            self.call_number(call)

            # Check for a winners
            winners = self.check_for_win()

            if winners:
                break

        # Calculate the score
        win_idx = winners[0]

        board_sum = self.calc_final_score(win_idx)

        print(f"Player {win_idx} won with score = {board_sum * call}")


if __name__ == "__main__":

    # Sample Game
    sample = BingoGame("./data/sample.txt")
    sample.game_of_bingo()
