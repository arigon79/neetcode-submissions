class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        res, curSum = 0, 0
        for num in nums:
            curSum += num
            diff = curSum - k
            
            res += prefix.get(diff, 0)

            prefix[curSum] = 1 + prefix.get(curSum, 0)

        return res