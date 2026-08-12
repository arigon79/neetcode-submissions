class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)   
        stack = []
        
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                tempVal, tempIdx = stack.pop()
                results[tempIdx] = idx - tempIdx
            stack.append((temp, idx))
        
        return results