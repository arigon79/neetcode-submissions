class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        majority = nums[0]

        for num in nums[1:]:
            if num == majority:
                count += 1
            else:
                count -= 1
            
            if count < 0:
                majority = num
        
        return majority