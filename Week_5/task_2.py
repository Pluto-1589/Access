wa_nrs = ["0781111119", "0792653913", "0797763139",
          "0792793193", "0781139022", "0764320165"]


def get_possible_nrs(n):

    pos_nums = set()

    if len(n) != 9 or n[:2] != "07":
        return "Invalid phone number"
    else:
        for idx in range(10):
            for digit in range(10):
                pos_nums.add("07" + n[2:idx] + str(digit) + n[idx:])

    possible_nrs_for_juliet = []

    for num in wa_nrs:
        if num in pos_nums:
            possible_nrs_for_juliet.append(num)

    return possible_nrs_for_juliet


# For this particular number, the function should find the
# last element in wa_nrs
print(get_possible_nrs("076432165"))
