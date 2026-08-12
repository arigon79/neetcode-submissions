class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one, two = cost[n - 1], 0
        print(one, two)
        for i in range(n - 2, -1, -1):
            temp = one
            one = min(cost[i] + two, cost[i] + one)
            two = temp
        
        return min(one, two)