class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        nums.sort()
        # nums=[9,1,4,7,3,-1,0,5,8,-1,6]
        # sort=[-1,-1,0,1,3,4,5,6,7,8,9]
        res = 1
        curLen = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                curLen += 1
                res = max(curLen, res)
            else:
                res = max(curLen, res)
                curLen = 1
        return res
