from collections import deque

MAX_VERTICES = 100  # Maximum number of vertices allowed

# Function to perform Depth-First Search (DFS)
def depthFirstSearch(node, adjacencyList, visited):
    visited.add(node)
    print(node, end=" ")
    for neighbor in adjacencyList[node]:
        if neighbor not in visited:
            depthFirstSearch(neighbor, adjacencyList, visited)

# Function to perform Breadth-First Search (BFS)
def breadthFirstSearch(node, adjacencyList):
    distances = [-1] * MAX_VERTICES  # Initialize all distances to -1
    distances[node] = 0  # Distance of the starting node is 0
    queue = deque([node])  # Initialize the queue with the starting node
    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")
        for neighbor in adjacencyList[current_node]:
            if distances[neighbor] == -1:  # If the neighbor hasn't been visited yet
                distances[neighbor] = distances[current_node] + 1  # Update its distance
                queue.append(neighbor)  # Enqueue the neighbor

# Main program
adjacencyList = [[] for _ in range(MAX_VERTICES)]  # Initialize the adjacency list

# Read the number of nodes and edges
numNodes = int(input("Enter the number of nodes: "))
numEdges = int(input("Enter the number of edges: "))

# Read the edges and update the adjacency list
print("Enter the edges:")
for i in range(numEdges):
    u, v = map(int, input(f"Enter edge {i+1} (u v): ").split())
    adjacencyList[u].append(v)
    adjacencyList[v].append(u)  # For undirected graph

# Prompt the user for the starting node
startNode = int(input("Enter the starting node for DFS and BFS: "))

# Perform DFS
print("DFS:", end=" ")
visited = set()  # Use a set to keep track of visited nodes
depthFirstSearch(startNode, adjacencyList, visited)
print()

# Perform BFS
print("BFS:", end=" ")
breadthFirstSearch(startNode, adjacencyList)