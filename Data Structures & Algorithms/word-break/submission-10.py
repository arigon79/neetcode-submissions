class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # n = len(s)
        # m = len(wordDict)
        # t = max(len(wordDict))
        
        # Time: O(n*m*t)
        # Space: O(n)
        memo = { len(s) : True}

        def dfs(i):
            if i in memo:
                return memo[i]
            
            for word in wordDict:
                if (i + len(word) <= len(s) and 
                (word == s[i : i + len(word)])):
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return dfs(0)