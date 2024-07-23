from collections import deque
"""
Graphs --> Adjacency List
"""

# GraphNode used for adjacency list
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbours = []

# Or use a HashMap
adjList = { "A": [], "B": [] }

# Given directed edges, build an adjacency list
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C ", "E"], ["E", "D"]]

adjList = {}

for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    adjList[src].append(dst)


# Count paths --> DFS (backtracking)
"""
Time complexity: O(n**v)
"""
def dfs(node, target, adjList, visit):
    if node in visit:
        return 0
    if node == target:
        return 1
    
    count = 0
    visit.add(node)
    for neighbour in adjList[node]:
        count += dfs(neighbour, target, adjList, visit)
    visit.remove(node)

    return count

print(dfs("A", "E", adjList, set()))


# Shortest path from node to target --> BFS
"""
Size of graph: O(v)
Time complexity: O(V + E)
Space complexity: O(V)
"""
def bfs(node, target, adjList):
    length = 0
    visit = set()
    visit.add(node)
    queue = deque()
    queue.append(node)

    while queue:
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr == target:
                return length
            
            for neighbour in adjList[curr]:
                if neighbour not in visit:
                    visit.add(neighbour)
                    queue.append(neighbour)
        length += 1
    return length

print(bfs("A", "E", adjList))