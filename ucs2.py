import heapq

def uniform_cost_search(graph, start, goal):
    heap = [(0, start)]
    visited = set()
    while heap:
        (cost, current) = heapq.heappop(heap)
        if current == goal:
            return cost
        if current in visited:
            continue
        visited.add(current)
        for node, weight in graph[current].items():
            heapq.heappush(heap, (cost + weight, node))
    return float("inf")

graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1},
}

print(uniform_cost_search(graph, "A", "D"))

