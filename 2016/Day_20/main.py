"""
--- Day 20: Firewall Rules ---

You'd like to set up a small hidden computer here so you can use it to get back
into the network later. However, the corporate firewall only allows
communication with certain external IP addresses.

You've retrieved the list of blocked IPs from the firewall, but the list seems
to be messy and poorly maintained, and it's not clear which IPs are allowed.
Also, rather than being written in dot-decimal notation, they are written as
plain 32-bit integers, which can have any value from 0 through 4294967295,
inclusive.

For example, suppose only the values 0 through 9 were valid, and that you
retrieved the following blacklist:

5-8
0-2
4-7

The blacklist specifies ranges of IPs (inclusive of both the start and end
value) that are not allowed. Then, the only IPs that this firewall allows are 3
and 9, since those are the only numbers not in any range.

PART 1: Given the list of blocked IPs you retrieved from the firewall (your
        puzzle input), what is the lowest-valued IP that is not blocked?
"""


class Firewall:
    def __init__(self, datafile, allowed_rng: (int, int)):
        """
        Parse the rules from disk and contain them in structured format.
        """
        self.allowed_rng = allowed_rng
        self.rules = []

        if datafile != "":
            with open(datafile) as fp:
                for line in fp.readlines():
                    num1, num2 = line.split("-")

                    nums = [int(num1), int(num2)]
                    low = min(nums)
                    hig = max(nums)

                    # Check the numbers are valid and overwrite if not
                    if low < self.allowed_rng[0]:
                        low = self.allowed_rng[0]

                    if hig > self.allowed_rng[1]:
                        hig = self.allowed_rng[1]

                    self.rules.append((low, hig))

            # Sort the rules
            self.rules.sort()

    def lowest_allowed_address(self) -> int:
        """
        Find the lowest unblocked IP address in the firewall currently.
        """
        min_ip = 0

        # Find the first rule to allow the current min_ip
        for rl_idx in range(len(self.rules)):
            low, high = self.rules[rl_idx]

            if low <= min_ip <= high:
                min_ip = high + 1

        return min_ip


if __name__ == "__main__":
    obs_comp = Firewall("./data/input.txt", (0, 4294967295))
    print(f"Part 1 = {obs_comp.lowest_allowed_address()}")
