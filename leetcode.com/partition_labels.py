#!/usr/bin/env python3

"""
https://www.youtube.com/watch?v=ED4ateJu86I
https://leetcode.com/problems/partition-labels
https://medium.com/@crazcuber/amazon-interview-question-partition-labels-aebe54d24d9e
"""
from collections import OrderedDict


def partitionLabels(seq):
    char_count = dict.fromkeys(seq, 0)
    for char in seq:
        char_count[char] += 1

    char_last_index = OrderedDict()
    for char in seq:
        char_last_index[char] = (len(s) - s[::-1].index(char)) - 1

    od = OrderedDict(sorted(char_last_index.items()))

    results = []
    char_start_index = 0
    char_stop_index = 0
    for char, char_index in od.items():
        if char_stop_index == 0:
            char_stop_index = char_index + 1
            results.append(len(s[char_start_index:char_stop_index]))
            char_start_index = char_stop_index

        if char_index >= char_start_index:
            print(char, s[char_start_index:char_index])

    return results


if __name__ == '__main__':
    s = "ababcbacadefegdehijhklij"

    result = partitionLabels(s)
    print(result)
