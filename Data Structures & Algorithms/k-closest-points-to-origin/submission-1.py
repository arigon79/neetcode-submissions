class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        
        for point in points:
            xi = point[0]
            yi = point[1]

            distance = ((xi - 0)**2 + (yi - 0)**2)**(1/2)

            heapq.heappush(closest, (-distance, point))

        for _ in range(len(closest) - k):
            heapq.heappop(closest)
            
        return [val[1] for val in closest]
        