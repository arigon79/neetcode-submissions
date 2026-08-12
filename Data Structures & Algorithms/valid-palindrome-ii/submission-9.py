class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        count = 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            
            if s[l].lower() != s[r].lower():
                if s[l].lower() == s[r - 1].lower()  and count:
                    r -= 1
                    count = 0
                    continue
                if s[l + 1].lower() == s[r].lower() and count:
                    l += 1
                    count = 0
                    continue
                
                return False
            
            else:
                l += 1
                r -= 1
        
        return True


