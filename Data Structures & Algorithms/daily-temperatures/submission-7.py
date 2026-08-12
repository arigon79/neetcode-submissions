class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        i, j = 0, 1

        while i < j and j < len(temperatures):
            if temperatures[i] < temperatures[j]:
                res[i] = j - i
                i += 1
                j = i + 1
            else:
                if j == len(temperatures) - 1:
                    i += 1
                    j = i + 1
                else:
                    j += 1

        return res



        