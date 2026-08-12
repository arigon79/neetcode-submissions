class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks:
            count[t] = 1 + count.get(t, 0)
        
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque()
        t = 0

        while maxHeap or q:
            t += 1
            if maxHeap:
                val = 1 + heapq.heappop(maxHeap)

                if val < 0:
                    q.append((val, t + n))

            if q and q[0][1] == t:
                val = q.popleft()[0]
                heapq.heappush(maxHeap, val)

        return t

