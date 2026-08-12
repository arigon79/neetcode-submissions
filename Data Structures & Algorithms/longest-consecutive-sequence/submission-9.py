class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        track = set(nums)
        for n in nums:
            if (n - 1) not in track:
                length = 1
                while (n + length) in track:
                    length += 1
                
                res = max(res, length)
        return res
