class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        
        for c in s:
            if c not in mapping:
                stack.append(c)
                print
            else:
                if stack and stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
