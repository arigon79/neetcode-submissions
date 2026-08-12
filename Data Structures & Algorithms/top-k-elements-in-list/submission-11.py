class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Overall Time Complexity: O(nlogk) or O(nlogn)~worst case
        # Overall Space Complexity: O(n)
        
        count = {} # Time: O(n) Space: O(n)
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        heap = [] # Time: O(n) Space: O(nlogn)
        for num, c in count.items():
            heapq.heappush(heap, (c, num))
        return [r[1] for r in heapq.nlargest(k, heap)] # Time: O(n) Space: O(nlogn)