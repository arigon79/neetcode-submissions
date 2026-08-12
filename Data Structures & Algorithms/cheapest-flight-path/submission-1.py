class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Time: O(Elog(n*k))
        # Space: O(n + E)
        
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append([w, v])
        
        stops_to_node = {}  # stops needed to reach each node
        minHeap = [[0, src, 0]] # cost, node, stop 
        while minHeap:
            cost, node, stop = heapq.heappop(minHeap)

            if node == dst:
                return cost
            
            if stop > k:
                continue
            
            if node in stops_to_node and stops_to_node[node] <= stop:
                continue
            
            stops_to_node[node] = stop

            for neiCost, nei in adj[node]:
                heapq.heappush(minHeap, [cost + neiCost, nei, stop + 1])
        
        return -1
