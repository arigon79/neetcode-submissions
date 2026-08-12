class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        i = 0
        count = {}
        for s in strs:
            count[s] = len(s)
        
        min_val = min(count.values())

        for j in range(min_val):
            c = None
            for s in strs:
                if c == None:
                    c = s[j]
                else:
                    if c != s[j]:
                        return res
            res += c
        return res
                    
                

        