class Solution:
    def longestPalindrome(self, s: str) -> str:
        def ispalindrome(s):
            l = 0
            r = len(s) - 1

            while l <= r:
                if s[l] != s[r]:
                    return False

                l +=1
                r -= 1
            
            return True
        
        res = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                if ispalindrome(s[i:j + 1]):
                    print(s[i:j+1])
                    print(len(res))
                    res = res if len(res) > len(s[i: j + 1]) else s[i:j + 1]
        
        return res



