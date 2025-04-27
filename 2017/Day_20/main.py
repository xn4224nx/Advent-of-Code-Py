"""
--- Day 20: Particle Swarm ---

Suddenly, the GPU contacts you, asking for help. Someone has asked it to
simulate too many particles, and it won't be able to finish them all in time to
render the next frame at this rate.

It transmits to you a buffer (your puzzle input) listing each particle in order
(starting with particle 0, then particle 1, particle 2, and so on). For each
particle, it provides the X, Y, and Z coordinates for the particle's position
(p), velocity (v), and acceleration (a), each in the format <X,Y,Z>.

Each tick, all particles are updated simultaneously. A particle's properties
are updated in the following order:

    -   Increase the X velocity by the X acceleration.

    -   Increase the Y velocity by the Y acceleration.

    -   Increase the Z velocity by the Z acceleration.

    -   Increase the X position by the X velocity.

    -   Increase the Y position by the Y velocity.

    -   Increase the Z position by the Z velocity.

Because of seemingly tenuous rationale involving z-buffering, the GPU would
like to know which particle will stay closest to position <0,0,0> in the long
term. Measure this using the Manhattan distance, which in this situation is
simply the sum of the absolute values of a particle's X, Y, and Z position.

For example, suppose you are only given two particles, both of which stay
entirely on the X-axis (for simplicity). Drawing the current states of
particles 0 and 1 (in that order) with an adjacent a number line and diagram of
current X positions (marked in parentheses), the following would take place:

    p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
    p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>                         (0)(1)

    p=< 4,0,0>, v=< 1,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
    p=< 2,0,0>, v=<-2,0,0>, a=<-2,0,0>                      (1)   (0)

    p=< 4,0,0>, v=< 0,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
    p=<-2,0,0>, v=<-4,0,0>, a=<-2,0,0>          (1)               (0)

    p=< 3,0,0>, v=<-1,0,0>, a=<-1,0,0>    -4 -3 -2 -1  0  1  2  3  4
    p=<-8,0,0>, v=<-6,0,0>, a=<-2,0,0>

At this point, particle 1 will never be closer to <0,0,0> than particle 0, and
so, in the long run, particle 0 will stay closest.

PART 1: Which particle will stay closest to position <0,0,0> in the long term?
"""

import re


class ParticleSwarm:
    def __init__(self, datafile: str, pnt: (int, int, int) = (0, 0, 0)):
        self.pnt = pnt
        self.particles = []

        with open(datafile, "r") as fp:
            for line in fp.readlines():
                result = re.findall("-?[0-9]+", line)

                if result is None or len(result) != 9:
                    raise Exception(f"Line '{line}' could not be parsed!")

                self.particles.append(
                    [
                        (
                            int(result[0]),
                            int(result[1]),
                            int(result[2]),
                        ),
                        (
                            int(result[3]),
                            int(result[4]),
                            int(result[5]),
                        ),
                        (
                            int(result[6]),
                            int(result[7]),
                            int(result[8]),
                        ),
                    ]
                )

    def tick(self):
        """
        Calculate each particles new acceleration, velocity and position in
        that order.
        """
        for p_idx in range(len(self.particles)):

            # Modify velocity with the current acceleration
            self.particles[p_idx][1] = (
                self.particles[p_idx][2][0] + self.particles[p_idx][1][0],
                self.particles[p_idx][2][1] + self.particles[p_idx][1][1],
                self.particles[p_idx][2][2] + self.particles[p_idx][1][2],
            )

            # Modify position with the just changed velocity
            self.particles[p_idx][0] = (
                self.particles[p_idx][0][0] + self.particles[p_idx][1][0],
                self.particles[p_idx][0][1] + self.particles[p_idx][1][1],
                self.particles[p_idx][0][2] + self.particles[p_idx][1][2],
            )

    def particle_dists(self) -> list[int]:
        """
        For each particle calculate the manhattan distance from the specifified
        point. Return the distances as a list.
        """
        return [abs(x[0][0]) + abs(x[0][1]) + abs(x[0][2]) for x in self.particles]

    def long_term_closest(self) -> int:
        """
        Perform multiple ticks to determe which of the particles will remain the
        closest to the specified point long term. Shortcut using SUVAT equations
        s = ut + 0.5 at^2
        """
        time_period = 1_000_000

        # Calculate the new positions after a large period of time
        part_dists = []
        for p_idx in range(len(self.particles)):
            part_dists.append(
                abs(
                    self.particles[p_idx][0][0]
                    + self.particles[p_idx][1][0] * time_period
                    + 0.5 * self.particles[p_idx][2][0] * time_period * time_period
                )
                + abs(
                    self.particles[p_idx][0][1]
                    + self.particles[p_idx][1][1] * time_period
                    + 0.5 * self.particles[p_idx][2][1] * time_period * time_period
                )
                + abs(
                    self.particles[p_idx][0][2]
                    + self.particles[p_idx][1][2] * time_period
                    + 0.5 * self.particles[p_idx][2][2] * time_period * time_period
                )
            )

        # Find the particle with the smallest distance
        return min(range(len(part_dists)), key=part_dists.__getitem__)


if __name__ == "__main__":
    print(f"Part 1 = {ParticleSwarm("./data/input.txt").long_term_closest()}")
