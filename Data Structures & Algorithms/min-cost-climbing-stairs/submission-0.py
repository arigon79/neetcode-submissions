class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {len(cost): 0}
        
        def climb(i):
            if i >= len(cost):
                return mem[len(cost)]
            if i in mem:
                return mem[i]
        
            mem[i] = cost[i] + min(climb(i + 1), climb(i + 2))
            return mem[i]
        
        return min(climb(0), climb(1))

        