'''
You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.
'''

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b, p in roads:
            graph[a].append((b, p))
            graph[b].append((a, p))

        visited = set()
        cost = math.inf

        def dfs(node):
            if node in visited:
                return
            nonlocal cost
            visited.add(node)

            for neigh, pos in graph[node]:
                cost = min(cost, pos)
                dfs(neigh)

        dfs(1)

        return cost

# Time: O(n)

