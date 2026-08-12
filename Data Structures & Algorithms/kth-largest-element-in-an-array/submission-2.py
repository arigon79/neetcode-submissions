class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)

        i = 1
        while i <= k:
            val = heapq.heappop(heap)
            if i == k:
                return -val
            i += 1
        return 
            

        