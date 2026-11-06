import random
def heuristic(board):
    count = 0
    for i in range(8):
        for j in range(i+1, 8):
            if board[i] == board[j] or abs(board[i]-board[j]) == abs(i-j):
                count += 1
    return count
def neighbours(board):
    n = []
    for i in range(8):
        for j in range(8):
            if board[i] != j:
                b = board.copy()
                b[i] = j
                n.append(b)
    return n
def hill_climbing():
    while True:
        board = [random.randint(0, 7) for _ in range(8)]
        while heuristic(board) != 0:
            next_states = neighbours(board)
            best = min(heuristic(b) for b in next_states)
            if best >= heuristic(board):
                break
            choices = [b for b in next_states if heuristic(b) == best]
            board = random.choice(choices)
        if heuristic(board) == 0:
            return board
solution = hill_climbing()
print("Solution:", solution)
print("Heuristic:", heuristic(solution))
for i in range(8):
    for j in range(8):
        print("Q" if solution[i] == j else ".", end=" ")
    print()
