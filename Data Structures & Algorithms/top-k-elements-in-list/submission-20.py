class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]
        
        for item, count in freq.items():
            bucket[count].append(item)
    
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res