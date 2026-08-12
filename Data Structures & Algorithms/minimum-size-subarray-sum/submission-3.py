class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l, r = 0, 0
        tmp = 0
        while l <= r and r < len(nums):
            tmp += nums[r]

            while tmp >= target:
                res = min(res, r - l + 1)
                tmp -= nums[l]
                l += 1
            
            r += 1
        
        return 0 if res == float('inf') else res