class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        prev = None
        r = 0
        while r < len(nums):
            if nums[r] == prev:
                nums.pop(r)
                continue
            k += 1
            prev = nums[r]
            r += 1
        return k
