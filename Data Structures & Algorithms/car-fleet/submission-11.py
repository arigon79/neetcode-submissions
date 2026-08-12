class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 0 -> 2 -> 4 -> 6 -> 8 -> 10 = 5
        # 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 = 7
        # 2 -> 5 -> 8 -> 11 = 4
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        pairs.sort(reverse=True)
        
        stack = []
        for p, s in pairs:
            t = (target - p)/s
            print(f"stack: {stack}, {p}, {s}")
            if stack and stack[-1] >= t:
                continue
            else:
                stack.append(t)
        return len(stack)
