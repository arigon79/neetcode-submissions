class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        
        for i, val in enumerate(nums):
            if target - val in tracker:
                return [tracker[target - val], i]
            
            tracker[val] = i
        
        return -1