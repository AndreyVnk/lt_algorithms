'''
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.
'''

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        graph = [set() for _ in range(n)]
        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)

        visited = set()

        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            for neigh in graph[node]:
                dfs(neigh)
            return 1

        return sum(dfs(node) for node in range(n)) - 1

# Time: O(n)

