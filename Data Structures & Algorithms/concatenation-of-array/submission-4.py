class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        n = len(nums)
        res = [''] * 2 * n

        for i in range(n):
            res[i] = nums[i]
            res[i + n] = nums[i]
        
        return res