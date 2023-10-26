graph = {
	'A' : ['B','C'],
	'B' : ['D','E'],
	'C' : ['F','G'],
	'D' : [],
	'E' : [],
	'F' : [],
	'G' : []
}
visited = []
queue = []
def bfs(visited,graph,node):
	visited.append(node)
	queue.append(node)
	while queue:
		m = queue.pop(0)
		print(m, end = " ")
		for nighbour in graph[m]:
			if nighbour not in visited:
				visited.append(nighbour)
				queue.append(nighbour )

bfs(visited,graph,'A')
print('\n')
print("Breadth First Search")