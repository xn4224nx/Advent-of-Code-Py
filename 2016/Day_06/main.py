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
    with open(file_path) as fp:
        raw_signal = [line.strip() for line in fp.readlines()]

    # Parse each line as an array of characters
    return np.array(list(map(list, raw_signal)))


def find_vert_msg(signals: np.array) -> str:
    """
    For each column find the modal character and return them all as a
    concaternated string.
    """
    msg = []

    # Iterate over every column in the signals
    for col_idx in range(signals.shape[1]):
        vals, counts = np.unique(signals[:, col_idx], return_counts=True)

        # Save the modal character for this column
        msg.append(vals[np.argmax(counts)])

    # Assemble the resulting message
    return "".join(msg)


if __name__ == "__main__":
    sig = read_signal_data("./data/input.txt")
    print(f"Part 1 = {find_vert_msg(sig)}")
