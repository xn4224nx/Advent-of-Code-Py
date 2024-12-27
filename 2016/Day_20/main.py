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
        pass

    def blacklist_range(self, blck_range: (int, int)):
        """
        Modify the current allowed list of IPs blocking all the IP addresses
        specified in the aforementioned range.
        """
        pass

    def blacklist_all_ranges(self):
        """
        Using the supplied datafile backlist all the ranges specified in it.
        """
        pass

    def lowest_allowed_address(self) -> int:
        """
        Find the lowest unblocked IP address in the firewall currently.
        """
        pass


if __name__ == "__main__":
    pass
