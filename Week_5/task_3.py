# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def merge(a, b):

    # If one or both lists are empty, the empty list should be returned.
    if not a or not b:
        return []

    # get max length between inputs
    max_len = max(len(a), len(b))

    # original, get last val of original then multiply the string by the max length minus the length of the original list
    # [0,1,2] + 2 * (3 - 3)
    rep_a = a + [a[-1]] * (max_len - len(a))
    # [5,6] + 6 * (3 - 2)
    rep_b = b + [b[-1]] * (max_len - len(b))

    # tuple for elements at position i in the range of the maximum length
    merged = [(rep_a[i], rep_b[i]) for i in range(max_len)]

    return merged


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(merge([], [5, 6]))
print(merge([0, 1, 2], [5, 6]))
