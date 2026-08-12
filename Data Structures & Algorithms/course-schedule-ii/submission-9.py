class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visit, cycle = set(), set()
        res = []

        def dfs(node):
            if node in cycle:
                return False
            
            if node in visit:
                return True
            
            cycle.add(node)

            for nei in preMap[node]:
                if not dfs(nei):
                    return False
            
            cycle.remove(node)
            res.append(node)
            visit.add(node)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
            
        return res