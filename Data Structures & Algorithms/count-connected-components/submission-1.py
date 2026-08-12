class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visit = set()

        def dfs(node):
            if node in visit:
                return

            visit.add(node)

            for nei in adjList[node]:
                dfs(nei)

        count = 0

        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1

        return count