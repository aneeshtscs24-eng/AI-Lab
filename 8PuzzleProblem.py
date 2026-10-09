import heapq

GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)
GOAL_POSITIONS = {val: (i // 3, i % 3) for i, val in enumerate(GOAL_STATE) if val != 0}
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def manhattan_distance(state):
    dist = 0
    for idx, val in enumerate(state):
        if val != 0:
            target_r, target_c = GOAL_POSITIONS[val]
            curr_r, curr_c = divmod(idx, 3)
            dist += abs(curr_r - target_r) + abs(curr_c - target_c)
    return dist

def get_neighbors(state):
    blank_idx = state.index(0)
    r, c = divmod(blank_idx, 3)
    neighbors = []
    for dr, dc in MOVES:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            swap_idx = nr * 3 + nc
            new_state = list(state)
            new_state[blank_idx], new_state[swap_idx] = new_state[swap_idx], new_state[blank_idx]
            neighbors.append(tuple(new_state))
    return neighbors

def reconstruct_path(parent_map, state):
    path = []
    curr = state
    while curr is not None:
        path.append(curr)
        curr = parent_map.get(curr)
    return path[::-1]

def a_star_8_puzzle(start_state):
    counter = 0
    open_heap = [(manhattan_distance(start_state), 0, counter, start_state)]
    g_score = {start_state: 0}
    parent = {start_state: None}
    while open_heap:
        f, g, _, current = heapq.heappop(open_heap)
        if current == GOAL_STATE:
            return reconstruct_path(parent, current)
        if g > g_score[current]:
            continue
        for neighbor in get_neighbors(current):
            tentative_g = g + 1
            if tentative_g < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g
                parent[neighbor] = current
                counter += 1
                f_score = tentative_g + manhattan_distance(neighbor)
                heapq.heappush(open_heap, (f_score, tentative_g, counter, neighbor))
    return None

def print_board(state):
    for i in range(0, 9, 3):
        print(" ".join(str(x) if x != 0 else "_" for x in state[i:i+3]))

if __name__ == "__main__":
    start_state = (1, 2, 3, 0, 4, 6, 7, 5, 8)
    solution_path = a_star_8_puzzle(start_state)
    if solution_path:
        for step, board in enumerate(solution_path):
            print(f"Step {step}:")
            print_board(board)