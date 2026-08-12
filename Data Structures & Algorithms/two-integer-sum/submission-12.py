class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        tracker = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in tracker:
                res.append(tracker[diff])
                res.append(i)
            else:
                tracker[nums[i]] = i
        return res