class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # n = numCourses
        # Time: O(n)
        # Space: O(n)
        preMap = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        cycle = set()

        def dfs(node):
            if preMap[node] == []:
                return True
                    
            if node in cycle:
                return False
            
            cycle.add(node)

            for nei in preMap[node]:
                if not dfs(nei):
                    return False
            
            cycle.remove(node)
            preMap[node] = []
            return True
            

        for c in preMap:
            if not dfs(c):
                return False
        
        return True