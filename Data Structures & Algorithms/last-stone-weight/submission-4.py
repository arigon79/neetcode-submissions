class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heap = stones
        heapq.heapify(heap)
        
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if  y > x:
                heapq.heappush(stones,  x - y)
            
        return abs(heap[0]) if heap else 0
            