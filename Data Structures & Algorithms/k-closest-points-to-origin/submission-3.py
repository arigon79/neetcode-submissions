class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(distances, (distance, [x, y]))
        
        res = []
        for _ in range(k):
            res.append((heapq.heappop(distances))[1])
        
        return res