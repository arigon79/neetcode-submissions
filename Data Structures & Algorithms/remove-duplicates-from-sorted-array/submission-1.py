class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        tracker = set()
        while i < len(nums):
            if nums[i] in tracker:
                nums.pop(i)
            else:
                tracker.add(nums[i])
                i += 1
        
        return len(nums)
