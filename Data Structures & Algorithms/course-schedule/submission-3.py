class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        cycle = set()

        def dfs(node):
            if node in cycle:
                return False
            
            if preMap[node] == []:
                return True
            
            cycle.add(node)

            for nei in preMap[node]:
                if not dfs(nei):
                    return False
            
            cycle.remove(node)
            return True
        
        for crs in preMap:
            if not dfs(crs):
                return False
        
        return True