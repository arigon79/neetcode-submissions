class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks:
            count[t] = count.get(t, 0) + 1
        
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        t = 0
        while maxHeap or q:
            t += 1

            if maxHeap:
                val = 1 + heapq.heappop(maxHeap)
                
                if val < 0:
                    q.append([t + n, val])
            
            if q and q[0][0] == t:
                val = q.popleft()[1]
                heapq.heappush(maxHeap, val)
        
        return t


                
                    
