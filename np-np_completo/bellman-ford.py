def bellman_ford(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if (distances[node] + weight < distances[neighbor]):
                    distances[neighbor] = distances[node] + weight

    # Verificação dos pesos negativos
    for node in graph:
        for neighbor, weight in graph[node].items():
            if (distances[node] + weight < distances[neighbor]):
                return "Ciclo negativo"
    
    return distances

graph_negative = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': -3, 'D': 2},
    'C': {'D': -3},
    'D': {}
}

start_node = 'A'
bellman_ford_result = bellman_ford(graph_negative, start_node)
print("Bellman-Ford - Caminho mínimo e distâncias:", bellman_ford_result)
