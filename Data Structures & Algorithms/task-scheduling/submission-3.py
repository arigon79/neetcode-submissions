class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks:
            count[t] = 1 + count.get(t, 0)
        
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        q = deque()
        t = 0

        while q or heap:
            t += 1
            if heap:
                val = 1 + heapq.heappop(heap)
                
                if val < 0:
                    q.append((val, t + n))
            
            if q and q[0][1] == t:
                new_val = q.popleft()[0]
                heapq.heappush(heap, new_val)
        
        return t
                

                

            