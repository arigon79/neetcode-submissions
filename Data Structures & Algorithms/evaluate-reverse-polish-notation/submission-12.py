class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
        return stack[-1]
                        
