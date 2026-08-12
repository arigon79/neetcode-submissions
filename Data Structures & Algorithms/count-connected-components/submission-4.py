class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        visit = set()
        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)
            for nei in adj[node]:
                dfs(nei)

            return
        
        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
        
        return count
                