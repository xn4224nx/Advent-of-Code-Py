"""
--- Day 8: Seven Segment Search ---

Each digit of a seven-segment display is rendered by turning on or off any of
seven segments named a through g.

The problem is that the signals which control the segments have been mixed up on
each display. The submarine is still trying to display numbers by producing
output on signal wires a through g, but those wires are connected to segments
randomly. Worse, the wire/segment connections are mixed up separately for each
four-digit display! (All of the digits within a display use the same
connections, though.)

For each display, you watch the changing signals for a while, make a note of all
ten unique signal patterns you see, and then write down a single four digit
output value (your puzzle input). Using the signal patterns, you should be able
to work out which pattern corresponds to which digit.

Using this information, you should be able to work out which combination of
signal wires corresponds to each of the ten digits. Then, you can decode the
four digit output value.

Because the digits 1, 4, 7, and 8 each use a unique number of segments, you
should be able to tell which combinations of signals correspond to those digits.

Part 1:
    In the output values, how many times do digits 1, 4, 7, or 8 appear?

Part 2:
    What do you get if you add up all of the output values?
"""


def sort_str(unordered: str) -> str:
    """
    Sort the letters in a string and return it
    """
    # Turn it into an ordered list
    unordered = sorted(unordered)

    # Transform it back into a string and return it
    return "".join(unordered)


def some_char_in_str(container: str, sub: str, count: int = None) -> bool:
    """
    Test if all the `count` of the chars in `sub` are all in `container`
    """

    char_cnt = 0

    if count is None:
        count = len(sub)

    for char in sub:
        if char in container:
            char_cnt += 1

    if char_cnt >= count:
        return True
    else:
        return False


def parse_digit_codes(digit_signal: list[str]) -> dict[str: str]:
    """
    Using a list of digit strings determine what digit refers to each code.
    """

    # Order the chars in the code
    digit_signal= [sort_str(x) for x in digit_signal]

    # Return Dictionary
    digits = {x: None for x in digit_signal}

    # Sort the digits due to length
    len_5_digi = []
    len_6_digi = []

    # Pick out the digits with unique length and sort the others
    for code in digit_signal:

        if len(code) == 2:
            digits[code] = "1"
            one_code = code

        elif len(code) == 4:
            digits[code] = "4"
            four_code = code

        elif len(code) == 3:
            digits[code] = "7"
            seven_code = code

        elif len(code) == 7:
            digits[code] = "8"

        elif len(code) == 5:
            len_5_digi.append(code)

        elif len(code) == 6:
            len_6_digi.append(code)

        else:
            raise Exception("Unknown digit encountered.")

    # Distinguish the 6 cell digits
    for code in len_6_digi:
        if some_char_in_str(code, four_code):
            digits[code] = "9"

        elif some_char_in_str(code, seven_code):
            digits[code] = "0"

        else:
            digits[code] = "6"

    # Distinguish the 5 cell digits
    for code in len_5_digi:
        if some_char_in_str(code, one_code):
            digits[code] = "3"

        elif some_char_in_str(code, four_code, 3):
            digits[code] = "5"

        else:
            digits[code] = "2"

    # Ensure all the digits have been identified
    assert(None not in digits.values())

    # Return a dict of digits lookups
    return digits


def lookup_output_digits(
        digit_lookup: dict[str: str], digit_output: list[str]) -> int:
    """
    Use a code lookup to decode the digit output.
    """

    output = "".join([digit_lookup[sort_str(x)] for x in digit_output])
    return int(output)


if __name__ == "__main__":

    raw_digits = open("./data/input.txt").read().splitlines()

    cnt_1_4_7_8 = 0
    all_outputs = []

    for line in raw_digits:

        # Extract the signal digits and the output digits
        signals, outputs = line.split("|")

        # Split the signal & output strings into lists
        signals = [x.strip() for x in signals.split()]
        outputs = [x.strip() for x in outputs.split()]

        # Work out the code for each digit
        digit_lookup = parse_digit_codes(signals)

        # Use the lookup to de-encode the output number
        out_num = lookup_output_digits(digit_lookup, outputs)
        all_outputs.append(out_num)

        # Count the occurrence of 1, 4, 7, 8 in the output digits
        for num in [1, 4, 7, 8]:
            cnt_1_4_7_8 += str(out_num).count(str(num))

    print(f"The answer to part 1: {cnt_1_4_7_8}")
    print(f"The answer to part 2: {sum(all_outputs)}")
