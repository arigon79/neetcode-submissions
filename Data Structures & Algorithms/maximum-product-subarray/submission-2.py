class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        prefix = suffix = 1


        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[ n - 1 - i] * (suffix or 1)
            print(f"prefix: {prefix}, suffix: {suffix}")
            res = max(res, suffix, prefix)

        return res
