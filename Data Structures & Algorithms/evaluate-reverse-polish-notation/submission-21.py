class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        stack = []
        # Time: O(n)
        # Space: O(n)

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if t == "+":
                    res = a + b
                elif t == '-':
                    res = a - b
                elif t == '*':
                    res = a * b
                else:
                    res = int(a / b)
                stack.append(int(res))
        return stack[-1]