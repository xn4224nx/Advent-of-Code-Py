"""
--- Day 16: Aunt Sue ---

Your Aunt Sue has given you a wonderful gift, and you'd like to send her a
thank you card. However, there's a small problem: she signed it "From, Aunt
Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out which
Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the
gift. You open the present and, as luck would have it, good ol' Aunt Sue got
you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed,
as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few
specific compounds in a given sample, as well as how many distinct kinds of
those compounds there are. According to the instructions, these are what the
MFCSAM can detect:

    -   children, by human DNA age analysis.

    -   cats. It doesn't differentiate individual breeds.

    -   Several seemingly random breeds of dog: samoyeds, pomeranians, akitas,
        and vizslas.

    -   goldfish. No other kinds of fish.

    -   trees, all in one group.

    -   cars, presumably by exhaust or gasoline or something.

    -   perfumes, which is handy, since many of your Aunts Sue wear a few
        kinds.

In fact, many of your Aunts Sue have many of these. You put the wrapping from
the gift into the MFCSAM. It beeps inquisitively at you a few times and then
prints out a message on ticker tape:

    children: 3
    cats: 7
    samoyeds: 2
    pomeranians: 3
    akitas: 0
    vizslas: 0
    goldfish: 5
    trees: 3
    cars: 2
    perfumes: 1

You make a list of the things you can remember about each Aunt Sue. Things
missing from your list aren't zero - you simply don't remember the value.

PART 1: What is the number of the Sue that got you the gift?
"""

import re


def read_aunt_data(data_file: str) -> list[dict[str:int]]:
    """
    Read a data file that contains details about aunts and
    create a structured format.
    """
    all_aunts = []
    re_pat = re.compile(r"([a-z]+): (\d+)")

    with open(data_file) as fp:
        for line in fp.readlines():
            tmp_aunt = {}

            # Find all the properties of each aunt and store them
            for match in re_pat.finditer(line):
                tmp_aunt[match.group(1)] = int(match.group(2))

            # An aunt will be fully described on only one line
            all_aunts.append(tmp_aunt)

    return all_aunts


def is_same_aunt(true_aunt: dict[str:int], pos_aunt: dict[str:int]) -> bool:
    """
    Test to see if two aunts could be the same.
    """
    for chara, val in pos_aunt.items():
        # If the aunts share a characteristic ensure it matches
        # if not they are not the same aunt.
        if chara in true_aunt and true_aunt[chara] != val:
            return False

    return True


def find_matched_aunt(
    aunt_data: list[dict[str:int]], aunt_to_find: dict[str:int]
) -> int:
    """
    Determine the index+1 of the aunt in the `aunt_data` that matches the aunt
    characteristics given in `aunt_to_find`.
    """
    for idx in range(len(aunt_data)):
        if is_same_aunt(aunt_to_find, aunt_data[idx]):
            return idx + 1
    else:
        raise Exception("Matching Aunt not found!")


if __name__ == "__main__":
    pos_aunts = read_aunt_data("./data/input.txt")
    true_aunt = read_aunt_data("./data/p1_aunt.txt")[0]

    print(f"Part 1 = {find_matched_aunt(pos_aunts, true_aunt)}")
