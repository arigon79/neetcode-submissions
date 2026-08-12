import math
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            distance = math.sqrt((p[0] - 0)**2 + (p[1] - 0)**2)
            heapq.heappush(heap, (distance, p))

        return [p[1] for p in heapq.nsmallest(k, heap)]
        