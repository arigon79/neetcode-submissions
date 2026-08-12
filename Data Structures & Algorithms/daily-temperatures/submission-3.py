class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackVal, stackIdx = stack.pop()
                results[stackIdx] = i - stackIdx
                
            stack.append([t, i])

        return results
        
