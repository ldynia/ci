#!/bin/python3

"""
Links: https://www.youtube.com/watch?v=J9ikRMK8Yhs
"""

import math
import os
import random
import re
import sys


def minimumSwaps(arr):
    swaps_count = 0

    return swaps_count


def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]
    return arr


if __name__ == '__main__':
    n = 4
    arr = [4, 3, 1, 2]
    # n = int(input())
    # arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # fptr.write(str(res) + '\n')
    # fptr.close()
