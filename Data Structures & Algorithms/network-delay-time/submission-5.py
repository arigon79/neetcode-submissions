class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for n1, n2, w in times:
            adj[n1].append((n2, w))
        
        print(adj)
        minHeap = [(0, k)]
        t = 0
        visit = set()

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            t = w1
            visit.add(n1)

            for n2, w2 in adj[n1]:
                print(n2, w2)
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
            
        return t if len(visit) == n else -1