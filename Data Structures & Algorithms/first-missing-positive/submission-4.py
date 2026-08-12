class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        maxVal = max(nums)
        print(nums, maxVal)
        for i in range(1, maxVal + 1):
            if i in nums:
                continue
            else:
                return i
        return maxVal + 1
        