class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Time: O((4^n/sqrt(n)))
        # Space: O(n)
        
        res = []
        stack = []

        def dfs(openN, closeN):
            nonlocal res

            if openN == closeN == n:
                res.append(''.join(stack.copy()))
                return
            
            if openN < n:
                stack.append('(')
                dfs(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(')')
                dfs(openN, closeN + 1)
                stack.pop()
            
            return

        dfs(0, 0)
        return res
