class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visit = set()

        def dfs(node):
            if node in visit:
                return False # Cycle detected
            
            if preMap[node] == []:
                return True

            visit.add(node)

            for nei in preMap[node]:
                if not dfs(nei):
                    return False
            visit.remove(node)
            preMap[node] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
            
        return True