class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = []
        for num in nums:
            if num not in tracker:
                tracker.append(num)
            else:
                return True
        return False
