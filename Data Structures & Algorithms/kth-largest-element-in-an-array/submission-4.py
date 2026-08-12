class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Space: O(n)
        # Time: O(nlogk)
        heap = [-n for n in nums]
        heapq.heapify(heap)

        return -heapq.nsmallest(k, heap)[-1]