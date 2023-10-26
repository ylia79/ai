def dfs(graph, start, depth):
    visited = set()
    stack = [(start, 0)]
    while stack:
        current, current_depth = stack.pop()
        if current_depth <= depth:
            if current not in visited:
                visited.add(current)
                print(current)
            if current_depth < depth:
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        stack.append((neighbor, current_depth + 1))

graph = {
    'A': ['C', 'B'],
    'B': ['E', 'D'],
    'C': ['G', 'F'],
    'D': ['I', 'H'],
    'E': ['K', 'J'],
    'F': ['M', 'L'],
    'G': ['O', 'N'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': []
}

start_node = 'A'
max_depth = int(input("Enter the maximum depth: "))

for depth in range(max_depth + 1):
    print(f"Depth {depth}:")
    dfs(graph, start_node, depth)
    print()
