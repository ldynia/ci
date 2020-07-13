#!/bin/python3

"""
https://www.hackerrank.com/challenges/2d-array/problem
"""

import math
import os
import random
import re
import sys


def hourglassSum(arr):
    heads = []
    bodies = []
    floors = []

    HEAD_LENGTH = 3
    BODY_INDEX = 1
    FEET_LENGTH = 3

    VERTICAL_STOP_INDEX = 3
    HORIZONTAL_STOP_INDEX = 3

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i <= VERTICAL_STOP_INDEX and j <= HORIZONTAL_STOP_INDEX:
                head = sum(arr[i][j:j + HEAD_LENGTH])
                heads.append(head)

                floor = sum(arr[i + 2][j:j + FEET_LENGTH])
                floors.append(floor)

                body = arr[i + 1][j + BODY_INDEX]
                bodies.append(body)

    hourglasses = tuple(zip(heads, bodies, floors))
    hourglasses_sumed = [sum(hg) for hg in hourglasses]

    return max(hourglasses_sumed)


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(result) + '\n')
    fptr.close()
