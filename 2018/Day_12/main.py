"""
--- Day 12: Subterranean Sustainability ---

The year 518 is significantly more underground than your history books implied.
Either that, or you've arrived in a vast cavern network under the North Pole.

After exploring a little, you discover a long tunnel that contains a row of
small pots as far as you can see to your left and right. A few of them contain
plants - someone is trying to grow things in these geothermally-heated caves.

The pots are numbered, with 0 in front of you. To the left, the pots are
numbered -1, -2, -3, and so on; to the right, 1, 2, 3.... Your puzzle input
contains a list of pots from 0 to the right and whether they do (#) or do not
(.) currently contain a plant, the initial state. (No other pots currently
contain plants.) For example, an initial state of #..##.... indicates that pots
0, 3, and 4 currently contain plants.

Your puzzle input also contains some notes you find on a nearby table: someone
has been trying to figure out how these plants spread to nearby pots. Based on
the notes, for each generation of plants, a given pot has or does not have a
plant based on whether that pot (and the two pots on either side of it) had a
plant in the last generation. These are written as LLCRR => N, where L are pots
to the left, C is the current pot being considered, R are the pots to the right,
and N is whether the current pot will have a plant in the next generation. For
example:


        -   A note like ..#.. => . means that a pot that contains a plant but
            with no plants within two pots of it will not have a plant in it
            during the next generation.

        -   A note like ##.## => . means that an empty pot with two plants on
            each side of it will remain empty in the next generation.

        -   A note like .##.# => # means that a pot has a plant in a given
            generation if, in the previous generation, there were plants in that
            pot, the one immediately to the left, and the one two pots to the
            right, but not in the ones immediately to the right and two to the
            left.

It's not clear what these plants are for, but you're sure it's important, so
you'd like to make sure the current configuration of plants is sustainable by
determining what will happen after 20 generations.

For example, given the following input:

    initial state: #..#.#..##......###...###

    ...## => #
    ..#.. => #
    .#... => #
    .#.#. => #
    .#.## => #
    .##.. => #
    .#### => #
    #.#.# => #
    #.### => #
    ##.#. => #
    ##.## => #
    ###.. => #
    ###.# => #
    ####. => #

For brevity, in this example, only the combinations which do produce a plant are
listed. (Your input includes all possible combinations.) Then, the next 20
generations will look like this:

                    1         2         3
          0         0         0         0
    0: ...#..#.#..##......###...###...........
    1: ...#...#....#.....#..#..#..#...........
    2: ...##..##...##....#..#..#..##..........
    3: ..#.#...#..#.#....#..#..#...#..........
    4: ...#.#..#...#.#...#..#..##..##.........
    5: ....#...##...#.#..#..#...#...#.........
    6: ....##.#.#....#...#..##..##..##........
    7: ...#..###.#...##..#...#...#...#........
    8: ...#....##.#.#.#..##..##..##..##.......
    9: ...##..#..#####....#...#...#...#.......
    10: ..#.#..#...#.##....##..##..##..##......
    11: ...#...##...#.#...#.#...#...#...#......
    12: ...##.#.#....#.#...#.#..##..##..##.....
    13: ..#..###.#....#.#...#....#...#...#.....
    14: ..#....##.#....#.#..##...##..##..##....
    15: ..##..#..#.#....#....#..#.#...#...#....
    16: .#.#..#...#.#...##...#...#.#..##..##...
    17: ..#...##...#.#.#.#...##...#....#...#...
    18: ..##.#.#....#####.#.#.#...##...##..##..
    19: .#..###.#..#.#.#######.#.#.#..#.#...#..
    20: .#....##....#####...#######....#.#..##.

The generation is shown along the left, where 0 is the initial state. The pot
numbers are shown along the top, where 0 labels the center pot, negative-
numbered pots extend to the left, and positive pots extend toward the right.
Remember, the initial state begins at pot 0, which is not the leftmost pot used
in this example.

After one generation, only seven plants remain. The one in pot 0 matched the
rule looking for ..#.., the one in pot 4 matched the rule looking for .#.#., pot
9 matched .##.., and so on.

In this example, after 20 generations, the pots shown as # contain plants, the
furthest left of which is pot -2, and the furthest right of which is pot 34.
Adding up all the numbers of plant-containing pots after the 20th generation
produces 325.

PART 1: After 20 generations, what is the sum of the numbers of all pots which
        contain a plant?

You realize that 20 generations aren't enough. After all, these plants will need
to last another 1500 years to even reach your timeline, not to mention your
future.

PART 2: After fifty billion (50000000000) generations, what is the sum of the
        numbers of all pots which contain a plant?
"""

import sys
from collections import deque


