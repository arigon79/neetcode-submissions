class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_val = min([len(i) for i in strs])
        
        res = ''

        for i in range(min_val):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return res
            
            res += strs[0][i]

    
        return res