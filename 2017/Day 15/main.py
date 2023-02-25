"""
--- Day 15: Dueling Generators ---

Here, you encounter a pair of dueling generators. The generators, called
generator A and generator B, are trying to agree on a sequence of numbers.
However, one of them is malfunctioning, and so the sequences don't always
match.

As they do this, a judge waits for each of them to generate its next value,
compares the lowest 16 bits of both values, and keeps track of the number of
times those parts of the values match.

The generators both work on the same principle. To create its next value, a
generator will take the previous value it produced, multiply it by a factor
(generator A uses 16807; generator B uses 48271), and then keep the remainder
of dividing that resulting product by 2147483647. That final remainder is the
value it produces next.
"""


def num_generator(prev_val: int, mult_val: int, divisor: int) -> int:

    while True:
        prev_val *= mult_val
        prev_val %= 2147483647

        if prev_val % divisor == 0:
            yield prev_val


def binary_check(num_a: int, num_b: int, last_n:int) -> bool:
    return bin(num_a)[-last_n:] == bin(num_b)[-last_n:]


gen_a1 = num_generator(116, 16807, 1)
gen_b1 = num_generator(299, 48271, 1)
gen_a2 = num_generator(116, 16807, 4)
gen_b2 = num_generator(299, 48271, 8)

sum_part1 = 0
sum_part2 = 0

for i in range(40_000_000):
    sum_part1 += binary_check(next(gen_a1), next(gen_b1), 16)

print(sum_part1)

for i in range(5_000_000):

    num_a = next(gen_a2)
    num_b = next(gen_b2)

    sum_part2 += binary_check(num_a, num_b, 16)

print(sum_part2)