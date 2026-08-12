class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [n for n in nums if n > 0]
        if len(nums) == 0:
            return 1
        maxVal = max(nums)
        print(nums, maxVal)
        for i in range(1, maxVal + 1):
            if i in nums:
                continue
            else:
                return i
        return maxVal + 1
        