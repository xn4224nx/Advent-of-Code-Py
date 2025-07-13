r"""

--- Day 7: The Sum of Its Parts ---

You find yourself standing on a snow-covered coastline; apparently, you landed a
little off course. The region is too hilly to see the North Pole from here, but
you do spot some Elves that seem to be trying to unpack something that washed
ashore. It's quite cold out, so you decide to risk creating a paradox by asking
them for directions.

"Oh, are you the search party?" Somehow, you can understand whatever Elves from
the year 1018 speak; you assume it's Ancient Nordic Elvish. Could the device on
your wrist also be a translator? "Those clothes don't look very warm; take
this." They hand you a heavy coat.

"We do need to find our way back to the North Pole, but we have higher
priorities at the moment. You see, believe it or not, this box contains
something that will solve all of Santa's transportation problems - at least,
that's what it looks like from the pictures in the instructions." It doesn't
seem like they can read whatever language it's in, but you can: "Sleigh kit.
Some assembly required."

"'Sleigh'? What a wonderful name! You must help us assemble this 'sleigh' at
once!" They start excitedly pulling more parts out of the box.

The instructions specify a series of steps and requirements about which steps
must be finished before others can begin (your puzzle input). Each step is
designated by a single letter. For example, suppose you have the following
instructions:

    Step C must be finished before step A can begin.
    Step C must be finished before step F can begin.
    Step A must be finished before step B can begin.
    Step A must be finished before step D can begin.
    Step B must be finished before step E can begin.
    Step D must be finished before step E can begin.
    Step F must be finished before step E can begin.

Visually, these requirements look like this:

     -->A--->B--
    /    \      \
    C     -->D----->E
    \           /
     ---->F-----

Your first goal is to determine the order in which the steps should be
completed. If more than one step is ready, choose the step which is first
alphabetically. In this example, the steps would be completed as follows:

        -   Only C is available, and so it is done first.

        -   Next, both A and F are available. A is first alphabetically, so it
            is done next.

        -   Then, even though F was available earlier, steps B and D are now
            also available, and B is the first alphabetically of the three.

        -   After that, only D and F are available. E is not available because
            only some of its prerequisites are complete. Therefore, D is
            completed next.

        -   F is the only choice, so it is done next.

        -   Finally, E is completed.

So, in this example, the correct order is CABDFE.

PART 1: In what order should the steps in your instructions be completed?
"""


class SleighSteps:
    def __init__(self, step_relations: str):
        self.depends = {}

        with open(step_relations, "r") as fp:
            for line in fp.readlines():
                step_0 = ord(line[5]) - ord("A")
                step_1 = ord(line[36]) - ord("A")

                # Ensure that the steps are known about
                if step_0 not in self.depends:
                    self.depends[step_0] = set()
                if step_1 not in self.depends:
                    self.depends[step_1] = set()

                # Add in dependancies
                self.depends[step_1].add(step_0)

    def correct_order(self) -> str:
        """
        Determine the order that the steps must be executed in order to
        build the sleigh. Return a string of that order.
        """
        unused_steps = {x for x in self.depends.keys()}
        step_order = []

        while len(unused_steps) > 0:
            pos_nxt_steps = [x for x in unused_steps if len(self.depends[x]) == 0]

            # Pick the alphabetically ordered first next step
            nxt_step = sorted(pos_nxt_steps)[0]

            # Update data structures
            step_order.append(nxt_step)
            unused_steps.remove(nxt_step)
            [y.discard(nxt_step) for y in self.depends.values()]

        # Convert the order back to letters
        return "".join([chr(x + ord("A")) for x in step_order])


if __name__ == "__main__":
    pass
