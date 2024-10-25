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

import re


class BalanceBots:
    def __init__(self, instruc_file: str):
        """
        Load the instructions, parse the instructions and initialise the parts
        of the Balance Bot factory.
        """
        self.bots = []
        self.outputs = []
        self.instrucs = []

        val_pat = re.compile(r"value ([0-9]+) goes to bot ([0-9]+)")
        bmv_pat = re.compile(
            r"bot ([0-9]+) gives low to (bot|output) "
            r"([0-9]+) and high to (bot|output) ([0-9]+)"
        )

        # Parse the file if it is provided
        if instruc_file != "":
            max_bot = 0
            max_output = 0

            with open(instruc_file, "r") as fp:
                for line in fp.readlines():
                    line_data = val_pat.match(line)

                    # Bot assignment instruction
                    if line_data is not None:
                        bot = int(line_data.group(2))
                        val = int(line_data.group(1))

                        # Save the instruction
                        self.instrucs.append(
                            {
                                "type": "send-val",
                                "val": val,
                                "bot": bot,
                            }
                        )

                        # Check if a larger bot index has been found
                        if bot > max_bot:
                            max_bot = bot

                        continue

                    line_data = bmv_pat.match(line)

                    # A balance move instruction
                    if line_data is not None:
                        src_bot = int(line_data.group(1))
                        low_dest = int(line_data.group(3))
                        high_dest = int(line_data.group(5))
                        is_low_bot = line_data.group(2) == "bot"
                        is_high_bot = line_data.group(4) == "bot"

                        # Save the instruction
                        self.instrucs.append(
                            {
                                "type": "bal-mov",
                                "src-bot": src_bot,
                                "low-bot": is_low_bot,
                                "low-dest": low_dest,
                                "high-bot": is_high_bot,
                                "high-dest": high_dest,
                            }
                        )

                        # Check for greater bot or output indexes
                        if is_low_bot and low_dest > max_bot:
                            max_bot = low_dest
                        elif low_dest > max_output:
                            max_output = low_dest

                        if is_high_bot and high_dest > max_bot:
                            max_bot = high_dest
                        elif high_dest > max_output:
                            max_output = high_dest

                        continue

                    raise Exception(f"Line '{line}' could not be parsed!")

            # Define the bots and outputs as empty
            self.bots = [[] for _ in range(max_bot)]
            self.outputs = [[] for _ in range(max_output)]

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
