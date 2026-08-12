class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                print(i, j)
                if temperatures[i] < temperatures[j]:
                    print('bigger')
                    res[i] = j - i
                    break
        return res