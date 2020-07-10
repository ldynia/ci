#!/bin/python3

"""
Link: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
"""

import math
import os
import random
import re
import sys


def jumpingOnClouds(clouds):
    CUMULUS = 0
    ONE_STEP_JUMP = 1
    TWO_STEP_JUMP = 2

    cloud_indexes = []
    thunder_indexes = []
    tmp = {"cumulus": 0, "thunder": 0}

    # index clouds
    for i in range(0, len(clouds)):
        if int(clouds[i]) == CUMULUS:
            tmp['cumulus'] += 1
            cloud_indexes.append(i)
        else:
            tmp['thunder'] += 1
            thunder_indexes.append(i)

    # count clouds
    jump = 0
    current_cloud_index = 0
    for ci in cloud_indexes:
        one_step_index = current_cloud_index + ONE_STEP_JUMP
        two_step_index = current_cloud_index + TWO_STEP_JUMP
        if current_cloud_index == 0:
            if two_step_index not in thunder_indexes:
                current_cloud_index = two_step_index
            else:
                current_cloud_index = one_step_index
            jump += 1
        else:
            if current_cloud_index < cloud_indexes[-1]:
                if two_step_index not in thunder_indexes:
                    current_cloud_index = two_step_index
                else:
                    current_cloud_index = one_step_index
                jump += 1

    return jump


if __name__ == '__main__':
    try:
        n = int(input().strip())
        c = list(map(int, input().rstrip().split()))

        assert c[0] == 0, f"First input '{c[0]}' MUST be 0."
        assert c[-1] == 0, f"Last input '{c[-1]}' MUST be 0."
        assert len(c) == n, "Provided input doesn't match own lengths."
        assert 2 <= n <= 100,  f"Provided input '{n}' is in invalid range. Allowed range is '2 <= n <= 100'."
        for n in c:
            assert n in [0, 1], f"Provided input '{n}' is invalid. Allowed values are [0, 1]."
    except AssertionError as e:
        print(f"Error: {e}")
        exit(1)
    except ValueError as e:
        print(f"Error: Invalid value provided. {e}")
        exit(1)
    except Exception as e:
        print(f"Error: Something went wrong")
        exit(1)

    result = jumpingOnClouds(c)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(result) + '\n')
    fptr.close()
