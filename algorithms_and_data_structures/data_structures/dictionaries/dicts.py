from collections import defaultdict
from collections import OrderedDict


if __name__ == '__main__':
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)
    print(d)

    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(2)
    d['b'].add(4)
    print(d)

    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4

    for key in d:
        print(key, d[key])

    # Common features in dict
    a = {'x': 1, 'y': 2, 'z': 3}
    b = {'w': 10, 'x': 11, 'y': 2}

    print(a.keys() & b.keys())
    print(a.keys() - b.keys())
    print(a.items() & b.items())
    print(a.items() - b.items())

    # Make a new dictionary with certain keys removed
    c = {key: a[key] for key in a.keys() - {'z', 'w'}}
    print(c)
