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


# Count paths (backtracking)
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