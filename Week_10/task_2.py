def powerset(nums: list):
    # The power set includes all subsets ranging from the empty set to the set itself.
    # takes a list of integers as input and returns all possible subsets of these integers.
    # If the input list is empty, the function should return a list containing an empty list.
    # Ensure that the function removes duplicates if the input list contains any.

    # remove duplicates
    nums = list(set(nums))

    # base case
    if not nums:
        return [[]]
    else:
        # subsets are powerset function from second index item to last
        sub_sets = powerset(nums[1:])
        # first value of nums
        first_val = nums[0]
        # complete power set is the first value plus the subsets in subsets
        complete = [[first_val] + subset for subset in sub_sets]

        return sub_sets + complete


# The following lines call the function and print the return
# value to the Console. This way you can check what they do.
test_set = [1, 2, 3]
result = powerset(test_set)
# Example output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# Note that the order of the powerset could differ depending on the implementation.
# Make sure to look at the predefined test and adjust it if so.
print(result)
