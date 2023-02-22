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


def clean_stream(garbage_stream: str) -> str:
    """Remove garbage characters from stream and return a cleaned version."""

    # Define what groups are garbage and what are not
    lgroup = "{"
    rgroup = "}"
    lgarb = "<"
    rgarb = ">"
    cancel = "!"

    cleaned_stream = ""

    # Loop over the stream of text and identify the groups
    i = 0
    in_garb = False

    while i < len(garbage_stream):

        # What is the current character in the stream
        char = garbage_stream[i]

        # Skip the next character if char is the cancel one.
        if char == cancel:
            i += 2
            continue

        # Is the stream in a garbage group
        if char == lgarb:
            in_garb = True

        if char == rgarb:
            in_garb = False

        # Record Groups
        if not in_garb and char in (lgroup, rgroup):
            cleaned_stream += char

        # Move onto the next character in the stream
        i += 1

    return cleaned_stream


print(clean_stream("{{<!>},{<!>},{<!>},{<a>}}"))
