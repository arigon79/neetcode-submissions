class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        #time complexity(n*m)
        #space complexity: O(1)
        smallest = float('inf')
        for s in strs:
            if len(s) < smallest:
                smallest = len(s)

        for i in range(smallest):
            prev = strs[0][i]
            for s in strs[1:]:
                if s[i] != prev:
                    return res
            res += prev
        
        return res