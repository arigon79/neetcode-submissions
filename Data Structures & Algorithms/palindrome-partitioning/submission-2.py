class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        res = []

        def dfs(i, subset):
            if i == len(s):
                res.append(subset.copy())
                return None
            
            for j in range(i, len(s)):
                if isPal(s, i, j):
                    subset.append(s[i: j + 1])
                    dfs(j + 1, subset)
                    subset.pop()
            return None
        
        dfs(0, [])
        return res
