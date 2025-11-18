def merge(values):
    dct = {}
    for i in values:
        for key, values in i.items():
            dct.setdefault(key, set()).add(values)

    return dct

print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]))