class CaveGarden:
    """
    Simulate a row of plant pots that spread, grow and die out according to
    certain rules and an inital state defined in a supplied text file.
    """

    def __init__(self, data_file: str):
        self.empty = "."
        self.full = "#"
        self.window = 5
        self.orig_start = 0
        self.r_remove = []
        self.r_add = []
        self.r_maintain = []

        with open(data_file, "r") as fp:
            for idx, line in enumerate(fp):
                line = line.strip()

                # Read the intial state.
                if idx == 0:
                    line = line.split(": ")[1]
                    self.plants = deque(line)

                # Read the conversion rules.
                elif idx > 1:
                    pre_state, post_state = line.split(" => ")

                    # Does this rule add a plant
                    if (
                        post_state == self.full
                        and pre_state[self.window // 2] == self.empty
                    ):
                        self.r_add.append(list(pre_state))

                    # Does this rule remove a plant
                    elif (
                        post_state == self.empty
                        and pre_state[self.window // 2] == self.full
                    ):
                        self.r_remove.append(list(pre_state))

                    # Does this rule maintain a plant
                    elif (
                        post_state == self.full
                        and pre_state[self.window // 2] == self.full
                    ):
                        self.r_maintain.append(list(pre_state))

    def grow(self):
        """
        Apply the pre-defined rules to the current plants and change the garden.
        """
        # Ensure that there is at least four empty pots at the start
        while (
            self.full == self.plants[0]
            or self.full == self.plants[1]
            or self.full == self.plants[2]
            or self.full == self.plants[3]
        ):
            self.plants.appendleft(self.empty)
            self.orig_start -= 1

        # Ensure that there at least four empty pots at the end
        while (
            self.full == self.plants[len(self.plants) - 1]
            or self.full == self.plants[len(self.plants) - 2]
            or self.full == self.plants[len(self.plants) - 3]
            or self.full == self.plants[len(self.plants) - 4]
        ):
            self.plants.append(self.empty)

        new_plants = deque(self.empty * len(self.plants))
        sample = deque([self.plants[x] for x in range(self.window)])

        # Implement the changes
        for idx in range(self.window, len(self.plants)):

            # Add a plant
            for add_pat in self.r_add:
                for pat_idx in range(len(add_pat)):
                    if sample[pat_idx] != add_pat[pat_idx]:
                        break
                else:
                    assert self.plants[idx - self.window // 2 - 1] == self.empty
                    new_plants[idx - self.window // 2 - 1] = self.full

            # Maintain a plant
            for main_pat in self.r_maintain:
                for pat_idx in range(len(main_pat)):
                    if sample[pat_idx] != main_pat[pat_idx]:
                        break
                else:
                    assert self.plants[idx - self.window // 2 - 1] == self.full
                    new_plants[idx - self.window // 2 - 1] = self.full

            # Remove a plant
            for rm_pat in self.r_remove:
                for pat_idx in range(len(rm_pat)):
                    if sample[pat_idx] != rm_pat[pat_idx]:
                        break
                else:
                    assert self.plants[idx - self.window // 2 - 1] == self.full
                    new_plants[idx - self.window // 2 - 1] = self.empty

            # Move the sample onto the next window
            sample.popleft()
            sample.append(self.plants[idx])

        # Overwrite the old plants
        self.plants = new_plants

    def plant_score(self) -> int:
        """
        Sum up the indexex of the plants, the index being relative to the
        original position of the first every left most plant.
        """
        plant_sum = 0

        for plnt_idx in range(len(self.plants)):
            if self.plants[plnt_idx] == self.full:
                plant_sum += plnt_idx + self.orig_start

        return plant_sum

    def total_plants_after_time(self, elapsed_time: int) -> int:
        """
        Apply the growth rules the set amount of times and return the resulting
        plant score.
        """
        for _ in range(elapsed_time):
            self.grow()

        return self.plant_score()

    def long_term_plant_score(self, elapsed_time: int) -> int:
        """
        Find the plant score after a very large elapsed time.
        """

        # find the plant score at 1000 and 2000
        for _ in range(1000):
            self.grow()
        score_1k = self.plant_score()

        for _ in range(1000):
            self.grow()
        score_2k = self.plant_score()

        # Determine the gradient and intercept
        grad = (score_2k - score_1k) / 1000
        intercept = score_2k - grad * 2000

        # Calculate what it will be at in the large elapsed time
        return int(grad * elapsed_time + intercept)


if __name__ == "__main__":
    print(f"Part 1 = {CaveGarden('./data/input_0.txt').total_plants_after_time(20)}")
    print(
        f"Part 2 = {CaveGarden('./data/input_0.txt').long_term_plant_score(50000000000)}"
    )
