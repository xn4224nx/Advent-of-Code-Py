r"""
--- Day 8: Matchsticks ---

Space on the sleigh is limited this year, and so Santa
will be bringing his list as a digital copy. He needs
to know how much space it will take up when stored.

It is common in many programming languages to provide
a way to escape special characters in strings. For
example, C, JavaScript, Perl, Python, and even PHP
handle special characters in very similar ways.

However, it is important to realize the difference
between the number of characters in the code
representation of the string literal and the number
of characters in the in-memory string itself.

Santa's list is a file that contains many double-
quoted string literals, one on each line. The only
escape sequences used are \\ (which represents a
single backslash), \" (which represents a lone
double-quote character), and \x plus two
hexadecimal characters (which represents a single
character with that ASCII code).

PART 1: Disregarding the whitespace in the file, what
        is the number of characters of code for
        string literals minus the number of
        characters in memory for the values of the
        strings in total for the entire file?

Now, let's go the other way. In addition to finding
the number of characters of code, you should now
encode each code representation as a new string and
find the number of characters of the new encoded
representation, including the surrounding double
quotes.

PART 2: Your task is to find the total number of
        characters to represent the newly encoded
        strings minus the number of characters of
        code in each original string literal.
"""

import ast
import re


def read_nn_list(file_path: str) -> list[str]:
    """
    Read Santa's naughtly and nice list from file and
    return a list of strings representing each line
    of the file.
    """
    nn = []

    with open(file_path) as fp:
        for line in fp:
            nn.append(line.strip())

    return nn


def count_raw_char(f_input: str) -> int:
    """
    Count the characters in the input string
    `f_input` that are in memory.
    """
    return len(f_input)


def count_literal_char(f_input: str) -> int:
    """
    Determine the number of characters for the
    literal string `f_input`
    """
    return len(ast.literal_eval(f_input))


def count_encoded_char(f_input: str) -> int:
    """
    Encode the string as a new representation and
    return its length.
    """
    enc_char = len(f_input) + 2  # For quoting
    enc_char += f_input.count("\\")
    enc_char += f_input.count('"')

    return enc_char


def char_deficit(file_path: str, char_deficit: bool) -> int:
    """
    Ignoring the whitespace in the file, what is
    the number of characters of code for string
    literals minus the number of characters in memory
    for the values of the strings in total for the
    entire file?
    """
    l_sum = c_sum = e_sum = 0

    for line in read_nn_list(file_path):
        c_sum += count_raw_char(line)
        l_sum += count_literal_char(line)
        e_sum += count_encoded_char(line)

    if char_deficit:
        return c_sum - l_sum
    else:
        return e_sum - c_sum


if __name__ == "__main__":
    print(f"Part 1 = {char_deficit('./data/input.txt', True)}")
    print(f"Part 2 = {char_deficit('./data/input.txt', False)}")
