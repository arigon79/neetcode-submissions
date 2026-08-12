class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # n = len(digits)
        # Time: O(n* 4^n)
        # Space: O(1)
        
        if len(digits) == 0:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []    

        def dfs(i, subset):
            if i == len(digits):
                res.append("".join(subset))
                return
            
            s = mapping[digits[i]]
            
            for j in range(len(s)):
                subset.append(s[j])
                dfs(i + 1, subset)
                subset.pop()
            
            return 
        
        dfs(0, [])
        return res