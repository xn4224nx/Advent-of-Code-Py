# -*- coding: utf-8 -*-
"""

--- Day 4: The Ideal Stocking Stuffer ---

Find MD5 hashes which, in hexadecimal, start with at least five zeroes.

Created on Tue Dec 27 02:28:29 2022

@author: FAKENAME
"""

import hashlib

secret_key = "yzbqklnj"

has_num = 0

while True:

    hash_num = secret_key + str(has_num).zfill(6)

    hash_ = hashlib.md5(hash_num.encode()).hexdigest()

    if hash_.startswith("000000"):
        print(hash_)
        break

    has_num += 1
