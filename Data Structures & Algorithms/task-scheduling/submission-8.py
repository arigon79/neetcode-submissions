class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # m = num of tasks
        # k = num of unique task
        
        # Overall time: O(mlogk) but k == 26 or constant. So O(m * 1) = O(m) 
        # Space: O(1)

        count = {}  # Space: O(k)
        for t in tasks: # O(m)
            count[t] = 1 + count.get(t, 0) 
        maxHeap = [-c for c in count.values()] # Space: O(k) #O(k)
        heapq.heapify(maxHeap) # Time: O(k)
        q = deque()
        t = 0

        while maxHeap or q:
            t += 1
            if maxHeap:
                val = 1 + heapq.heappop(maxHeap) #O(logk)
                if val < 0:
                    q.append([val, t + n]) # O(1)
            
            if q and q[0][1] == t:
                val = q.popleft()[0] # O(1)
                heapq.heappush(maxHeap, val) # O(logk)
        return t
    