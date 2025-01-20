# implement a function move that takes two arguments: 1) a game state and 2) a direction into which the player marker should be moved. The function should check whether this move is possible and, if yes, return the mutated game state, as well as all possible walking directions in the new state, ordered alphabetically (i.e., down < left < right < up).

def move_right(state):

    current_position = list(current_player_position(state))
    rocks = rock_position(state)

    new_position = (current_position[0], current_position[1] + 1)

    if new_position in rocks:
        raise Warning("Invalid movement, to the right are rocks")
    elif new_position[1] >= len(state[0]):
        raise Warning("Invalid movement, position out of bound")
    elif new_position[0] >= len(state):
        raise Warning("Invalid movement, position out of bound")
    else:
        new_state = list(state)
        row_player = new_state[current_position[0]]

        # replace old player location with " "
        row_player = (
            row_player[:current_position[1]] + " " +
            row_player[current_position[1] + 1:]
        )

        # Place "o" in the new position
        row_player = (
            row_player[:new_position[1]] + "o" +
            row_player[new_position[1] + 1:]
        )

    return tuple(new_state)


def move_left(state):

    current_position = list(current_player_position(state))
    rocks = rock_position(state)

    new_position = (current_position[0], current_position[1] - 1)

    if new_position in rocks:
        raise Warning("Invalid movement, to the left are rocks")
    elif new_position[1] >= len(state[0]):
        raise Warning("Invalid movement, position out of bound")
    elif new_position[0] >= len(state):
        raise Warning("Invalid movement, position out of bound")
    else:
        new_state = list(state)
        row_player = new_state[current_position[0]]

        # replace old player location with " "
        row_player = (
            row_player[:current_position[1]] + " " +
            row_player[current_position[1] + 1:]
        )

        # Place "o" in the new position
        row_player = (
            row_player[:new_position[1]] + "o" +
            row_player[new_position[1] + 1:]
        )

    return tuple(new_state)


def move(state, direction):
    # You task is to test and implement a function move that takes two arguments: 1) a game state and 2) a direction into which the player marker should be moved. The function should check whether this move is possible and, if yes, return the mutated game state, as well as all possible walking directions in the new state, ordered alphabetically (i.e., down < left < right < up).For example, a call to move(state, "right") should return the following result (a tuple with two elements, the first being the updated game world and the second containing all valid next movement directions):
    # new game state :

    def current_player_position(state):

        for idx_row, row in enumerate(state):
            if "o" in row:
                idx_col = row.index("o")

        return (idx_row, idx_col)

    def rock_position(state):

        rock_idx = []

        for idx_row, row in enumerate(state):
            for idx_col, char in enumerate(row):
                if "#" == char:
                    idx_col = row.index("#")
                    rock_idx.append((idx_row, idx_col))

        return rock_idx

    current_position = list(current_player_position(state))
    rocks = rock_position(state)

    # right
    if direction == "right":
        pass
    # left
    if direction == "left":
        pass
    # up
    if direction == "up":
        pass
    # down
    if direction == "down":
        pass
    pass


# The following line calls the function and prints the return
# value to the Console.
s1 = (
    "#####   ",
    "###    #",
    "#   o ##",
    "   #####"

)
# s2 = move(s1, "right")

# print("= New State =")
# print("\n".join(s2[0]))
# print(f"\nPossible Moves: {s2[1]}")

print(current_player_position(s1))
print(rock_position(s1))
print(move_left(s1))
print("\n".join(move_left(s1)))
