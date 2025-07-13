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

As you're about to begin construction, four of the Elves offer to help. "The
sun will set soon; it'll go faster if we work together." Now, you need to
account for multiple people working on steps simultaneously. If multiple steps
are available, workers should still begin them in alphabetical order.

Each step takes 60 seconds plus an amount corresponding to its letter: A=1,
B=2, C=3, and so on. So, step A takes 60+1=61 seconds, while step Z takes
60+26=86 seconds. No time is required between steps.

To simplify things for the example, however, suppose you only have help from
one Elf (a total of two workers) and that each step takes 60 fewer seconds (so
that step A takes 1 second and step Z takes 26 seconds). Then, using the same
instructions as above, this is how each second would be spent:

Second   Worker 1   Worker 2   Done
   0        C          .
   1        C          .
   2        C          .
   3        A          F       C
   4        B          F       CA
   5        B          F       CA
   6        D          F       CAB
   7        D          F       CAB
   8        D          F       CAB
   9        D          .       CABF
  10        E          .       CABFD
  11        E          .       CABFD
  12        E          .       CABFD
  13        E          .       CABFD
  14        E          .       CABFD
  15        .          .       CABFDE

Each row represents one second of time. The Second column identifies how many
seconds have passed as of the beginning of that second. Each worker column
shows the step that worker is currently doing (or . if they are idle). The
Done column shows completed steps.

Note that the order of the steps has changed; this is because steps now take
time to finish and multiple workers can begin multiple steps simultaneously.

In this example, it would take 15 seconds for two workers to complete these
steps.

PART 2: With 5 workers and the 60+ second step durations described above, how
        long will it take to complete all of the steps?
"""

import sys


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
        depends = self.depends.copy()
        unused_steps = {x for x in depends.keys()}
        step_order = []

        while len(unused_steps) > 0:
            pos_nxt_steps = [x for x in unused_steps if len(depends[x]) == 0]

            # Pick the alphabetically ordered first next step
            nxt_step = sorted(pos_nxt_steps)[0]

            # Update data structures
            step_order.append(nxt_step)
            unused_steps.remove(nxt_step)
            [y.discard(nxt_step) for y in depends.values()]

        # Convert the order back to letters
        return "".join([chr(x + ord("A")) for x in step_order])

    def threaded_order_time(self, num_workers: int, add_time: int) -> int:
        """
        Determine the total time to do all the steps when you have a certain
        number workers and each step takes a value equal to its order and an
        additional time period.
        """
        step_order = []
        depends = self.depends.copy()
        unused_steps = {x for x in depends.keys()}
        worker_load = [None] * num_workers
        worker_time = [None] * num_workers
        time_taken = 0

        while len(unused_steps) > 0:
            pos_nxt_steps = sorted(
                [x for x in unused_steps if len(depends[x]) == 0], reverse=True
            )

            # Assign the steps to workers
            for wrk_idx in range(num_workers):
                if worker_load[wrk_idx] is None and pos_nxt_steps:
                    step = pos_nxt_steps.pop()
                    worker_load[wrk_idx] = step
                    worker_time[wrk_idx] = 1 + step + add_time
                    unused_steps.remove(step)
                    [y.discard(step) for y in depends.values()]

            # Find the step that will complete next
            nxt_step = None
            min_wrk_idx = None
            min_time = sys.maxsize

            for wrk_idx in range(num_workers):
                if worker_time[wrk_idx] is not None and worker_time[wrk_idx] < min_time:
                    nxt_step = worker_load[wrk_idx]
                    min_wrk_idx = wrk_idx
                    min_time = worker_time[wrk_idx]

            # Speed forward time till one of the workers completes
            worker_time = [
                worker_time[x] - min_time if worker_time[x] is not None else None
                for x in range(num_workers)
            ]

            # Add the completed step and reset the worker
            step_order.append(nxt_step)
            worker_time[min_wrk_idx] = None
            worker_load[min_wrk_idx] = None
            time_taken += min_time

        # Take care of the remaining workers
        return time_taken + max([x for x in worker_time if x is not None]) + 1


if __name__ == "__main__":
    constr = SleighSteps("./data/input_0.txt")
    print(f"Part 1 = {constr.correct_order()}")
    print(f"Part 2 = {constr.threaded_order_time(5, 60)}")
