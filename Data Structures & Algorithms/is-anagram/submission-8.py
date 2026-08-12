class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_tr, t_tr = {}, {}
        for i in s:
            if i not in s_tr:
                s_tr[i] = 1
            else:
                s_tr[i] += 1
        for j in t:
            if j not in t_tr:
                t_tr[j] = 1
            else:
                t_tr[j] += 1
        
        return s_tr == t_tr
        