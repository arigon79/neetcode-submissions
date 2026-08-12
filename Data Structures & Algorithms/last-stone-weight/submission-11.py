class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        # Time: O(nlogn)
        # Space: O(n)
        heapq.heapify(heap)

        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            
            if x == y:
                continue
            else:
                heapq.heappush(heap, -abs(y - x))

        return -heap[0] if heap else 0

