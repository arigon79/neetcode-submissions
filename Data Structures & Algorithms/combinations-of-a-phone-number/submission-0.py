class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz", 
        }
        res = []
        
        if len(digits) == 0:
            return res

        def backtrack(i, subset):
            if i == len(digits):
                res.append(''.join(subset.copy()))
                return
            
            for c in mapping[digits[i]]:
                subset.append(c)
                backtrack(i + 1, subset)
                subset.pop()
            
        backtrack(0, [])
        return res