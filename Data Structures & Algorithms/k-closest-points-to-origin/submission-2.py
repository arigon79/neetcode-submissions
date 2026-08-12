class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = (x**2 + y**2)**(1/2)
            heapq.heappush(heap, (distance, [x, y]))
        
        closest = heapq.nsmallest(k, heap)
        res = []
        for d, p in closest:
            res.append(p)
        
        return res