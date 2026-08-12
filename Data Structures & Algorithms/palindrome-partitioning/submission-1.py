class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(s):
            # Time: O(n)
            # Space: O(1)
            l, r = 0, len(s) - 1
            while l < r:
                if not s[l].lower().isalnum():
                    l += 1
                if not s[r].lower().isalnum():
                    r -= 1
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i, subset):
            nonlocal res

            if i == len(s):
                res.append(subset.copy())
                return 
            
            for j in range(i, len(s)):
                subString = s[i : j + 1]
                if isPalindrome(subString):
                    subset.append(subString)
                    dfs(j + 1, subset)
                    subset.pop()
            
        dfs(0, [])
        return res
            





        return [[]]