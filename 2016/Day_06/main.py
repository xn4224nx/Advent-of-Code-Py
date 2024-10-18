"""
--- Day 6: Signals and Noise ---

Something is jamming your communications with Santa. Fortunately, your signal is
only partially jammed, and protocol in situations like this is to switch to a
simple repetition code to get the message through.

In this model, the same message is sent repeatedly. You've recorded the
repeating message signal (your puzzle input), but the data seems quite corrupted
- almost too badly to recover. Almost.

All you need to do is figure out which character is most frequent for each
position.

PART 1: Given the recording in your puzzle input, what is the error-corrected
        version of the message being sent?
"""

import numpy as np


def read_signal_data(file_path: str) -> np.array:
    """
    Load the corrupted signal data into a 2D numpy array of characters.
    """
    pass


def find_vert_msg(signals: np.array) -> str:
    """
    For each column find the modal character and return them all as a
    concaternated string.
    """
    pass


if __name__ == "__main__":
    pass
