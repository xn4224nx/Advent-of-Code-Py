"""
--- Day 14: Extended Polymerization ---

The submarine manual contains instructions for finding the optimal polymer
formula; specifically, it offers a polymer template and a list of pair insertion
rules (your puzzle input). You just need to work out what polymer would result
after repeating the pair insertion process a few times.

The first line is the polymer template - this is the starting point of the
process. The following section defines the pair insertion rules.

Part 1:
    Apply 10 steps of pair insertion to the polymer template and find the most
    and least common elements in the result. What do you get if you take the
    quantity of the most common element and subtract the quantity of the least
    common element?

Part 2:
    Apply 40 steps of pair insertion to the polymer template and find the most
    and least common elements in the result. What do you get if you take the
    quantity of the most common element and subtract the quantity of the least
    common element?
"""

from collections import Counter


class Polymer:

    def __init__(self, data_file_path: str):

        self.raw_template = ""
        self.template = {}
        self.insert_rules = {}
        self.letter_freq = {}

        # Load the raw datafile and parse
        for idx, line in enumerate(open(data_file_path).read().splitlines()):

            # Get the template
            if idx == 0:
                self.raw_template = line

            # Collect pair insertion rules
            if "->" in line:
                pair, element = line.split(" -> ")
                self.insert_rules[pair] = element

        # Determine the pairs in the original polymer template
        for idx in range(len(self.raw_template)-1):

            # Determine the current pair
            curr_pair = self.raw_template[idx:idx+2]

            # Create a dict of the pair frequency
            if curr_pair not in self.template:
                self.template[curr_pair] = 1
            else:
                self.template[curr_pair] += 1

        # Create the letter frequency dictionary
        for char in self.raw_template:
            if char not in self.letter_freq:
                self.letter_freq[char] = 1
            else:
                self.letter_freq[char] += 1

    def process_chain_once(self):
        """
        Using the pair insertion rules in the `self.insert_rules` dict inset
        pairs of values in `self.chain`.
        """

        new_chain = self.template.copy()

        for pair, ele in self.insert_rules.items():

            # If the pair is in the template, pairs in the template will change
            if pair in self.template and self.template[pair] > 0:

                # Create the new pairs
                left = pair[0] + ele
                right = ele + pair[1]

                # Create the keys if they don't exist
                new_chain.setdefault(pair, 0)
                new_chain.setdefault(left, 0)
                new_chain.setdefault(right, 0)
                self.letter_freq.setdefault(ele, 0)

                # Get the current pair count
                pair_cnt = self.template[pair]

                # Remove the pair that will split
                new_chain[pair] -= pair_cnt

                # Add in the new pairs
                new_chain[left] += pair_cnt
                new_chain[right] += pair_cnt

                # Add in the new letters
                self.letter_freq[ele] += pair_cnt

        # Remove zero or negative counts
        new_chain = {pair: cnt for pair, cnt in new_chain.items() if cnt > 0}

        self.template = new_chain

    def element_freq_range(self) -> int:
        """
        Return the difference between the most and least frequent element in the
        polymer chain.
        """

        # Count the elements in the chain
        ele_freq = Counter(self.letter_freq).most_common()

        return ele_freq[0][1] - ele_freq[-1][1]


if __name__ == "__main__":

    poly = Polymer("./data/input.txt")

    for _ in range(10):
        poly.process_chain_once()

    print(f"The answer to part one is : {poly.element_freq_range()}")

    for _ in range(30):
        poly.process_chain_once()

    print(f"The answer to part two is : {poly.element_freq_range()}")
