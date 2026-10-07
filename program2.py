def find_blank(state):
    return state.index(0)


def get_neighbors(state):
    neighbors = []
    blank_idx = find_blank(state)
    row, col = divmod(blank_idx, 3)

    moves = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    for dr, dc, _ in moves:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col

            new_state = list(state)
            new_state[blank_idx], new_state[new_idx] = \
                new_state[new_idx], new_state[blank_idx]

            neighbors.append(tuple(new_state))

    return neighbors


def dls(state, goal, depth):

    if state == goal:
        return [state]

    if depth <= 0:
        return None

    for neighbor in get_neighbors(state):
        result = dls(neighbor, goal, depth - 1)

        if result is not None:
            return [state] + result

    return None


if __name__ == "__main__":

    initial_board = (
        1, 2, 3,
        4, 0, 7,
        8, 5, 6
    )

    goal_board = (
        1, 2, 3,
        4, 5, 6,
        7, 8, 0
    )

    depth_limit = 10  

    print("\nSearching using Depth Limited Search (DLS)...")

    path = dls(initial_board, goal_board, depth_limit)

    if path:
        print(f"\nSolution found at depth {len(path) - 1}!")

        for step, board in enumerate(path):
            print(f"\nStep {step}:")
            print(board[0:3])
            print(board[3:6])
            print(board[6:9])

    else:
        print(f"\nNo solution found within depth limit {depth_limit}.")