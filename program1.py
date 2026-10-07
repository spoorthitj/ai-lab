
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
            new_state[blank_idx], new_state[new_idx] = new_state[new_idx], new_state[blank_idx]
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


def iddfs(start_state, goal_state, max_depth=30):
    for depth in range(max_depth + 1):
        result = dls(start_state, goal_state, depth)
        if result is not None:
            return result, depth  # Returns path and the depth it was found at
            
    return None, None


if __name__ == "__main__":

    initial_board = (1, 2, 3, 
                     4, 0, 5, 
                     6, 7, 8)
                     
    goal_board =    (1, 2, 3, 
                     4, 5, 0, 
                     6, 7, 8)
    
    print("Searching for a solution using IDDFS...")
    path, found_depth = iddfs(initial_board, goal_board, max_depth=10)
    
    if path:
        print(f"Solution found at depth {found_depth} with {len(path) - 1} moves!\n")
        for step, board in enumerate(path):
            print(f"Step {step}:")
            print(board[0:3])
            print(board[3:6])
            print(board[6:9])
            print()
    else:
        print("No solution found within the maximum depth limit.")
 
