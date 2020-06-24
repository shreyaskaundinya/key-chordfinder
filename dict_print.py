'''def dprint(d, depth=1):
    layers = []
    layers.append(list(d.keys()))
    values = []
    for value in d.values():
        if isinstance(value, dict):
            values.append(list(value.values()))
        else:
            values.append

    layers.append(values)
    print(layers)




dprint(d)'''


d = {
    "1": {
        "name": {"here": "one"}
    },

    "2": {
        "name": "two"
    },

    "3": {
        "name": "three"
    }
}


def dvals(d, layers, length, keys):
    print(d, layers, length, keys)
    if length == -1:
        return layers
    elif length == len(d)-1:
        layers.append(keys)
    else:
        pass

    v = d[keys[length]]
    print("v", v, keys[length])
    if isinstance(v, dict):
        l = dvals(v, [], len(v)-1, list(v.keys()))
        layers.append(l)
    else:
        layers.append(d[keys[length]])

    length -= 1
    print()


emp = []
pr = dvals(d, emp, len(d)-1, list(d.keys()))
print(pr)
