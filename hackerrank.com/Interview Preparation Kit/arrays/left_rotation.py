#!/bin/python3

"""
Link: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
"""

import math
import os
import random
import re
import sys


def rotLeft(a, d):
    if len(a) == d:
        return a

    head = a[:d]
    tail = a[d:]

    return tail + head


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
