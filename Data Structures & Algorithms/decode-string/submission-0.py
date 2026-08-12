class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ']':
                res = ''

                while stack[-1] != '[':
                    res = stack.pop() + res
                stack.pop()

                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                res = res * int(num)
                stack.append(res)
            else:
                stack.append(c)

        return ''.join(stack)
