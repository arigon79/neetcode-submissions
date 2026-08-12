class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)

        for i in range(len(nums)):
            for j in range(i+ 1, len(nums)):
                l = j + 1
                r = len(nums) - 1
                
                while l < r:
                    summation = nums[i] + nums[j] + nums[l] + nums[r]
                    if summation == target:
                        if [nums[i], nums[j], nums[l], nums[r]] not in res:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                    elif summation < target:
                        l += 1
                    else:
                        r -= 1

        return res
                

        