class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        adjList = {i: [] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        visit = set()
        
        def dfs(node, prevNode):
            if node in visit:
                return True
            visit.add(node)
            for nei in adjList[node]:
                if nei == prevNode:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True

        for i in range(n):
            if i not in visit and dfs(i, -1):
                count += 1
        
        return count