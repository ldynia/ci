#!/bin/python3

import math
import os
import random
import re
import sys


def makeAnagram(a, b):
    set_a = set(a)
    set_b = set(b)

    if len(a) == 0 or len(b) == 0:
        return len(a) + len(b)

    # count and set a flag for set a
    dict_a = dict.fromkeys(set_a, 0)
    only_ones_in_a = True
    for char in a:
        dict_a[char] += 1
        if dict_a[char] > 1:
            only_ones_in_a = False

    # count and set a flag for set b
    dict_b = dict.fromkeys(set_b, 0)
    only_once_in_b = True
    for char in b:
        dict_b[char] += 1
        if dict_b[char] > 1:
            only_once_in_b = False

    if only_ones_in_a and only_once_in_b:
        return len(set_a.difference(set_b)) + len(set_b.difference(set_a))

    # calculate deletions for common chars in both sets
    deletion_count = 0
    common_chars = set_a.intersection(set_b)
    for char in common_chars:
        if dict_a[char] != dict_b[char]:
            deletion_count += abs(dict_a[char] - dict_b[char])

    # calculate deletions for chars in sets a
    for char in dict_a.keys():
        if char not in common_chars:
            deletion_count += dict_a[char]

    # calculate deletions for chars in sets b
    for char in dict_b.keys():
        if char not in common_chars:
            deletion_count += dict_b[char]

    return deletion_count


if __name__ == '__main__':
    a = input().strip()
    b = input().strip()

    res = makeAnagram(a, b)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(res) + '\n')
    fptr.close()
