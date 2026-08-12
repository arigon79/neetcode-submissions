class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'}' : '{', ')': '(', ']': '['}
        stack = []

        for p in s:
            if p not in mapping:
                stack.append(p)
            else:
                if stack and stack[-1] == mapping[p]:
                    stack.pop()
                else:
                    return False

        return False if len(stack) else True


