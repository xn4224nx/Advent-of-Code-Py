"""
--- Day 10: Balance Bots ---

You come upon a factory in which many robots are zooming around handing small
microchips to each other.

Upon closer examination, you notice that each bot only proceeds when it has two
microchips, and once it does, it gives each one to a different bot or puts it
in a marked "output" bin. Sometimes, bots take microchips from "input" bins,
too.

Inspecting one of the microchips, it seems like they each contain a single
number; the bots must use some logic to decide what to do with each chip. You
access the local control computer and download the bots' instructions (your
puzzle input).

Some of the instructions specify that a specific-valued microchip should be
given to a specific bot; the rest of the instructions indicate what a given bot
should do with its lower-value or higher-value chip.

PART 1: Based on your instructions, what is the number of the bot that is
        responsible for comparing value-61 microchips with value-17 microchips?
"""


class BalanceBots:
    def __init__(self, instruc_file: str):
        pass

    def send_val_to_bot(self, val: int, bot: int):
        pass

    def balance_move(
        self,
        src_bot: int,
        low_dest_bot: bool,
        low_dest: int,
        high_dest_bot: bool,
        high_dest: int,
    ):
        pass

    def find_comp_bot(self, val_0: int, val_1: int) -> int:
        pass

    def execute_all_insrucs(self):
        pass


if __name__ == "__main__":
    pass
