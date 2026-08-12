class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
            
        adList = {n: [] for n in range(n)}
        for a, b in edges:
            adList[a].append(b)
            adList[b].append(a)
        visit = set()

        def dfs(node, prevNode):
            if node in visit:
                return False

            visit.add(node)
            
            for nei in adList[node]:
                if nei == prevNode:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visit) == n
            