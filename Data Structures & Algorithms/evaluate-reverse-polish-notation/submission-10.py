class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            signs = ['+', '-', '*', '/']

            if token not in signs:
                stack.append(int(token))
            else:
                a = int(stack.pop())
                b = int(stack.pop())
            
                if token == "+":
                    stack.append(a + b)
                elif token == '-':
                    stack.append(b - a)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(b / a))

        return stack[-1]
                        
                    