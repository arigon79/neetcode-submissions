class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Time: O(nlogn)
        # Space: O(n)
        heap = [-n for n in nums]
        heapq.heapify(heap)
        
        for _ in range(k - 1):
            heapq.heappop(heap)
        
        return -heapq.heappop(heap)