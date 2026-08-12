class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = Counter(nums)
        res = []
        for key, val in tracker.items():
            res.append((val, key))
        
        heapq.heapify(res)
        return [val[1] for val in heapq.nlargest(k, res)]
        
