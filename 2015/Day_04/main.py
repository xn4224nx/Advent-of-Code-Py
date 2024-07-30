"""
--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to
bitcoins) to use as gifts for all the economically forward-
thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal,
start with at least five zeroes. The input to the MD5 hash is
some secret key (your puzzle input, given below) followed by a
number in decimal.

PART 1: To mine AdventCoins, you must find Santa the lowest
        positive number (no leading zeroes: 1, 2, 3, ...) that
        produces such a hash.
"""

import hashlib


def valid_mine(secret_key: str, answer: int) -> bool:
    """
    Determine if the combination of secret key and answer
    creates a MD5 hash digest with five leading zeroes.
    """

    value = secret_key + str(answer)
    digest = hashlib.md5(value.encode()).hexdigest()

    return digest[:5] == "00000"


def mine_santa_coins(secret_key: str) -> int:
    """
    Find the lowest integer that produces a MD5 hash that starts
    with five zeroes. Then return that integer.
    """
    answer = 1

    while not valid_mine(secret_key, answer):
        answer += 1

    return answer


if __name__ == "__main__":
    print(f"Part 1 answer = {mine_santa_coins('iwrupvqb')}")
