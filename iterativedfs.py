def iterative_dfs(graph, start, goal):
    for depth in range(len(graph)):
        if dfs(graph, start, goal, depth):
            return True
    return False

def dfs(graph, start, goal, depth):
    if depth < 0:
        return False
    if start == goal:
        return True
    for child in graph[start]:
        if dfs(graph, child, goal, depth - 1):
            return True
    return False

# Test on acyclic graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
start = 'A'
goal = 'E'
result = iterative_dfs(graph, start, goal)
print(result)  # True

# Test on cyclic graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['A'],
    'E': [],
    'F': []
}
start = 'A'
goal = 'E'
result = iterative_dfs(graph, start, goal)
print(result)  # True

