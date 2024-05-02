import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def heuristic(state, goal_state):
    h = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_position = next((r, c) for r, row in enumerate(goal_state) for c, v in enumerate(row) if v == value)
                h += manhattan_distance((i, j), goal_position)
    return h

def is_goal(state, goal_state):
    return state == goal_state

def get_neighbors(node):
    neighbors = []
    i, j = get_blank_position(node.state)

    for x, y, move in [(i-1, j, 'up'), (i+1, j, 'down'), (i, j-1, 'left'), (i, j+1, 'right')]:
        if 0 <= x < 3 and 0 <= y < 3:
            new_state = [row[:] for row in node.state]
            new_state[i][j], new_state[x][y] = new_state[x][y], new_state[i][j]
            action = f"Move {move}"
            neighbors.append(PuzzleNode(new_state, node, action, node.cost + 1, heuristic(new_state, goal_state)))

    return neighbors

def print_solution(node):
    moves = []  # List to store moves

    while node.parent is not None:
        moves.append((node.action, node.state, node.cost, node.heuristic, node.cost + node.heuristic))
        node = node.parent


    total_cost = 0
    print("\n")
    print("\t    | |")
    print("\t    | |")
    print("\t   \\   /")
    print("\t    \\ /")
    print("\n")
    for move, state, gn, hn, fn in reversed(moves):
        print(f"\t{move}")
        print("\tg(n):", gn)
        print("\th(n):", hn)
        print("\tf(n):", fn)
        print("\n")
        for row in state:
            print('\t',row)
        

        total_cost += 1  # Increment the total cost for each step



    print("Total Cost:", total_cost)


def a_star(initial_state, goal_state):
    initial_node = PuzzleNode(initial_state, None, None, 0, heuristic(initial_state, goal_state))
    heap = [initial_node]
    heapq.heapify(heap)
    visited = set()

    while heap:
        current_node = heapq.heappop(heap)

        if is_goal(current_node.state, goal_state):
            print_solution(current_node)
            return

        visited.add(tuple(map(tuple, current_node.state)))

        for neighbor in get_neighbors(current_node):
            if tuple(map(tuple, neighbor.state)) not in visited:
                heapq.heappush(heap, neighbor)

    print("No solution found.")

initial_state = []
goal_state = []

print("Enter the initial state (3x3 matrix, use 0 for the blank space):")
for i in range(3):
    row = list(map(int, input().split()))
    initial_state.append(row)

print("\nEnter the goal state (3x3 matrix, use 0 for the blank space):")
for i in range(3):
    row = list(map(int, input().split()))
    goal_state.append(row)

print("\nSteps :-")
print("\n\tInitial State")
for row in initial_state:
    print('\t',row)

a_star(initial_state, goal_state)