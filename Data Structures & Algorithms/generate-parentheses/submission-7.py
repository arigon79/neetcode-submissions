class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Time: O((4^n) / (n^(1/2)))
        # Space: O(n)

        res = []
        stack = []

        def dfs(openN, closeN):
            if openN == closeN == n:
                res.append(''.join(stack))
                return None
            
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