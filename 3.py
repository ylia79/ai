from queue import PriorityQueue

def greedy_best_first_search(graph, start_node, goal_node, heuristic):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start_node))
    
    while not pq.empty():
        cost, current_node = pq.get()
        if current_node == goal_node:
            print("Goal node found:", current_node)
            return
        visited.add(current_node)
        print("Visiting node:", current_node)
        
        for neighbor, neighbor_cost in graph[current_node]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))
    
    print("Goal node not found!")

heuristic = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

graph = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Bucharest': [('Urziceni', 85), ('Pitesti', 101), ('Giurgiu', 90), ('Fagaras', 211)],
    'Craiova': [('Dobreta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
    'Eforie': [('Hirsova', 86)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Giurgiu': [('Bucharest', 90)],
    'Hirsova': [('Eforie', 86), ('Urziceni', 98)],
    'Iasi': [('Neamt', 87), ('Vaslui', 92)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Neamt': [('Iasi', 87)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Bucharest', 101), ('Craiova', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Rimnicu Vilcea', 80), ('Fagaras', 99)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Vaslui': [('Iasi', 92), ('Urziceni', 142)],
    'Zerind': [('Arad', 75), ('Oradea', 71)]
}

start_node = 'Arad'
goal_node = 'Bucharest'
greedy_best_first_search(graph, start_node, goal_node, heuristic)