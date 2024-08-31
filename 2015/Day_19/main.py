"""
--- Day 19: Medicine for Rudolph ---

Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly,
and he needs medicine.

Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph
is going to need custom-made medicine. Unfortunately, Red-Nosed Reindeer
chemistry isn't similar to regular reindeer chemistry, either.

The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission
plant, capable of constructing any Red-Nosed Reindeer molecule you need. It
works by starting with some input molecule and then doing a series of
replacements, one per step, until it has the right molecule.

However, the machine has to be calibrated before it can be used. Calibration
involves determining the number of molecules that can be generated in one step
from a given starting point.

The machine replaces without regard for the surrounding characters. For
example, given the string H2O, the transition H => OO would result in OO2O.

Your puzzle input describes all of the possible replacements and, at the
bottom, the medicine molecule for which you need to calibrate the machine.

PART 1: How many distinct molecules can be created after all the different ways
        you can do one replacement on the medicine molecule?
"""

import re


def read_machine_data(data_file: str) -> tuple[list[tuple[str, str]], str]:
    """
    Read the machine instruction data and return a list of transformations and
    the starting chemical.
    """
    instr = []

    with open(data_file) as fp:
        for line in fp.readlines():
            line = line.strip()

            # Extract instruction
            if " => " in line:
                instr.append(tuple(line.split(" => ", 1)))

            elif line.strip() == "":
                continue

            else:
                chem = line

    return (instr, chem)


def find_one_instr_molec(instr: tuple[str, str], chem: str) -> list[str]:
    """
    Find the possible chemicals that can be made from a single molecules
    replacement using one instruction on each molecule once.
    """
    all_chems = []

    # Find all the positions of the parts that will be replaced and concat
    for mtc in re.finditer(instr[0], chem):
        new_chem = chem[: mtc.start(0)] + instr[1] + chem[mtc.end(0) :]
        all_chems.append(new_chem)

    return all_chems


def find_all_possible_chems(all_instr: list[tuple[str, str]], chem: str) -> int:
    """
    Determine the number of possible chemicals that can be created from a set
    of molecule replacement instructions.
    """
    possible_chems = set()

    for instr in all_instr:
        possible_chems.update(find_one_instr_molec(instr, chem))

    return len(possible_chems)


if __name__ == "__main__":
    pass
