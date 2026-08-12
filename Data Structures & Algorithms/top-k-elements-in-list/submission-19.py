class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Overal time: O(nlogn)
        # Overall Space: O(n)
        counter = Counter(nums) # O(n)
        heap = []
        # Time: O(nlogn)
        for key in counter: 
            heapq.heappush(heap, (counter[key], key)) 
        # O(nlogk)
        return [res[1] for res in heapq.nlargest(k, heap)]