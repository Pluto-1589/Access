from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
]


def reverse_index(dataset: list):

    # create empty dictionary
    index_dictionary = {}
    # set a list as default value of defaultdict and assign to index
    index = defaultdict(list)

    # enumerate over index and string in dataset
    for idx, string in enumerate(dataset):

        # split string into words then lowercase them, then assign to words
        words = string.lower().split()
        # iterate over word in words
        for word in words:
            # assign word as key and append idx to the list in index dict
            index[word].append(idx)

    # turn from type defaultdict to dict
    index_dictionary = dict(index)

    return index_dictionary


    # don't forget to return your resulting dictionary
# You can see the output of your function here
print(reverse_index(dataset))
