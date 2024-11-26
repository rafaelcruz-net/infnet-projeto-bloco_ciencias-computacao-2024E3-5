def tsp_caixeiro_viajante(graph, start):
    unvisited = set(graph.keys())
    unvisited.remove(start)
    current_node = start
    path = [start]
    total_distance = 0
    
    while unvisited:
        next_node = min(unvisited, key=lambda node: graph[current_node][node])
        total_distance += graph[current_node][next_node]
        path.append(next_node)
        current_node = next_node
        unvisited.remove(next_node)
    
    # Retorna ao ponto de partida
    total_distance += graph[current_node][start]
    path.append(start)

    return path, total_distance

graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

start_node = 'A'

path, distance = tsp_caixeiro_viajante(graph, start_node)
print("Caminho aproximado:", path)
print("Distância total aproximada:", distance)