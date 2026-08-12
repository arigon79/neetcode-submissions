class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {c: [] for c in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        res = []
        cycle = set()
        visit = set()

        def dfs(node):
            if node in visit:
                return True
            if node in cycle:
                return False
            
            cycle.add(node)
            for nei in preMap[node]:
                if not dfs(nei):
                    return False
            
            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
            
        return res
