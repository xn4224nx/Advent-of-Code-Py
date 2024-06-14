"""
--- Day 20: Infinite Elves and Infinite Houses ---

Each Elf delivers presents equal to ten times his or her number at each house.

The elves that visit a house are based on the factors of the house number.

What is the lowest house number of the house to get at least as many presents
as the number in your puzzle input?

"""
import numpy as np

N = 36000000

n_presents = np.zeros(N//10)
n_presents2 = np.zeros(N//10)

for i in range(1, N//10):
    n_presents[i::i] += 10 * i
    n_presents2[i:(50*i)+1:i] += 11 * i

# Part 1
print(np.where(n_presents >= N)[0][0])

# Part 2
print(np.where(n_presents2 >= N)[0][0])

