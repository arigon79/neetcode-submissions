class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = set()
        for i in nums:
            if i not in tracker:
                tracker.add(i)
            else:
                return True
        return False