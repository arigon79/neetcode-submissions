class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [()] * len(speed)
        for i in range(len(speed)):
            pairs[i] = (position[i], speed[i])
        pairs.sort(reverse=True)
        
        for i in range(len(pairs)):
            d, s = target - pairs[i][0], pairs[i][1]
            t = d/s
            if stack and t <= stack[-1]:
                continue
            stack.append(t)
        
        return len(stack)

