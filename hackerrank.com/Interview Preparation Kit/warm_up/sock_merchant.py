#!/bin/python3

"""
Link: https://www.hackerrank.com/challenges/sock-merchant/problem
"""

import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    tmp = {}
    for color in ar:
        if color in tmp:
            tmp[color] += 0.5
        else:
            tmp[color] = 0.5

    # Sum up floored elements
    result = 0
    for v in tmp.values():
        result += int(v)

    return result


if __name__ == '__main__':
    try:
        n = int(input().strip())
        ar = list(map(int, input().rstrip().split()))

        assert len(ar) == n, "Provided input(s) doesn't match own lengths."
        assert 1 <= n <= 100, "Provided input is in invalid range. Accepted range is '1 <= n <= 100'."
        for n in ar:
            assert 1 <= n <= 100, f"Element '{n}' is in invalid range. Accepted range is '1 <= n <= 100'."
    except ValueError:
        print(f"Error: Provided input is invalid. Program expects only integers.")
        exit(1)
    except AssertionError as e:
        print(f"Error: {e}")
        exit(1)
    except Exception:
        print(f"Error: Provided input is invalid. Details: {e}")
        exit(1)

    result = sockMerchant(n, ar)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(result) + '\n')
    fptr.close()
