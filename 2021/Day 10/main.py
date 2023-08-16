"""
--- Day 10: Syntax Scoring ---

The navigation subsystem syntax is made of several lines containing chunks.
There are one or more chunks on each line, and chunks contain zero or more
other chunks. Adjacent chunks are not separated by any delimiter; if one chunk
stops, the next chunk (if any) can immediately start. Every chunk must open and
close with one of four legal pairs of matching characters:

    If a chunk opens with (, it must close with ).
    If a chunk opens with [, it must close with ].
    If a chunk opens with {, it must close with }.
    If a chunk opens with <, it must close with >.

Some lines are incomplete, but others are corrupted. Find and discard the
corrupted lines first.

A corrupted line is one where a chunk closes with the wrong character - that is,
where the characters it opens and closes with do not form one of the four legal
pairs listed above. Some of the lines aren't corrupted, just incomplete; you can
ignore these lines for now.

Part 1:
    Find the first illegal character in each corrupted line of the navigation
    subsystem. What is the total syntax error score for those errors?

Part 2:
    Find the completion string for each incomplete line, score the completion
    strings, and sort the scores. What is the middle score?
"""

open_char = ["(", "[", "{", "<"]
close_char = [")", "]", "}", ">"]
compat_char = dict(zip(close_char, open_char))


def score_errors(corrupted_chars: list[str]) -> int:
    """
    Generate a score for the list of corrupted characters.
    """
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    tot_score = 0

    for sc_char, val in scores.items():
        tot_score += corrupted_chars.count(sc_char) * val

    return tot_score


if __name__ == "__main__":

    # Load the chunk data
    chunk_data = open("./data/input.txt", "r").read().splitlines()

    first_corrupted = []

    for chunk in chunk_data:

        opening_chunks = []
        first_corrupted_char = None

        # Iterate over each character in the chunk
        for char in chunk:

            if char in open_char:
                # Make a record of every new opening chunk
                opening_chunks.append(char)

            elif char in close_char:

                match_char = opening_chunks.pop()

                # Check that the last seen opening chunk is compatible
                if match_char != compat_char[char]:

                    # If there isn't a match the line is corrupted
                    if first_corrupted_char is None:
                        first_corrupted_char = char
                        continue
            else:
                raise Exception(f"'{char}' is not compatible.")

        # Record the first corrupted char
        if first_corrupted_char is not None:
            first_corrupted.append(first_corrupted_char)

    # Solution to part 1
    total_score = score_errors(first_corrupted)
    print(f"Total corrupted character score is: {total_score}")
