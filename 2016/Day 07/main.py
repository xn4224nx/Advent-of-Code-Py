"""
--- Day 7: Internet Protocol Version 7 ---

An ABBA is any four-character sequence which consists of a pair of two
different characters followed by the reverse of that pair, such as xyyx or
abba.

However, the IP also must not have an ABBA within any hypernet sequences,
which are contained by square brackets.

How many IPs in your puzzle input support TLS?
"""

import re


def is_palindrome(text_str: str, abba: bool) -> bool:
    """Check if a string is a palindrome."""

    # Make sure that the interior characters are different
    if abba and text_str[0] == text_str[1]:
        return False

    # Loop over the first part of the string
    for i in range(0, len(text_str)//2):

        # check if the ith char == the -i character
        if text_str[i] != text_str[len(text_str)-1-i]:
            return False
    else:
        return True


def str_generator(text_str: str, window: int):
    """Generator to give the window size of the `text_str`."""

    for i in range(len(text_str) - window + 1):
        yield text_str[i:i+window]


def is_tls_isp(ip_tuple: tuple) -> bool:
    """Check if an isp address is compliant."""

    # Check the bad parts
    for string in ip_tuple[1]:
        if any([is_palindrome(x, True) for x in str_generator(string, 4)]):
            return False

    # Check the good parts
    for string in ip_tuple[0]:
        if any([is_palindrome(x, True) for x in str_generator(string, 4)]):
            return True
    else:
        return False


def is_ssl_isp(ip_tuple: tuple) -> bool:
    """Is an ISP SSL compliant."""

    # Find all the ABA
    aba_arr = []
    for string in ip_tuple[0]:
        for sub_str in str_generator(string, 3):
            if is_palindrome(sub_str, True):
                aba_arr.append(sub_str)
    else:
        # If the array is empty it's not compliant
        if not aba_arr:
            return False

    # Find all the BAB
    bab_arr = []
    for string in ip_tuple[1]:
        for sub_str in str_generator(string, 3):
            if is_palindrome(sub_str, True):
                bab_arr.append(sub_str)
    else:
        # If the array is empty it's not compliant
        if not bab_arr:
            return False

    # Flip the found ABA strings
    for i in range(len(aba_arr)):
        aba_arr[i] = aba_arr[i][1] + aba_arr[i][0] + aba_arr[i][1]

    # See if the ABA and BAB have common elements
    for str_1 in aba_arr:
        if str_1 in bab_arr:
            return True
    else:
        return False


# Load the data from disk
data = open("data/input.txt").read().splitlines()

# Parse the data into the separate parts

# Extract the parts that should and shouldn't contain palindromes
good_data = [re.findall(r"[a-z]+\[|\][a-z]+", x) for x in data]
bad_data = [re.findall(r"\[([a-z]+)", x) for x in data]

# Clear unwanted characters
good_data = [[y.replace("[", "").replace("]", "")
              for y in x] for x in good_data]

tls_valid_ips = 0
ssl_valid_ips = 0

# Detect if an ISP address will support TSP
for ip_address in zip(good_data, bad_data):
    if is_tls_isp(ip_address):
        tls_valid_ips += 1

    if is_ssl_isp(ip_address):
        ssl_valid_ips += 1

# Part 1
print(tls_valid_ips)

# Part 2
print(ssl_valid_ips)
