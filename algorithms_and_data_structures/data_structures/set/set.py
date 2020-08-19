# link https://www.programiz.com/python-programming/set
# step 10: https://learning.oreilly.com/scenarios/python-cookbook-data/9781492061465/

s1 = {1, 2, 3}
s2 = {3, 4, 5}


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            yield item


def dedupeDict(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            seen.add(val)
            yield item


if __name__ == '__main__':
    print('union', s1 | s2)
    print('symmetric difference', s1 ^ s2)
    print('intersect', s1 & s2)
    print('diffrence right', s1 - s2)
    print('diffrence left', s2 - s1)

    a = [1, 5, 2, 1, 9, 1, 5, 10]
    r = dedupe(a)  # generator
    print('xxx', list(r))

    b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    r1 = dedupeDict(b, key=lambda d: d['x'])
    r2 = dedupeDict(b, key=lambda d: (d['x'], d['y']))
    print(list(r1))
    print(list(r2))
