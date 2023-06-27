"""
--- Day 2: Dive! ---

Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like forward 1,
down 2, or up 3:

    - forward X increases the horizontal position by X units.
    - down X increases the depth by X units.
    - up X decreases the depth by X units.

Note that since you're on a submarine, down and up affect your depth, and so
they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You
should probably figure out where it's going. Your horizontal position and depth
both start at 0.

Calculate the horizontal position and depth you would have after following the
planned course.

    Part 1: What do you get if you multiply your final horizontal position by
            your final depth?

"""