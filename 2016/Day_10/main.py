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
        self.max_bot = None
        self.outputs = None

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
                        elif not is_low_bot and low_dest > max_output:
                            max_output = low_dest

                        if is_high_bot and high_dest > max_bot:
                            max_bot = high_dest
                        elif not is_high_bot and high_dest > max_output:
                            max_output = high_dest

                        continue

                    raise Exception(f"Line '{line}' could not be parsed!")

            # Save the maximums found
            self.max_bot = max_bot
            self.max_output = max_output

    def send_val_to_bot(self, val: int, bot: int):
        """
        Assign a value to a specific bot.
        """
        self.bots[bot].append(val)

    def balance_move(
        self,
        src_bot: int,
        low_dest_bot: bool,
        low_dest: int,
        high_dest_bot: bool,
        high_dest: int,
    ):
        """
        Move the two numbers from a bot, the highest to one destination
        and the lowest to another.
        """
        if len(self.bots[src_bot]) != 2:
            return

        val_0 = self.bots[src_bot][0]
        val_1 = self.bots[src_bot][1]

        # If the first is the smallest
        if val_0 < val_1:
            if low_dest_bot:
                self.bots[low_dest].append(val_0)
            else:
                self.outputs[low_dest].append(val_0)

            if high_dest_bot:
                self.bots[high_dest].append(val_1)
            else:
                self.outputs[high_dest].append(val_1)

        # Otherwise the second is smaller
        else:
            if low_dest_bot:
                self.bots[low_dest].append(val_1)
            else:
                self.outputs[low_dest].append(val_1)

            if high_dest_bot:
                self.bots[high_dest].append(val_0)
            else:
                self.outputs[high_dest].append(val_0)

        # Clear the source bot of its values
        self.bots[src_bot] = []

    def find_comp_bot(self, val_0: int, val_1: int) -> int:
        """
        Execute all the instructions and find the number of the bot that
        is responsible for comparing the two values; val_0 and val_1.
        """
        # Define the bots and outputs as empty
        self.bots = [[] for _ in range(self.max_bot + 1)]
        self.outputs = [[] for _ in range(self.max_output + 1)]

        # Keep a record of the instructions that have been used
        used_instr = [False for _ in range(len(self.instrucs))]

        # Execute the assignment instructions
        for idx, instr in enumerate(self.instrucs):
            if instr["type"] == "send-val":
                self.send_val_to_bot(instr["val"], instr["bot"])
                used_instr[idx] = True

        # Try and execute instructions until none are left
        while False in used_instr:

            # Iterate over all the instructions in order
            for idx, instr in enumerate(self.instrucs):

                # If the instruction has been used skip it
                if used_instr[idx]:
                    continue

                # Check the bot only has two values
                if len(self.bots[instr["src-bot"]]) != 2:
                    continue

                # Check for the comparison
                if val_0 is not None or val_1 is not None:
                    if self.bots[instr["src-bot"]] == [val_0, val_1] or self.bots[
                        instr["src-bot"]
                    ] == [val_1, val_0]:
                        return instr["src-bot"]

                self.balance_move(
                    instr["src-bot"],
                    instr["low-bot"],
                    instr["low-dest"],
                    instr["high-bot"],
                    instr["high-dest"],
                )

                used_instr[idx] = True

        # Only crash if the numbers were not provided
        if val_0 is not None or val_1 is not None:
            raise Exception("Transaction not found!")


if __name__ == "__main__":
    factory = BalanceBots("./data/input.txt")
    print(f"Part 1 = {factory.find_comp_bot(61, 17)}")
