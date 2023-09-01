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
"""


class Polymer:

    def __init__(self, data_file_path: str):

        self.template = ""
        self.chain = ""
        self.insert_rules = {}

        # Load the raw datafile and parse
        for idx, line in enumerate(open(data_file_path).read().splitlines()):

            # Get the template
            if idx == 0:
                self.template = line
                self.chain = line

            # Collect pair insertion rules
            if "->" in line:
                pair, element = line.split(" -> ")
                self.insert_rules[pair] = element

    def process_chain_once(self):
        """
        Using the pair insertion rules in the `self.insert_rules` dict inset
        pairs of values in `self.chain`.
        """
        pass

    def element_freq_range(self) -> int:
        """
        Return the difference between the most and least frequent element in the
        polymer chain.
        """
        pass


sample_poly = Polymer("./data/sample.txt")
