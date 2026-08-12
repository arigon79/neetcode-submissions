class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        if len(s) != len(t):
            return False

        for i in s:
            if i in s_hash:
                s_hash[i] += 1
            else:
                s_hash[i] = 1

        for j in t:
            if j in t_hash:
                t_hash[j] += 1
            else:
                t_hash[j] = 1

        for key, value in t_hash.items():
            if not key in s_hash or s_hash[key] != value:
                return False

        return True