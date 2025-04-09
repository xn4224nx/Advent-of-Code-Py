"""
--- Day 12: Digital Plumber ---

Walking along the memory banks of the stream, you find a small village that is
experiencing a little confusion: some programs can't communicate with each
other.

Programs in this village communicate using a fixed system of pipes. Messages are
passed between programs using these pipes, but most programs aren't connected to
each other directly. Instead, programs pass messages between each other until
the message reaches the intended recipient.

For some reason, though, some of these messages aren't ever reaching their
intended recipient, and the programs suspect that some pipes are missing. They
would like you to investigate.

You walk through the village and record the ID of each program and the IDs with
which it can communicate directly (your puzzle input). Each program has one or
more programs with which it can communicate, and these pipes are bidirectional;
if 8 says it can communicate with 11, then 11 will say it can communicate with
8.

You need to figure out how many programs are in the group that contains program
ID 0.

For example, suppose you go door-to-door like a travelling salesman and record
the following list:

0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5

In this example, the following programs are in the group that contains program
ID 0:

    -   Program 0 by definition.
    -   Program 2, directly connected to program 0.
    -   Program 3 via program 2.
    -   Program 4 via program 2.
    -   Program 5 via programs 6, then 4, then 2.
    -   Program 6 via programs 4, then 2.

Therefore, a total of 6 programs are in this group; all but program 1, which has
a pipe that connects it to itself.

PART 1: How many programs are in the group that contains program ID 0?
"""

import re


class ProgramNetwork:
    def __init__(self, connections_file: str):
        self.conns = {}

        with open(connections_file, "r") as fp:
            for line in fp.readlines():
                prog, prog_links = line.split(" <-> ", 1)

                # Extract the program links
                prog_links = [int(x.strip()) for x in prog_links.split(",")]
                prog = int(prog)

                # Add in missing programs
                if prog not in self.conns:
                    self.conns[prog] = set()

                # Add in links in this record
                self.conns[prog].update(prog_links)

                # Add in the reverse links
                for c_prog in prog_links:
                    if c_prog not in self.conns:
                        self.conns[c_prog] = set()
                    self.conns[c_prog].add(prog)

        # Remove self referential links
        for prog in self.conns:
            if prog in self.conns[prog]:
                self.conns[prog].remove(prog)

    def group_size(self, program_id: int) -> int:
        """
        Find the size of the group that contains the specified program.
        """
        conn_progs = set()
        next_progs = {program_id}

        # Start at the initial program and count every other program it links to
        while len(next_progs) > 0:
            new_next_progs = set()

            # Get the connected programs
            for prog in next_progs:
                conn_progs.add(prog)

                # Prepare to check programs in the next loop
                for c_prog in self.conns[prog]:
                    if c_prog not in conn_progs:
                        new_next_progs.add(c_prog)

            # Prepare for the next loop iteration
            next_progs = new_next_progs

        return len(conn_progs)


if __name__ == "__main__":
    pass
