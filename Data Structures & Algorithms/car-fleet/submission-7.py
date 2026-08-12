class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []

        for i in range(len(speed)):
            pair.append((position[i], speed[i]))
        
        pair = sorted(pair, reverse=True)
        print(pair)
        
        stack = []

        for p, s in pair:
            stack.append((target - p) / s)
            print(stack)

            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
