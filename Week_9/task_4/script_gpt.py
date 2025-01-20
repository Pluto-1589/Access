

def move(state, direction):

    validate_state(state)
    if direction not in ("up", "down", "left", "right"):
        raise Warning(f"Invalid direction: {direction}")

    rows = len(state)
    cols = len(state[0])
    x, y = find_player(state)

    dx, dy = {"up": (-1, 0), "down": (1, 0), "left": (0, -1),
              "right": (0, 1)}[direction]
    nx, ny = x + dx, y + dy

    if not (0 <= nx < rows and 0 <= ny < cols) or state[nx][ny] == "#":
        raise Warning("Invalid move: Blocked or out of bounds")

    new_state = [list(row) for row in state]
    new_state[x][y], new_state[nx][ny] = " ", "o"
    new_state = tuple("".join(row) for row in new_state)

    possible_moves = []
    for d, (dx, dy) in {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}.items():
        px, py = nx + dx, ny + dy
        if 0 <= px < rows and 0 <= py < cols and state[px][py] == " ":
            possible_moves.append(d)

    return new_state, tuple(sorted(possible_moves))


def validate_state(state):

    if not isinstance(state, tuple) or not all(isinstance(row, str) for row in state):
        raise Warning("State must be a tuple of strings")

    if len(set(len(row) for row in state)) > 1:
        raise Warning("Rows in the state have inconsistent lengths")

    valid_chars = {"#", " ", "o"}
    if any(char not in valid_chars for row in state for char in row):
        raise Warning("State contains invalid characters")

    if sum(row.count("o") for row in state) != 1:
        raise Warning("State must contain exactly one player marker")

    if len(state) <= 0 or len(state[0]) <= 0:
        raise Warning("State size must be greater than 0")


def find_player(state):

    for i, row in enumerate(state):
        for j, char in enumerate(row):
            if char == "o":
                return i, j
    raise Warning("Player not found")
