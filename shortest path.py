def shortest_path(graph, start_node, end_node):


  Q = [start_node]
  visited = set()

  while Q:
    current_node = Q.pop(0)
    visited.add(current_node)

    for neighbor in graph[current_node]:
      if neighbor not in visited:
        Q.append(neighbor)

        if neighbor == end_node:
          return [current_node] + shortest_path(graph, start_node, neighbor)

  return None


# Example usage:
graph = {
  'A': {'B': 1, 'C': 3},
  'B': {'D': 2},
  'C': {'D': 4},
  'D': {'E': 5}
}

shortest_path = shortest_path(graph, 'A', 'E')

print(shortest_path)
