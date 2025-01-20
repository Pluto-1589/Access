# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def min_domino_rotations(top, bottom):

    def check(target, top, bottom, n):
        rotations_top, rotations_bottom = 0, 0

        for i in range(n):
            if top[i] != target and bottom[i] != target:
                return -1
            elif top[i] != target:
                rotations_top += 1
            elif bottom[i] != target:
                rotations_bottom += 1

        return min(rotations_top, rotations_bottom)

    n = len(top)

    min_rotations = check(top[0], top, bottom, n)

    if min_rotations == -1:
        return check(bottom[0], top, bottom, n)

    return min_rotations


# The following line calls the function which will print # value to the Console.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(min_domino_rotations([2, 6, 2, 1, 2, 2], [5, 2, 4, 2, 3, 2]))
print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))
