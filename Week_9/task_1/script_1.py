def sorted_arrays_overlap(array_1, array_2):
    # Validate input types
    if not isinstance(array_1, list) or not isinstance(array_2, list):
        raise TypeError(
            "Invalid input types! Both parameters should be arrays.")

    # Check for empty arrays
    if not array_1 or not array_2:
        raise ValueError("Empty arrays! Neither of the arrays can be empty.")

    # Ensure all elements are integers
    if not all(isinstance(x, int) for x in array_1 + array_2):
        raise TypeError(
            "Invalid data types within arrays! Arrays should contain only integers.")

    # Check if arrays are sorted
    if array_1 != sorted(array_1) or array_2 != sorted(array_2):
        raise ValueError(
            "Not sorted arrays! Both arrays should be sorted in ascending order.")

    # Find intersection
    return sorted(set(array_1).intersection(array_2))
