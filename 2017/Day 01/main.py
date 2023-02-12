"""
--- Day 1: Inverse Captcha ---

It goes on to explain that you may only leave by solving a captcha to prove
you're not a human.

The captcha requires you to review a sequence of digits (your puzzle input) and
find the sum of all digits that match the next digit in the list. The list is
circular, so the digit after the last digit is the first digit in the list.
"""


def load_data(fp):
    """Load the data from disk and return array of digits."""

    data = open(fp).read().strip()
    return [int(x) for x in data]


def rev_captcha(num_ls, halfway=False):
    """
    Sums the digits that are the same as the next one in the sequence.

    Halfway means that only digits that match the one len(num_ls)/2 away will
    be included.
    """

    ls_sum = 0

    if halfway:
        shift = len(num_ls)//2
    else:
        shift = 1

    for i in range(len(num_ls)):

        # What digit should this one be compared to?
        comp_idx = (i + shift) % len(num_ls)

        if num_ls[i] == num_ls[comp_idx]:
            ls_sum += num_ls[i]

    return ls_sum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    number = load_data("data/input.txt")

    # Loop over the digits and sum any that are the same as the next one
    print(rev_captcha(number))

    # Loop over the digits and sum any that are the same as half the list len
    print(rev_captcha(number, True))
