class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(openL, closeL):
            if openL == closeL == n:
                res.append(''.join(stack))
                return
            
            if openL < n:
                stack.append('(')
                dfs(openL + 1, closeL)
                stack.pop()
            
            if closeL < openL:
                stack.append(')')
                dfs(openL, closeL + 1)
                stack.pop()
            return
        dfs(0, 0)
        return res
            