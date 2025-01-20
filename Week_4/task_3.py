def compress(data):
    """ First, it should extract all keys, sort them alphabetically (as the Python sorted function does it), and store them in a tuple. Second, it should create a tuple for each dictionary, where the values of the dictionary are stored in the correct order.

    [
    {"a": 1, "b": 2, "c": 3},
    {"a": 9, "c": 7, "b": 8}, # dictionary keys don't have any order
    ...
    ]


    (
    ("a", "b", "c"),   # keys in a tuple
    [
        (1, 2, 3),     # values of each dictionary
        (9, 8, 7)      # values in correct order corresponding to the keys!
    ]
    )
    """

    # If data is an entirely empty list, the result tuple should contain an empty tuple and an empty list. If data is a list containing an empty dictionary, then the result tuple should contain an empty tuple as the first value and a list containing an empty tuple as the second value

    if data == []:
        return (), []
    elif data == [{}]:
        return (), [()]
    else:
        key_lst = []
        val_lst = []

        # data 1st item is a dictionary, get the keys of that dict if theres something in dict else return empty list
        key_lst = sorted(data[0].keys() if data else [])

        # iterate over lst items
        for d in data:
            # append to val_lst tuple: the value for the key in key list
            val_lst.append(tuple(d[key] for key in key_lst))

        key_tup = tuple(key_lst)

    return (key_tup, val_lst)


data = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "c": 6, "b": 5},
    {"a": 7, "c": 8, "b": 9}
]
print(compress(data))
