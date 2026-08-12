class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        
        for num, freq in counter.items():
            heapq.heappush(heap, (freq, num))
        res = []
        for i in heapq.nlargest(k, heap):
            res.append(i[1])
        return res