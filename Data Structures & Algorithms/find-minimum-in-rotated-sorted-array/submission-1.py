class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        res = nums[0]

        while start <= end:
            if nums[start] < nums[end]:
                return min(res, nums[start])

            mid = (start + end) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid - 1

        return res
            

