#!/bin/python3

"""
Link: https://www.hackerrank.com/challenges/counting-valleys/problem
"""

import math
import os
import random
import re
import sys


def countingValleys(n, s):
    AT_SEA_LINE = 0
    BELLOW_SEA_LINE = -1

    altitude = 0
    valley_roamed = 0
    valley_entered = False
    valley_exited = False

    for step in s:
        if step == 'U':
            altitude += 1
        else:
            altitude -= 1

        if altitude == BELLOW_SEA_LINE:
            valley_entered = True

        if altitude == AT_SEA_LINE and valley_entered:
            valley_roamed += 1
            valley_entered = False

    return valley_roamed


if __name__ == '__main__':
    try:
        n = int(input())
        s = input()

        pattern = "^[UD]{%s,%s}$" % (n, n)
        match = re.search(pattern, s, flags=re.IGNORECASE)

        assert match, f"Invalid pattern for steps input, allowd input is [uUdD] {n} char long."
        assert 2 <= n <= 10**6, "N input is in invalid range. Valid range is '2 < N < 1000000'"
    except ValueError as e:
        print("Error: Invalid value for steps input. Steps input MUST be an intager.")
        exit(1)
    except AssertionError as e:
        print(f"Error: {e}")
        exit(1)

    result = countingValleys(n, s)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(result) + '\n')
    fptr.close()
