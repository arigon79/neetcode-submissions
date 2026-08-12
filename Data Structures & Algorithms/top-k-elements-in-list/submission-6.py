class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)

        for n in nums:
            cnt[n] += 1
        
        arr = []
        for key, val in cnt.items():
            arr.append([val, key])
        
        arr.sort()
        res = []
        for _ in range(k):
            res.append(arr.pop()[1])

        return res

        
