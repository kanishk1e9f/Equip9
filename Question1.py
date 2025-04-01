from collections import deque

def find_nearest_equipment(n, edges, availability, start_provider, target_equipment):
    graph = {i: [] for i in range(1, n+1)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    for key in graph:
        graph[key].sort()

    if target_equipment in availability.get(start_provider, []):
        return [start_provider]

    queue = deque([(start_provider, [start_provider])])
    visited = set([start_provider])

    while queue:
        provider, path = queue.popleft()
        for neighbor in graph[provider]:
            if neighbor not in visited:
                if neighbor == 1 and start_provider != 1:
                    continue
                visited.add(neighbor)
                new_path = path + [neighbor]

                if target_equipment in availability.get(neighbor, []):
                    return new_path

                queue.append((neighbor, new_path))

    return -1

n = 5
edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
availability = {1: ["excavator"], 2: [], 3: ["bulldozer"], 4: ["excavator"], 5: ["crane"]}
start_provider = 2
target_equipment = "excavator"

print(find_nearest_equipment(n, edges, availability, start_provider, target_equipment))
