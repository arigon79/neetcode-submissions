class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]

        cnt = 1

        for i in range(1, len(nums)):
            if nums[i] == res:
                cnt += 1
                continue
            
            cnt -= 1

            if cnt < 0:
                res = nums[i]
            
        return res
                