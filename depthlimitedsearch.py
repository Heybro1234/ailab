def depth_limited_search(graph, start, goal, limit):
    if start == goal:
        return [start]
    
    if limit == 0:
        return None
    
    for node in graph[start]:
        path = depth_limited_search(graph, node, goal, limit-1)
        if path is not None:
            return [start] + path
    
    return None

def print_nodes(graph, start, goal, limit):
    result = depth_limited_search(graph, start, goal, limit)
    if result is None:
        print("No path found")
    else:
        print("Path:", result)

# Example graph
graph = {"A": ["B", "C"],"B": ["D"],"C": ["E"],"D": ["F"],"E": [],"F": []}

start = "A"
goal = "F"
limit = 3

print_nodes(graph, start, goal, limit)

