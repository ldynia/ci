# Links: https://docs.python.org/3/howto/sorting.html

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}


if __name__ == '__main__':
    min_price = min(zip(prices.values(), prices.keys()))
    max_price = max(zip(prices.values(), prices.keys()))

    print(min(prices.values()))
    print(max(prices.values()))

    print(min_price)
    print(max_price)

    min_value = prices[min(prices, key=lambda k: prices[k])]
    man_value = prices[max(prices, key=lambda k: prices[k])]

    print(min_price)
    print(max_price)

    lt = list(prices.items())
    print(lt)

    prices_sorted = sorted(lt, key=lambda s: s[1], reverse=True)
    print(prices_sorted)

    prices_sorted = sorted(zip(prices.values(), prices.keys()), reverse=True)
    print(prices_sorted)

    # sorting a dict
    a = {'y': 2, 'x': 3, 'z': 1}
    print(sorted(list(a.items()), key=lambda el: el[0]))
    print(sorted(list(a.items()), key=lambda el: el[1]))
