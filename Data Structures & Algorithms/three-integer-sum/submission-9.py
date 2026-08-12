class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        # [-4, -1, -1, 0, 1, 2]
        
        for i, val in enumerate(nums):
            if val > 0:
                break
            
            if i > 0 and val == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                target = val + nums[l] + nums[r]
                
                if target == 0:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif target < 0:
                    l += 1
                else:
                    r -= 1
        return res


        