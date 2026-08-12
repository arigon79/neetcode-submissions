class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            a = len(nums) // 2 - 1
            b = a + 1
            return (nums[a] + nums[b]) / 2
        else:
            a = len(nums) // 2
            return float(nums[a])
        
