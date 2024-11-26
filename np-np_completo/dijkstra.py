import heapq

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if (current_distance > distances[current_node]):
            continue

        for neighbor, weigth in graph[current_node].items():
            distance = current_distance + weigth

            if (distance < distances[neighbor]):
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 6},
    'C': {'D': 3},
    'D': {}
}

start_node = 'A'
dijkstra_result = dijkstra(graph, start_node)
print("Dijkstra - Caminho mínimo e distâncias:", dijkstra_result)
