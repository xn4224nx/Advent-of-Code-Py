"""
--- Day 9: Stream Processing ---

The characters represent groups - sequences that begin with { and end with }.
Within a group, there are zero or more other things, separated by commas: either
another group or garbage. Since groups can contain other groups, a } only closes
the most-recently-opened unclosed group - that is, they are nestable. Your
puzzle input represents a single, large group which itself contains many
smaller ones.

Sometimes, instead of a group, you will find garbage. Garbage begins with < and
ends with >. Between those angle brackets, almost any character can appear,
including { and }. Within garbage, < has no special meaning.

In a futile attempt to clean up the garbage, some program has canceled some of
the characters within it using !: inside garbage, any character that comes after
! should be ignored, including <, >, and even another !.

Part 1
What is the total score for all groups in your input?
"""

# Define what groups are garbage and what are not
lgroup = "{"
rgroup = "}"
lgarb = "<"
rgarb = ">"
cancel = "!"


def stream_score(garbage_stream: str, non_canceled=False) -> int:
    """What is the score of a stream of garbage characters."""

    # Loop over the stream of text and identify the groups
    i = 0
    in_garb = False
    curr_score = 0
    score_total = 0
    canceled_chars = 0
    stack = []

    while i < len(garbage_stream):

        # What is the current character in the stream
        char = garbage_stream[i]

        # Skip the next character if char is the cancel one.
        if char == cancel:
            i += 1

        # Is the stream in a garbage group
        elif in_garb:
            if char == rgarb:
                in_garb = False
            else:
                canceled_chars += 1

        # Each new group down causes the score to go up
        elif char == lgroup:
            curr_score += 1
            stack.append(curr_score)

        # If garbage starts
        elif char == lgarb:
            in_garb = True

        # When a group ends add the current score to the total
        elif char == rgroup:
            curr_score -= 1
            score_total += stack.pop()

        # Move onto the next character in the stream
        i += 1

    if non_canceled:
        return canceled_chars
    else:
        return score_total


stream = open("data/input.txt", "r").read()

# Part 1
print(stream_score(stream))

# Part 2
print(stream_score(stream, True))