class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        tracker = set(nums)

        for n in nums:
            if (n - 1) not in tracker:
                length = 0
                while (length + n) in tracker:
                    length += 1

                res = max(res, length)
        return res