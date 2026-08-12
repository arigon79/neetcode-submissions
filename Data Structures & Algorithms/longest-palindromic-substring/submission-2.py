class Solution:
    def longestPalindrome(self, s: str) -> str:  
        def isPal(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        count = 0
        res = None

        for i in range(len(s)):
            for j in range(i, len(s)):
                c = s[i:j + 1]
                if isPal(c, 0, len(c) - 1) and len(c) > count:
                    count = len(c)
                    res = c
                    print(c)
        return res
                    
        

