class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        
        pairs = sorted(pairs, reverse=True)

        for p, s in pairs:
            val = (target - p) / s
            stack.append(val)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
            
        
        