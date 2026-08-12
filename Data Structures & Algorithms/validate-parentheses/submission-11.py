class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'}' : '{', ')': '(', ']': '['}
        stack = []

        for p in s:
            if p not in mapping:
                stack.append(p)
            else:
                if stack:
                    p2 = stack.pop()
                    if mapping[p] != p2:
                        return False
                else:
                    return False

        return False if len(stack) else True


