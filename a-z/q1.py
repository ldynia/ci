#!/#!/usr/bin/env python3

"""
amazon test id 23280666807354
"""

import math
from collections import OrderedDict


def closestLocations(totalCrates, allLocations, truckCapacity):
    origin = [0, 0]
    distances = {}
    # O(n)
    for location in allLocations:
        x = location[0] - origin[0]
        y = location[1] - origin[1]
        distance = math.sqrt(x**2 + y**2)
        distances[distance] = location

    # O(log n) or # O(nlog n)
    sorted_distance = sorted(distances.items())

    # O(n)
    results = []
    for d in sorted_distance:
        if len(results) < truckCapacity:
            results.append(d[1])

    return results


if __name__ == '__main__':
    result = closestLocations(3, [[1, 2], [3, 4], [1, -1]], 2)
    print(result)
