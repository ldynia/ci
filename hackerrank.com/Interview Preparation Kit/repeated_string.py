#!/bin/python3

import math
import os
import random
import re
import sys


def repeatedString(s, n):
    infint_str = ''
    if len(s) == n:
        infint_str = s

    if len(s) == 1 and s == 'a':
        return n

    if len(s) == 1 and s != 'a':
        infint_str = s * n

    if len(s) < n:
        divisions = int(n / len(s))
        print(divisions * len(s), n)
        if n == divisions * len(s):
            infint_str = s * divisions
        else:
            infint_str = s * divisions
            tail = n - (divisions * len(s))
            infint_str += infint_str[:tail]

    return infint_str.count('a')


if __name__ == '__main__':

    # s = input()
    # n = int(input())

    s = 'kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm'
    n = 736778906400

    result = repeatedString(s, n)
    print(result)

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # fptr.write(str(result) + '\n')
    # fptr.close()
