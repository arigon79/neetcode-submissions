class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()

        def dfs(node):
            if node in visit:
                return False
            
            if preMap[node] == []:
                return True
            
            visit.add(node)
            
            for nei in preMap[node]:
                if not dfs(nei):
                    return False
            
            visit.remove(node)
            return True
        
        for crs in preMap:
            if not dfs(crs):
                return False
            
        return True