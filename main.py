d = {"München": "MUC", "Budapest": "BUD", "Helsinki": "HEL"}

for key in d:
    value = d[key]
    print(key)
    print(value)

    for key, value in d.items():
        print(key + ": " + value)