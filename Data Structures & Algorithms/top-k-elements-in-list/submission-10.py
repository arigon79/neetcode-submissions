class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        heap = []
        for num, c in count.items():
            heapq.heappush(heap, (c, num))
        return [r[1] for r in heapq.nlargest(k, heap)]