#!/bin/python3

import math
import os
import random
import re
import sys


def repeatedString(s, n):
    if len(s) == 1 and s == 'a':
        return n

    if len(s) > n:
        return s[:n].count('a')

    a_count = s.count('a')
    if len(s) == n:
        return a_count

    divisions = int(n / len(s))
    head_count = a_count * divisions
    if n == divisions * len(s):
        return head_count

    tail = n - (divisions * len(s))
    tail_count = s[:tail].count('a')

    return head_count + tail_count


if __name__ == '__main__':
    s = input().strip()
    n = int(input().strip())

    result = repeatedString(s, n)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(result) + '\n')
    fptr.close()
