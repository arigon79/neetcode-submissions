class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {} 
        for t in tasks:
            count[t] = 1 + count.get(t, 0) # O(m)
        
        heap = [-c for c in count.values()] # O(k)
        heapq.heapify(heap) # O(k)
        q = deque()
        t = 0

        # Time: O(mlogk) = O(m * 1) = O(m)
        # Space: O(1)
        while q or heap:
            t += 1
            if heap:
                val = 1 + heapq.heappop(heap) # O(logk) where logk = 1 as k <=26. 
                                              # So O(logk) = O(1)
                if val < 0:
                    q.append((val, t + n))
            
            if q and q[0][1] == t:
                new_val = q.popleft()[0]    
                heapq.heappush(heap, new_val)   # O(logk) = O(1)
        return t
                

                

            