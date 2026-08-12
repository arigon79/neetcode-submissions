class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = defaultdict(list)
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i, n):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)

                edges[i].append((distance, j))
                edges[j].append((distance, i))
        
        res = 0
        visit = set()
        minHeap = [(0, 0)]

        while len(visit) < n:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            res += cost
            visit.add(i)

            for neiCost, nei in edges[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, (neiCost, nei))
        
        return res 
