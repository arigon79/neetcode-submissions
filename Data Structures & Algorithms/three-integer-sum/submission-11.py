class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n^2)
        # Space: O(m)
        nums = sorted(nums)
        n = len(nums)
        res = []
        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    cur = [nums[i], nums[l], nums[r]]
                    if cur not in res:
                        res.append(cur)
                    l += 1
                    r -= 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        return res