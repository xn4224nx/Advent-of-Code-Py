"""
--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent assistance
with jump instructions, it would like you to compute the result of a series of
unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to
increase or decrease that register's value, the amount by which to increase or
decrease it, and a condition. If the condition fails, skip the instruction
without modifying the register. The registers all start at 0.

The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10

What is the largest value in any register after completing the instructions?
"""

import re

class Register:
    """Simulate a CPU register."""

    def __init__(self, instructions_file_path: str):

        re_register_instructions = r"([a-z]+) (inc|dec) ([\-0-9]+) if " \
                                   r"([a-z]+) ([<>=!]{1,2}) ([\-0-9]+)"

        self.register_instructions = []
        self.register_values = {}
        self.max_during_run = 0

        # Load the instructions from file
        with open(instructions_file_path, "r") as file:
            for line in file:

                # Extract the name and weight of the program
                reg_instruct = re.search(re_register_instructions, line)

                # Put the values into a dict
                self.register_instructions.append(
                    {
                        "Mod Reg": reg_instruct.group(1),
                        "Chng Type": reg_instruct.group(2),
                        "Chng Amount": int(reg_instruct.group(3)),
                        "Com Reg": reg_instruct.group(4),
                        "Com Type": reg_instruct.group(5),
                        "Com Thres": int(reg_instruct.group(6))
                    }
                )

                # Initialise the register values
                if reg_instruct.group(1) not in self.register_values:
                    self.register_values[reg_instruct.group(1)] = 0

    def run_instruct(self, ins_dict: dict):
        """Run a single line instruction."""

        comparison_value = self.register_values[ins_dict["Com Reg"]]

        # Check if the change gets enacted
        if ins_dict["Com Type"] == "==":
            enacted = comparison_value == ins_dict["Com Thres"]

        elif ins_dict["Com Type"] == "<":
            enacted = comparison_value < ins_dict["Com Thres"]

        elif ins_dict["Com Type"] == ">":
            enacted = comparison_value > ins_dict["Com Thres"]

        elif ins_dict["Com Type"] == "<=":
            enacted = comparison_value <= ins_dict["Com Thres"]

        elif ins_dict["Com Type"] == ">=":
            enacted = comparison_value >= ins_dict["Com Thres"]

        elif ins_dict["Com Type"] == "!=":
            enacted = comparison_value != ins_dict["Com Thres"]

        else:
            raise Exception(f"{ins_dict['Com Type']} is not a recognised "
                            f"comparison type.")

        if not enacted:
            return

        if ins_dict["Chng Type"] == "dec":
            change_direction = -1
        elif ins_dict["Chng Type"] == "inc":
            change_direction = 1
        else:
            raise Exception(f"{ins_dict['Chng Type']}  is not a recognised "
                            f"change direction.")

        self.register_values[ins_dict["Mod Reg"]] += change_direction * \
                                                     ins_dict["Chng Amount"]

    def run_all_instructs(self):
        """Run all the instructions"""

        for instruct in self.register_instructions:

            self.run_instruct(instruct)

            # Check if the register max has been exceeded
            self.register_max()

    def register_max(self) -> int:
        """
        Find the maximum value in the register and set the max_during_run
        variable.
        """

        max_reg = max(self.register_values.values())

        if max_reg > self.max_during_run:
            self.max_during_run = max_reg


cpu_reg = Register("data/input.txt")
cpu_reg.run_all_instructs()

# Part 1
print(max(cpu_reg.register_values.values()))

# Part 2
print(cpu_reg.max_during_run)
