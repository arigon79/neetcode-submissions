class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = 1 + count.get(task, 0)
        
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)
        queue = deque()
        t = 0

        while heap or queue:
            t += 1
            if heap:
                val = 1 + heapq.heappop(heap)

                if val < 0:
                    queue.append([val, t + n])

            if queue and queue[0][1] == t:
                new_val = queue.popleft()[0]
                heapq.heappush(heap, new_val)
            
        return t