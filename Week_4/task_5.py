def invert(d):
    """return a dictionary where keys-value pairs in d have been inverted, meaning that the original values become keys and the original keys become values.

    inverted dictionary must have lists as values, in which all original keys are collected and sorted.
    """

    # initialise new dict
    new_d = {}
    # iterate over key and value in original dict
    for k, v in d.items():
        # if old value in new dict as key
        if v in new_d:
            # new dict old value is now key and append old key as value
            new_d[v].append(k)
            # otherwise
        else:
            # add old value as new key with old key as value
            new_d[v] = [k]

    # iterate over keys in new dict
    for key in new_d:
        # sort
        new_d[key].sort()

    return new_d


# should return {1: ["a", "b"], 3: ["c"]}
print(invert({"a": 1, "b": 1, "c": 3}))
