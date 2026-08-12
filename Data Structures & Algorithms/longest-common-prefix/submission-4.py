class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        
        max_cnt = min([len(s) for s in strs])
        
        i = 0
        
        for i in range(max_cnt):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return res  
                
            res += strs[0][i]
        
        return res
                

