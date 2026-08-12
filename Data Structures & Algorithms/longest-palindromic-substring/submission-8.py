class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s[0]
        
        memo = {}
        # i = start, j = end
        def isPal(i, j):
            if i >= j:
                return True
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if s[i] == s[j]:
                memo[(i, j)] = isPal(i + 1, j - 1)
            else:
                return False
            
            return memo[(i, j)]
            
        
        start, max_len = 0, 0

        for i in range(n):
            for j in range(i, n):
                if isPal(i, j):
                    if (j - i + 1) > max_len:
                        max_len = j - i + 1
                        start = i
        return s[start: start + max_len]
                