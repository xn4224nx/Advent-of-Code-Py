"""
--- Day 7: Recursive Circus ---

For example, if your list is the following:

pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)


...then you would be able to recreate the structure of the towers that looks
like this:

                gyxo
              /
         ugml - ebii
       /      \
      |         jptl
      |
      |         pbga
     /        /
tknk --- padx - havc
     \        \
      |         qoyq
      |
      |         ktlj
       \      /
         fwft - cntj
              \
                xhth

In this example, tknk is at the bottom of the tower (the bottom program), and
is holding up ugml, padx, and fwft. Those programs are, in turn, holding up
other programs; in this example, none of those programs are holding up any
other programs, and are all the tops of their own towers. (The actual tower
balancing in front of you is much larger.)

Part 1

Before you're ready to help them, you need to make sure your information is
correct. What is the name of the bottom program?

Part 2

Each of those sub-towers are supposed to be the same weight, or the disc itself
isn't balanced. The weight of a tower is the sum of the weights of the programs
in that tower.

Given that exactly one program is the wrong weight, what would its weight need
to be to balance the entire tower?
"""

import re


def load_prog_record(fp: str) -> dict[dict]:
    """Load the recursive data and parse into a dict."""

    ret_dict = {}

    pat_name_weight = r"([a-zA-Z]+) \(([0-9]+)\)"

    with open(fp, "r") as file:
        for line in file:

            # Extract the name and weight of the program
            prog_details = re.search(pat_name_weight, line)

            # Detect if this program has programs above it and extract the
            # names of them.
            if "->" in line:
                above_progs = re.findall("[a-z]+", line.split("->")[1])
            else:
                above_progs = []

            ret_dict[prog_details.group(1)] = {
                "Weight": int(prog_details.group(2)),
                "Above": above_progs
            }

    return ret_dict


def find_lowest_prog(program_record: dict[dict]) -> str:
    """Find the lowest root program in the program record."""

    progs_supported = []
    root_progs = []

    # Loop over the dict
    for prog_name, prog_details in program_record.items():

        # Only examine programs that support other programs
        if prog_details["Above"]:
            root_progs.append(prog_name)
            progs_supported += prog_details["Above"]

    # Check to see which programs that support other programs are not supported
    # themselves, that should be the root program.
    lowest_prog = [x for x in root_progs if x not in progs_supported]

    return lowest_prog[0]


def calc_above_weight(program_record: dict[dict]) -> None:
    """
    Calculates the variable `Above Weight` that is the sum of program weights
    of all programs above this program to the program record dict.
    """

    uncalc_progs = []

    # If the program has nothing above it set the above weight to zero
    for prog_name, prog_details in program_record.items():
        if not prog_details["Above"]:
            program_record[prog_name]["Above Weight"] = \
                program_record[prog_name]["Weight"]
        else:
            program_record[prog_name]["Above Weight"] = None
            uncalc_progs.append(prog_name)

    # Calculate the above weights for the lower programs
    while uncalc_progs:

        for prog_name in uncalc_progs[:]:

            prog_sum = program_record[prog_name]["Weight"]

            # Check if the above weights have been calculated for this program
            for sub_prog in program_record[prog_name]["Above"]:

                if program_record[sub_prog]["Above Weight"] is not None:
                    prog_sum += program_record[sub_prog]["Above Weight"]
                else:
                    # End the sub loop if not all the programs above it have
                    # been calculated yet.
                    prog_sum = None
                    break

            # If the above weight has been successfully calculated
            if prog_sum is not None:
                uncalc_progs.remove(prog_name)
                program_record[prog_name]["Above Weight"] = prog_sum


def find_imbalances(program_record: dict[dict]) -> int:
    """
    Find the imbalance in the program weight and return what the new weight
    of the item should be.
    """

    for prog_name, prog_details in program_record.items():

        # Skip programs with nothing above them
        if not prog_details["Above"]:
            continue

        # Extract the weights of the program above it
        above_prog_weights = [program_record[x]["Above Weight"]
                              for x in prog_details["Above"]]

        # Check they are all balanced
        if len(set(above_prog_weights)) == 1:
            continue

        # The unbalanced weight is the least frequent one
        unbalanced_weight = min(set(above_prog_weights),
                              key=above_prog_weights.count)

        unbalanced_prog_name = prog_details["Above"][
            above_prog_weights.index(unbalanced_weight)]

        change_needed = max(set(above_prog_weights),
                            key=above_prog_weights.count) - unbalanced_weight
        break

    # Return the sum of  unbalanced programs weight and the change_needed

    return program_record[unbalanced_prog_name]["Weight"] + change_needed


rec_data = load_prog_record("data/input.txt")

# Part 1
print(find_lowest_prog(rec_data))

# Part 2
calc_above_weight(rec_data)
print(find_imbalances(rec_data))
