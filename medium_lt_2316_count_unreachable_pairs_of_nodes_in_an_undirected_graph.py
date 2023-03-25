'''
You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

Return the number of pairs of different nodes that are unreachable from each other.
'''

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        graph = [set() for _ in range(n)]
        visited = set()
        sizes = [0] * n

        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        def dfs(node):
            size = 1
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    size += dfs(neigh)
            return size
        
        for node in range(n):
            if node not in visited:
                sizes[node] = dfs(node)

        ans, summ = 0, 0
        for size in sizes:
            ans += summ * size
            summ += size

        return ans

# Time: O(n)

