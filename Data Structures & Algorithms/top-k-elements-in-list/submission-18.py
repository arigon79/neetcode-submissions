class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for key in counter:
            heapq.heappush(heap, (counter[key], key))
            
        return [res[1] for res in heapq.nlargest(k, heap)]