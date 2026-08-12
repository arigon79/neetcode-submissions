class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = 0
        numSet = set(nums)

        for num in nums:
            if num in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                l = max(l, length)

        return l

            