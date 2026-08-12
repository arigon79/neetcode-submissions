class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tracker = set()
        for n in nums:
            if n in tracker:
                return n
            else:
                tracker.add(n)
        
