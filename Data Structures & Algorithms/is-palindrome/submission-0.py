class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        
        while start < end:
            s_l = s[start].lower()
            e_l = s[end].lower()
            if not s_l.isalnum():
                start += 1
                continue
            if not e_l.isalnum():
                end -= 1
                continue
            if  s_l != e_l :
                return False
            start += 1
            end -= 1
    
        return True
        