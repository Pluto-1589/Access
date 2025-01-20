count = 0


def knapsack(capacity, weights, values, lookup_table=None):
    # Only for performance measurement. You can ignore this line or event remove it.
    global count
    count += 1

    # Initialize lookup table on the first call
    if lookup_table is None:
        lookup_table = {}

    # You need to change the following part of the function
    # Try two possibilities for each item — either include it in the knapsack (if it fits) or exclude it — and take the maximum of these choices.
    # capacity: the maximum weight capacity of the knapsack.

    lst = []

    if capacity == 0 or not weights:
        return 0
    else:
        # if weight greater than capacity skip the weight by moving to the next one
        if weights[0] > capacity:
            res = knapsack(capacity, weights[1:], values[1:], lookup_table)
        else:
            # else take 1st value and add it to the recursive call
            include = values[0] + knapsack(capacity - weights[0],
                                           weights[1:], values[1:], lookup_table)
            # if the current item is excluded
            exclude = knapsack(
                capacity, weights[1:], values[1:], lookup_table)
            res = max(include, exclude)

        return res

    # weights: a list of weights for each item.
    # values: a list of values for each item.
    # lookup_table: a dictionary or list to store previously computed results for subproblems (only needed for the optional tests).


if __name__ == "__main__":
    # The following lines call the function and prints the return
    # value to the Console. This way you can check what it does.
    print("The maximum value in the knapsack is:",
          knapsack(50, [10, 20, 30], [260, 100, 120]))
    print("Number of function calls:", count)
