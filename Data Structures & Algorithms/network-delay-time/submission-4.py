class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Time: O(ElogV)
        # Space: O(E + V)
        adj = defaultdict(list)
        for n1, n2, w in times:
            adj[n1].append((n2, w))

        visit = set()
        minHeap = [(0, k)]
        res = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            res = max(res, w1)

            for n2, w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return res if len(visit) == n else -1
