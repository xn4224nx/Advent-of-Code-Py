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

"""

# Load the raw digit data
raw_digits = open("./data/input.txt").read().splitlines()

# Parse the digit data
digits = []
digit_len_cnt = {x: 0 for x in range(10)}

for line in raw_digits:

    # Extract the signal digits and the output digits
    signals, outputs = line.split("|")

    # Save the parsed and cleaned digit data
    digits.append({
            "signals": [x.strip() for x in signals.split()],
            "outputs": [x.strip() for x in outputs.split()],
    })

    # Count the frequency of output digit lengths
    for digi in digits[-1]["outputs"]:
        digit_len_cnt[len(digi)] += 1

cnt_1_4_7_8 = (digit_len_cnt[2] + digit_len_cnt[4] +
               digit_len_cnt[3] + digit_len_cnt[7])

print(f"The answer to part 1: {cnt_1_4_7_8}")
