def withinConstraint(graph, color, v, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graphColourUtil(graph, m, color, v):
    if v == len(graph):
        return True

    for c in range(1, m + 1):
        if withinConstraint(graph, color, v, c):
            color[v] = c
            if graphColourUtil(graph, m, color, v + 1):
                return True
            color[v] = 0
    return False

def graphColouring(graph, m, colors):
    color = [0] * len(graph)
    if not graphColourUtil(graph, m, color, 0):
        return False
    print("\nAssigned colors are - ")
    for v, c in enumerate(color):
        print(f"\tVertex {v+1} = {colors[c-1]}")
    return True


n = int(input("Enter the number of vertices: "))

graph = []

for _ in range(n):
    row = [0] * n 
    graph.append(row)
    
print("\nEnter the adjacent vertices for each vertex -\n")

for i in range(n):

    print(f"\tAdjacent vertices for Vertex {i+1} :", end=' ')
    adj_vertices = list(map(int, input().split()))
    for j in adj_vertices:
        graph[i][j-1] = 1
        graph[j-1][i] = 1

m = int(input("\nEnter the number of colors: "))
colors = input("Enter the color names separated by commas: ").split(',')
graphColouring(graph, m, colors)