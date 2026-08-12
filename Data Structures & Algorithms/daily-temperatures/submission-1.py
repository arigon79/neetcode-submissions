class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = [0] * n
        l, r = 0, 0
        while l < n:
            while r < n:
                if temperatures[r] > temperatures[l]:
                    break
                r += 1
            results[l] = r - l if r != n else 0
            l += 1
            r = l
        return results
