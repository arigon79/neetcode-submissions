class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        tracker = {}
        for i in range(len(nums)):
            if target - nums[i] in tracker:
                res.append(tracker[target - nums[i]])
                res.append(i)
            else:
                tracker[nums[i]] = i
        
        return res