words = ["apple", "mountain", "river", "asteroid", "armadillo", "guitar",
         "sapphire", "keyboard", "planet", "mango", "mirror", "jazz", "robot",
         "lighthouse", "pineapple", "wizard", "cloud", "penguin", "spaghetti"]


def words_with_length(length):
    '''this one just serves as an example'''
    return [word for word in words if len(word) == length]


def words_containing_string(s):
    return [word for word in words if s in word]


def words_starting_with_character(c):
    return [word for word in words if word[0] == c]


def words_with_matching_ends():
    return [word for word in words if word[0] == word[-1]]


def words_with_unique_characters():
    return [word for word in words if len(word) == len(set(word))]


def count_unique_characters():
    return {word: int(len(set(word))) for word in words}


def dictionary():
    from string import ascii_lowercase
    return {c: words_starting_with_character(c) for c in ascii_lowercase}


print(words_with_length(4))
print(words_containing_string("et"))
print(words_starting_with_character("a"))
print(words_with_matching_ends())
print(words_with_unique_characters())
print(count_unique_characters())
print(dictionary())
