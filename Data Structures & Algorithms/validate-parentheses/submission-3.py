class Solution:
    def isValid(self, s: str) -> bool:
        endToStart = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for i in s:
            if i not in endToStart:
                stack.append(i)
            else:
                if stack and endToStart[i] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False