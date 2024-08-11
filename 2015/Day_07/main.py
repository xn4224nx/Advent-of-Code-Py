"""
--- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of
wires and bitwise logic gates! Unfortunately, little
Bobby is a little under the recommended age range, and
he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and
can carry a 16-bit signal (a number from 0 to 65535). A
signal is provided to each wire by a gate, another
wire, or some specific value. Each wire can only get a
signal from one source, but can provide its signal to
multiple destinations. A gate provides no signal until
all of its inputs have a signal.

The included instructions booklet describes how to
connect the parts together: x AND y -> z means to
connect wires x and y to an AND gate, and then connect
its output to wire z.

Other possible gates include OR (bitwise OR) and RSHIFT
(right-shift). If, for some reason, you'd like to
emulate the circuit instead, almost all programming
languages (for example, C, JavaScript, or Python)
provide operators for these gates.

PART 1: In little Bobby's kit's instructions booklet
        (provided as your puzzle input), what signal is
        ultimately provided to wire a?
"""


class Circuit:
    """
    Simulate a circuit via a set of instructions read
    from a text file.
    """

    def __init__(self, inst_filepath: str):
        self.wire_sig = {}
        self.all_instr = []

        # Split the destination and instruction
        with open(inst_filepath) as fp:
            for raw_line in fp.readlines():
                instr, dest = raw_line.split(" -> ", 1)

                # Make a record of each wire
                self.wire_sig[dest.strip()] = 0

                # Save the instructions
                self.all_instr.append((instr.strip(), dest.strip()))

    def resolve_value(self, value: str) -> int:
        """
        Ensure the value is an integer or find out
        referenced wire's signal.
        """
        if value.isdigit():
            return int(value)

        elif value in self.wire_sig:
            return self.wire_sig[value]

        else:
            return None

    def exe_single_instr(self, instr: str, dest: str):
        """
        With a single instruction and destination modify
        the wire signals accordingly.
        """

        if "NOT" in instr:
            tmp = instr.replace("NOT ", "")
            val = self.resolve_value(tmp)

            if val is None:
                return

            self.wire_sig[dest] = ~self.resolve_value(tmp)

        elif " " in instr:
            p1, mid, p2 = instr.split(" ", 2)
            val1 = self.resolve_value(p1)
            val2 = self.resolve_value(p2)

            if val1 is None or val2 is None:
                return

            if mid == "AND":
                self.wire_sig[dest] = val1 & val2

            elif mid == "OR":
                self.wire_sig[dest] = val1 | val2

            elif mid == "LSHIFT":
                self.wire_sig[dest] = val1 << val2

            elif mid == "RSHIFT":
                self.wire_sig[dest] = val1 >> val2

            else:
                raise Exception(f"Unknown command {mid}")

        # Assignment
        else:
            val = self.resolve_value(instr)

            if val is None:
                return

            self.wire_sig[dest] = val

    def execute_instructions(self):
        """
        Run through all the instructions and modify the wire
        signals accordingly.
        """
        for instr, dest in self.all_instr:
            self.exe_single_instr(instr, dest)

    def ret_a_sig(self):
        """
        Return the signal of the a wire.
        """
        print(self.wire_sig)
        return self.wire_sig["a"]


if __name__ == "__main__":
    bob = Circuit("./data/input.txt")
    bob.execute_instructions()
    print(f"Part 1 = {bob.ret_a_sig()}")