class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(nlogk)
        # Space: O(k)
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]