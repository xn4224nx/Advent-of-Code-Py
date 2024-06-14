"""
--- Day 11: Corporate Policy ---

Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires,
Santa has devised a method of coming up with a password based on the previous
one. Corporate policy dictates that passwords must be exactly eight lowercase
letters (for security reasons), so he finds his new password by incrementing
his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on.
Increase the rightmost letter one step; if it was z, it wraps around to a, and
repeat with the next letter to the left until one doesn't wrap around.
"""

from collections import deque
import itertools


def increment_str(input_str) -> str:
    """Increment a letter string by one."""

    # Convert each letter to its number equivalent a=0, z=25
    number = deque([ord(x) - ord('a') for x in input_str])

    # Increment the last number in the array
    number[-1] += 1

    # Check for the number being greater than 25
    for i in range(len(number) - 1, -1, -1):

        # If a number is outside the range
        if number[i] > 25:

            # Set the number to what it should be
            number[i] = 0

            # If the number just changed was the first
            if i == 0:
                # Add a new number to the start of the array
                number.appendleft(1)

            else:
                # increment the number left of the current
                number[i - 1] += 1

    # Convert the numbers back to a string of letters
    new_number = []

    for digit in number:
        new_number.append(chr(digit + ord('a')))

    # Return a string of the new number created
    return "".join(new_number)


def password_check(input_str) -> bool:
    """Validate the password fits the rules"""

    # Rule 1 - include one increasing straight of at least three letters
    increasing_count = 0

    for i in range(1, len(input_str)):

        # Check if the previous string is one smaller than the current
        if ord(input_str[i]) == ord(input_str[i-1]) + 1:
            increasing_count += 1
        else:
            increasing_count = 0

        # Break the loop if the condition is ever met
        if increasing_count >= 2:
            break

    else:
        # If it gets to this point return false as it has failed this rule
        return False

    # Rule 2 - Passwords cannot contain i, o or l
    if "i" in input_str or "o" in input_str or "l" in input_str:
        return False

    # Rule 3 - Passwords must contain at least two different,
    # non-overlapping pairs of letters, like aa, bb, or zz.

    # Get an array of the lengths of repeated character in the string
    split_str = [len("".join(g)) for k, g in itertools.groupby(input_str)]

    # Remove 1 from the array
    split_str = [x for x in split_str if x > 1]

    # Return true if there are more than one group of repeated letters
    if len(split_str) > 1:
        return True
    else:
        return False


start_str = "cqjxxyzz"

start_str = increment_str(start_str)

# Test the password is valid
while not password_check(start_str):

    # If not increment it
    start_str = increment_str(start_str)

# Show the password that passes the check
print(start_str)
