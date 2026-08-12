class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        m = len(nums) / 2
        if len(nums) % 2 == 0:
            a = nums[int(m - 1)]
            b = nums[int(m)] 
            return (a + b)/2
        else:
            return nums[math.floor(m)]
            