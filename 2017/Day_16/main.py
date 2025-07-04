"""
--- Day 16: Permutation Promenade ---

You come upon a very unusual sight; a group of programs here appear to be
dancing.

There are sixteen programs in total, named a through p. They start by standing
in a line: a stands in position 0, b stands in position 1, and so on until p,
which stands in position 15.

The programs' dance consists of a sequence of dance moves:

    -   Spin, written sX, makes X programs move from the end to the front, but
        maintain their order otherwise. (For example, s3 on abcde produces
        cdeab).

    -   Exchange, written xA/B, makes the programs at positions A and B swap
        places.

    -   Partner, written pA/B, makes the programs named A and B swap places.

For example, with only five programs standing in a line (abcde), they could do
the following dance:

    -   s1, a spin of size 1: eabcd.

    -   x3/4, swapping the last two programs: eabdc.

    -   pe/b, swapping programs e and b: baedc.

After finishing their dance, the programs end up in order baedc.

PART 1: You watch the dance for a while and record their dance moves (your
        puzzle input). In what order are the programs standing after their
        dance?

Now that you're starting to get a feel for the dance moves, you turn your
attention to the dance as a whole.

Keeping the positions they ended up in from their previous dance, the programs
perform it again and again: including the first dance, a total of one billion
(1000000000) times.

In the example above, their second dance would begin with the order baedc, and
use the same dance moves:

    -   s1, a spin of size 1: cbaed.

    -   x3/4, swapping the last two programs: cbade.

    -   pe/b, swapping programs e and b: ceadb.

PART 2: In what order are the programs standing after their billion dances?
"""

from collections import deque


class ProgramDance:
    def __init__(self, initial_progs: str, instruc_file: str):
        self.init_state = deque(initial_progs)
        self.progs = deque(initial_progs)
        self.instructs = []

        # Parse the instruction file
        with open(instruc_file, "r") as fp:
            for raw in fp.read().split(","):
                tmp_insr = {}

                # Parse the raw instruction
                if raw[0] == "s":
                    tmp_insr["name"] = "spin"
                    tmp_insr["magnitude"] = int(raw[1:])

                elif raw[0] == "x":
                    tmp_insr["name"] = "exchange"
                    val0, val1 = raw[1:].split("/", 1)
                    tmp_insr["idx_a"] = int(val0)
                    tmp_insr["idx_b"] = int(val1)

                elif raw[0] == "p":
                    tmp_insr["name"] = "partner"
                    val0, val1 = raw[1:].split("/", 1)
                    tmp_insr["prog_a"] = val0.strip()
                    tmp_insr["prog_b"] = val1.strip()

                else:
                    raise Exception(f"Instruction {raw} isn't valid")

                self.instructs.append(tmp_insr)

    def spin(self, magnitude: int):
        """
        Make a number of programs move from the end to the front
        """
        self.progs.rotate(magnitude)

    def exchange(self, idx_a: int, idx_b: int):
        """
        Swap programs by index.
        """
        val_a = self.progs[idx_a]
        val_b = self.progs[idx_b]
        self.progs[idx_a] = val_b
        self.progs[idx_b] = val_a

    def partner(self, prog_a: str, prog_b: str):
        """
        Swap programs by value.
        """
        idx_a = self.progs.index(prog_a)
        idx_b = self.progs.index(prog_b)
        self.exchange(idx_a, idx_b)

    def execute_command(self, com: dict[str:str]):
        """
        Execute one of the commands, spin, exchange or partner.
        """
        if com["name"] == "spin":
            self.spin(com["magnitude"])

        elif com["name"] == "exchange":
            self.exchange(com["idx_a"], com["idx_b"])

        elif com["name"] == "partner":
            self.partner(com["prog_a"], com["prog_b"])

        else:
            raise Exception(f"Command is not supported: {com}")

    def state(self):
        """
        Return the state the programs are currently in.
        """
        return "".join(self.progs)

    def run_all_commands(self) -> str:
        """
        Using the instructions file find the final order of the programs.
        """
        for instr_idx in range(len(self.instructs)):
            self.execute_command(self.instructs[instr_idx])

        return self.state()

    def loop_detection_fstate(self, iterations: int = 1_000_000_000) -> str:
        """
        Run commands until a duplicate program state is seen. Then determine
        what the final state of the programs will be after the specified number
        of iterations.
        """
        self.progs = self.init_state
        seen_states = {self.state(): 0}
        loop_iter = 0

        # Find the loop in the instructions
        while True:
            self.run_all_commands()
            loop_iter += 1

            # Check if this state has been seen before
            if self.state() in seen_states:
                break

        # Determine characteristics about the loop
        loop_state = self.state()
        loop_size = loop_iter - seen_states[loop_state]

        # Work out how many of the iterations still need to be done after the loop
        remainder = (iterations - seen_states[loop_state]) % loop_size

        for _ in range(remainder):
            for instr_idx in range(len(self.instructs)):
                self.execute_command(self.instructs[instr_idx])

        return self.state()


if __name__ == "__main__":
    perm_prom = ProgramDance("abcdefghijklmnop", "./data/input.txt")
    print(
        f"Part 1 = {perm_prom.run_all_commands()}\n"
        f"Part 2 = {perm_prom.loop_detection_fstate()}\n"
    )
