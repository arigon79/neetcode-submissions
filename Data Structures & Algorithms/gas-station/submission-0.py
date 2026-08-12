class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        if sum(cost) > sum(gas):
            return -1
        
        for i in range(n):
            tank = gas[i] - cost[i]

            if tank < 0:
                continue
            
            j = (i + 1) % n
            while j != i:
                tank += gas[j]
                tank -= cost[j]
                if tank < 0:
                    break
                j = (j + 1) % n
            
            if j == i:
                return i
        
        return -1
