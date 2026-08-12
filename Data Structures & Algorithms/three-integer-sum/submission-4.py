class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if val > 0:
                break

            if i > 0 and val == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                target = val + nums[l] + nums[r]

                if target == 0:
                    if [val, nums[l], nums[r]] not in res:
                        res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    r -= 1

        return res