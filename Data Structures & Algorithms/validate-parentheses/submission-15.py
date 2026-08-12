class Solution:
    def isValid(self, s: str) -> bool:
        tracker = {
            '}': '{',
            ')': '(',
            ']' : '['
        }
        # Time: O(n)
        # Space: O(n)
        stack = []
        for c in s:
            if c not in tracker:
                stack.append(c)
            else:
                if stack and stack.pop() == tracker[c]:
                    continue
                else:
                    return False
        
        return True if len(stack) == 0 else False

